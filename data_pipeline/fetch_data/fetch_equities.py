import financedatabase as fd
from investorkit.investorkit.get_data.base import get_profile, get_financial_statements
from monitoring.prometheus_metrics import (
    EXECUTION_TIME,
    NEW_SYMBOLS,
    SYMBOLS_LENGTH,
    FETCH_PARAMS,
    MISSING_SYMBOLS,
)
from utils.context_manager import session_scope
from utils.process_data import filter_bigint_range
from datetime import datetime
import pandas as pd

run_id = datetime.now().isoformat()


def store_to_db(df, table_name, engine, SessionLocal):
    with session_scope(SessionLocal) as session:
        df.to_sql(table_name, con=engine, if_exists="append", index=False)
        session.flush()


@EXECUTION_TIME.time()
def fetch_equity_symbols(country="United States", market="NASDAQ Global Select"):
    equities = fd.Equities()
    selected_columns = [
        "name",
        "currency",
        "sector",
        "industry_group",
        "industry",
        "exchange",
        "market",
        "market_cap",
    ]
    us_equities = equities.select(country=country)
    df_equities = us_equities[us_equities["market"] == market][selected_columns]
    list_symbols = list(df_equities.index)

    SYMBOLS_LENGTH.labels(run_id=run_id).set(len(list_symbols))
    FETCH_PARAMS.labels(country=country, market=market, run_id=run_id).set(
        len(list_symbols)
    )

    return list_symbols


@EXECUTION_TIME.time()
def get_new_symbols(list_symbols, engine):
    existing_symbols_query = "SELECT symbol FROM profiles;"
    existing_symbols = pd.read_sql(existing_symbols_query, con=engine)
    new_symbols = list(set(list_symbols) - set(existing_symbols["symbol"].tolist()))
    new_symbols = new_symbols[:20]

    NEW_SYMBOLS.labels(run_id=run_id).inc(len(new_symbols))

    return new_symbols


def fetch_and_store_profiles(engine, api_key, SessionLocal):
    list_symbols = fetch_equity_symbols()
    new_symbols = get_new_symbols(list_symbols, engine)

    if new_symbols:
        df_profiles = get_profile(new_symbols, api_key)

        if not df_profiles.empty:
            missing_symbols = set(new_symbols) - set(df_profiles["symbol"])
            MISSING_SYMBOLS.labels(run_id=run_id).inc(len(missing_symbols))

            list_cols = [
                "symbol",
                "companyName",
                "cik",
                "exchange",
                "exchangeShortName",
                "industry",
                "sector",
                "country",
                "ipoDate",
                "defaultImage",
                "isEtf",
                "isActivelyTrading",
            ]

            df_profiles_filtered = df_profiles[list_cols]
            df_profiles_filtered["ipoDate"].replace("", None, inplace=True)
            df_profiles_filtered["cik"].replace("", None, inplace=True)

            store_to_db(df_profiles_filtered, "profiles", engine, SessionLocal)
        else:
            print("No profiles found for the new symbols.")
            MISSING_SYMBOLS.labels(run_id=run_id).inc(len(new_symbols))


def fetch_and_store_financial_statements(engine, api_key, SessionLocal):
    query = "SELECT DISTINCT symbol FROM cashflows2;"
    existing_symbols_df = pd.read_sql(query, engine)
    existing_symbols = set(existing_symbols_df["symbol"])

    query = "SELECT * FROM profiles;"
    df_profiles = pd.read_sql(query, engine)

    list_symbols = list(df_profiles["symbol"])
    list_symbols = [symbol for symbol in list_symbols if symbol not in existing_symbols]

    chunks = [list_symbols[i : i + 100] for i in range(0, len(list_symbols), 100)]

    for chunk in chunks:
        df, invalid_tickers = get_financial_statements(
            tickers=chunk,
            statement="cashflow",
            api_key=api_key,
            start_date="2000-01-01",
        )

        filtered_df = filter_bigint_range(df)
        store_to_db(filtered_df, "cashflows2", engine, SessionLocal)
