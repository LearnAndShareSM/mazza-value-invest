from urllib.request import urlopen
from urllib.error import HTTPError
import json
import pandas as pd

def available_companies(api_key):
  
    try:
        response = urlopen(f"https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key}")
        data = json.loads(response.read().decode("utf-8"))
    except HTTPError:
        raise ValueError("This endpoint is only for premium members. Please visit the subscription page to upgrade the "
                         "plan (Starter or higher) at https://financialmodelingprep.com/developer/docs/pricing")

    if 'Error Message' in data:
        raise ValueError(data['Error Message'])

    df = pd.DataFrame(data)
    df.loc[df["name"].isna(), "name"] = df["symbol"]
    df = df.set_index("symbol")
    
    df.reset_index(inplace=True)

    return df



def get_profile(tickers: list[str] | str, api_key: str) -> pd.DataFrame:
    """
    Gives information about the profile of a company which includes i.a. beta, company description, industry and sector.

    Args:
        ticker (list or string): the company ticker (for example: "AAPL")
        api_key (string): the API Key obtained from https://site.financialmodelingprep.com/developer/docs/pricing/jeroen/

    Returns:
        pd.DataFrame: the profile data.
    """

    naming: dict = {
        "symbol": "Symbol",
        "price": "Price",
        "beta": "Beta",
        "volAvg": "Average Volume",
        "mktCap": "Market Capitalization",
        "lastDiv": "Last Dividend",
        "range": "Range",
        "changes": "Changes",
        "companyName": "Company Name",
        "currency": "Currency",
        "cik": "CIK",
        "isin": "ISIN",
        "cusip": "CUSIP",
        "exchange": "Exchange",
        "exchangeShortName": "Exchange Short Name",
        "industry": "Industry",
        "website": "Website",
        "description": "Description",
        "ceo": "CEO",
        "sector": "Sector",
        "country": "Country",
        "fullTimeEmployees": "Full Time Employees",
        "phone": "Phone",
        "address": "Address",
        "city": "City",
        "state": "State",
        "zip": "ZIP Code",
        "dcfDiff": "DCF Difference",
        "dcf": "DCF",
        "ipoDate": "IPO Date",
    }

    if isinstance(tickers, str):
        ticker_list = [tickers]
    elif isinstance(tickers, list):
        ticker_list = tickers
    else:
        raise ValueError(f"Type for the tickers ({type(tickers)}) variable is invalid.")

    profile_dataframe: pd.DataFrame = pd.DataFrame()

    invalid_tickers = []
    for ticker in ticker_list:
        try:
            url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={api_key}"
            profile_dataframe[ticker] = get_financial_data(ticker=ticker, url=url).T
        except ValueError:
            print(f"No profile data found for {ticker}")
            invalid_tickers.append(ticker)

    if not profile_dataframe.empty:
        profile_dataframe = profile_dataframe.rename(index=naming)
        profile_dataframe = profile_dataframe.drop(
            ["image", "defaultImage", "isEtf", "isActivelyTrading", "isAdr", "isFund"],
            axis=0,
        )

    return profile_dataframe, invalid_tickers