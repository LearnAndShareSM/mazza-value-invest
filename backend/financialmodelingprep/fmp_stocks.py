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