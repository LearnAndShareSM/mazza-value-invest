import financedatabase as fd
from investorkit.investorkit.get_data.base import get_profile, get_financial_statements
from utils.context_manager import session_scope
from utils.process_data import filter_bigint_range
from datetime import datetime
import pandas as pd
from loguru import logger

# Add the run_id to logger context
run_id = datetime.now().isoformat()
logger.bind(run_id=run_id)


def store_to_db(df, table_name, engine, SessionLocal, run_id):
    try:
        with session_scope(SessionLocal, run_id) as session:
            df.to_sql(table_name, con=engine, if_exists="append", index=False)
            session.flush()
        logger.bind(run_id=run_id).info(f"Stored data into table {table_name}")
    except Exception as e:
        logger.bind(run_id=run_id).error(
            f"Failed to store data into table {table_name}. Error: {e}"
        )


def fetch_equity_symbols(country="United States", market="NASDAQ Global Select"):
    try:
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
        logger.info(
            f"Fetched {len(list_symbols)} equity symbols for {country} - {market}"
        )
        return list_symbols
    except Exception as e:
        logger.exception(
            f"Failed to fetch equity symbols for {country} - {market}. Error: {e}"
        )


def get_new_symbols(list_symbols, engine):
    try:
        existing_symbols_query = "SELECT symbol FROM profiles;"
        existing_symbols = pd.read_sql(existing_symbols_query, con=engine)
        new_symbols = list(set(list_symbols) - set(existing_symbols["symbol"].tolist()))
        new_symbols = new_symbols[:20]
        logger.info(f"Identified {len(new_symbols)} new symbols")
        return new_symbols
    except Exception as e:
        logger.exception(f"Failed to identify new symbols. Error: {e}")


def fetch_and_store_profiles(engine, api_key, SessionLocal, run_id):
    list_symbols = fetch_equity_symbols()
    new_symbols = get_new_symbols(list_symbols, engine)

    if new_symbols:
        df_profiles = get_profile(new_symbols, api_key)
        if not df_profiles.empty:
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
            store_to_db(df_profiles_filtered, "profiles", engine, SessionLocal, run_id)
        else:
            logger.warning("No profiles found for the new symbols.")


def fetch_and_store_financial_statements(engine, api_key, SessionLocal, run_id):
    try:
        query = "SELECT DISTINCT symbol FROM cashflows2;"
        existing_symbols_df = pd.read_sql(query, engine)
        existing_symbols = set(existing_symbols_df["symbol"])

        query = "SELECT * FROM profiles;"
        df_profiles = pd.read_sql(query, engine)

        list_symbols = list(df_profiles["symbol"])
        list_symbols = [
            symbol for symbol in list_symbols if symbol not in existing_symbols
        ]

        chunks = [list_symbols[i : i + 100] for i in range(0, len(list_symbols), 100)]

        for chunk in chunks:
            df, invalid_tickers = get_financial_statements(
                tickers=chunk,
                statement="cashflow",
                api_key=api_key,
                start_date="2000-01-01",
            )
            filtered_df = filter_bigint_range(df, run_id)
            store_to_db(filtered_df, "cashflows2", engine, SessionLocal, run_id)
            logger.info(f"Stored financial statements for {len(chunk)} symbols.")
    except Exception as e:
        logger.exception(
            f"An error occurred while fetching and storing financial statements: {e}"
        )
