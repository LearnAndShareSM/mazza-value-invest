from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String, Table, Text, Date
from sqlalchemy.ext.declarative import declarative_base

from .db_engine import engine

Base = declarative_base()


# Define the table with a name, columns, and constraints
class LogAvailableTickers(Base):
    __tablename__ = "log_available_tickers"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_tickers = Column(Integer, nullable=False)


class LogIngestedTickers(Base):
    __tablename__ = "log_ingested_tickers"

    id = Column(Integer, primary_key=True)
    ingestion_timestamp = Column(DateTime, nullable=False)
    ticker = Column(String, nullable=False)
    num_new_rows = Column(Integer, nullable=False)
    num_old_rows_diff_dates = Column(Integer, nullable=False)
    num_columns = Column(Integer, nullable=False)


class Balance(Base):
    __tablename__ = "fa_balance"
    fiscal_date_ending = Column(String)
    reported_currency = Column(String)
    cik = Column(String, primary_key=True)
    filling_date = Column(Date, primary_key=True)
    accepted_date = Column(Date, primary_key=True)
    calendar_year = Column(Date, primary_key=True)
    period = Column(String, primary_key=True)
    cash_and_cash_equivalents = Column(String)
    short_term_investments = Column(String)
    cash_and_short_term_investments = Column(String)
    net_receivables = Column(String)
    inventory = Column(String)
    other_current_assets = Column(String)
    total_current_assets = Column(String)
    property_plant_equipment_net = Column(String)
    goodwill = Column(String)
    intangible_assets = Column(String)
    goodwill_and_intangible_assets = Column(String)
    long_term_investments = Column(String)
    tax_assets = Column(String)
    other_non_current_assets = Column(String)
    total_non_current_assets = Column(String)
    other_assets = Column(String)
    total_assets = Column(String)
    account_payables = Column(String)
    short_term_debt = Column(String)
    tax_payables = Column(String)
    deferred_revenue = Column(String)
    other_current_liabilities = Column(String)
    total_current_liabilities = Column(String)
    long_term_debt = Column(String)
    deferred_revenue_non_current = Column(String)
    deferred_tax_liabilities_non_current = Column(String)
    other_non_current_liabilities = Column(String)
    total_non_current_liabilities = Column(String)
    other_liabilities = Column(String)
    capital_lease_obligations = Column(String)
    total_liabilities = Column(String)
    preferred_stock = Column(String)
    common_stock = Column(String)
    retained_earnings = Column(String)
    accumulated_other_comprehensive_income_loss = Column(String)
    othertotal_stockholders_equity = Column(String)
    total_stockholders_equity = Column(String)
    total_equity = Column(String)
    total_liabilities_and_stockholders_equity = Column(String)
    minority_interest = Column(String)
    total_liabilities_and_total_equity = Column(String)
    total_investments = Column(String)
    total_debt = Column(String)
    net_debt = Column(String)
    link = Column(String)
    final_link = Column(String)
    ticker = Column(String, primary_key=True)
    current_date = Column(Date)


Base.metadata.create_all(engine)
