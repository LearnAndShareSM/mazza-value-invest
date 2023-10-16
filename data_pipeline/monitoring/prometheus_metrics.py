from prometheus_client import Summary, Counter, Gauge

EXECUTION_TIME = Summary("function_execution_seconds", "Time spent processing.")
NEW_SYMBOLS = Counter(
    "new_symbols_fetched", "Number of new symbols fetched.", ["run_id"]
)
SYMBOLS_LENGTH = Gauge(
    "symbols_length", "Length of the list of symbols fetched.", ["run_id"]
)
TOTAL_RECORDS = Gauge(
    "total_records", "Total number of records in the profiles table.", ["run_id"]
)
FETCH_PARAMS = Gauge(
    "fetch_params",
    "Parameters passed to fetch_equity_symbols",
    ["country", "market", "run_id"],
)
MISSING_SYMBOLS = Counter(
    "missing_symbols_fetched", "Number of missing new symbols.", ["run_id"]
)
