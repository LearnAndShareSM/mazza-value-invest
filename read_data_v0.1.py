# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: obb
#     language: python
#     name: python3
# ---

# Cerchermo di arrivare velocemente a un modello di valutazione basilare per avere quanto prima una pipeline di partenza per la valutazione di un modello.
# In questo episodio cercheremo di scaricare i dati dei bilanci trimestrali degli stock presenti sul NASDAQ.
# Uno degli strumenti che impareremo a utilizzare nel nostro percorso è OpenBB,  open-source investment research software platform that gives you access to high-quality financial market data and analytical tools. Inoltre tra le API per accesso ai dati finanziari partiamo da FinancialModelingPrep di cui ho sottoscritto l'abbonamento (avendone testate diverse al momento ho valutato essere la piu completa e affidabile in termini di dati relativi ai bilanci e fondamentali di un azienda)

# Iniziamo settando l'API di FMP su openbb: 

# +
from openbb_terminal.sdk import openbb
import yaml

with open('credentials/api.yaml', 'r') as file:
    config = yaml.safe_load(file)

openbb.keys.fmp(key = config['keys']['fmp'], persist = True)


# -

# Da ricordare il comando help per avere informazioni sulle funzioni
# #help(openbb.stocks.fa.balance)
# e la documantazione SDK presente in 
#
# https://docs.openbb.co/sdk/reference
#

# Non sono riuscito a trovare un metodo su openBB che mi potesse ritornare tutta la lista ti tickers disponibili, quindi ho deciso di creare un file csv con tutti i tickers disponibili, quindi per questa operazione utilizzo direttamente la chiamata a FMP:

# +
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


# -

companies = available_companies(config['keys']['fmp'])

companies

companies_nasdaq = companies[(companies['exchangeShortName'] == "NASDAQ") & (companies['type'] == "stock")]
list_ticker = companies_nasdaq.symbol.to_list()

len(list_ticker)

companies_nasdaq.sort_values(by=['symbol'], ascending=False)

#  quando si parla di Nasdaq, si fa riferimento al Nasdaq Global Market e al Nasdaq Global Select. Il Nasdaq Global Market è il mercato principale di Nasdaq e ospita le società più grandi e liquide del mondo. Il Nasdaq Global Select è un mercato più esclusivo del Nasdaq Global Market e ospita società di dimensioni medie e grandi.

# Ad oggi, ci sono 3.949 ticker attivi associati a Nasdaq. Questi ticker rappresentano una vasta gamma di aziende, tra cui società tecnologiche, società finanziarie, società industriali e società di consumo.

# TODO: da capire quindi meglio la lista dei ticker ricavata da FMP (se sono presenti anche le variazioni storiche o semplicemente i ticker non piu attivi)

# Per esempio  Alphabet ha due classi di azioni quotate in borsa: Class A e Class C. Le azioni Class A hanno diritto di voto, mentre le azioni Class C non hanno diritto di voto. Il ticker GOOGL rappresenta le azioni Class A di Alphabet, mentre il ticker GOOG rappresenta le azioni Class C di Alphabet.
#
#

companies_nasdaq[companies_nasdaq['name'] == "Alphabet Inc."]

# Nel prossimo episodio cercheremo di estrarre lo storico di alcuni di questi ticker e storicizzare in locale i dati

#
