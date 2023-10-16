from sqlalchemy import Column, String, Integer, Boolean, Date, Sequence, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# SQLAlchemy Models
class Profile(Base):
    __tablename__ = "profiles"
    symbol = Column(String, primary_key=True, index=True)
    companyName = Column(String)
    cik = Column(Integer)
    exchange = Column(String)
    exchangeShortName = Column(String)
    industry = Column(String)
    sector = Column(String)
    country = Column(String)
    ipoDate = Column(Date)
    defaultImage = Column(Boolean)
    isEtf = Column(Boolean)
    isActivelyTrading = Column(Boolean)


class CashFlow(Base):
    __tablename__ = "cashflows2"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, Sequence("cashflow_id_seq"), primary_key=True, index=True)
    date = Column(String)  # Representing period[Q-DEC] as string
    symbol = Column(String, index=True)
    reportedCurrency = Column(String)
    cik = Column(BigInteger)
    fillingDate = Column(Date)
    acceptedDate = Column(Date)
    calendarYear = Column(BigInteger)
    period = Column(String)

    # Columns changed from Integer to BigInteger
    netIncome = Column(BigInteger)
    depreciationAndAmortization = Column(BigInteger)
    deferredIncomeTax = Column(BigInteger)
    stockBasedCompensation = Column(BigInteger)
    changeInWorkingCapital = Column(BigInteger)
    accountsReceivables = Column(BigInteger)
    inventory = Column(BigInteger)
    accountsPayables = Column(BigInteger)
    otherWorkingCapital = Column(BigInteger)
    otherNonCashItems = Column(BigInteger)
    netCashProvidedByOperatingActivities = Column(BigInteger)
    investmentsInPropertyPlantAndEquipment = Column(BigInteger)
    acquisitionsNet = Column(BigInteger)
    purchasesOfInvestments = Column(BigInteger)
    salesMaturitiesOfInvestments = Column(BigInteger)
    otherInvestingActivites = Column(BigInteger)
    netCashUsedForInvestingActivites = Column(BigInteger)
    debtRepayment = Column(BigInteger)
    commonStockIssued = Column(BigInteger)
    commonStockRepurchased = Column(BigInteger)
    dividendsPaid = Column(BigInteger)
    otherFinancingActivites = Column(BigInteger)
    netCashUsedProvidedByFinancingActivities = Column(BigInteger)
    effectOfForexChangesOnCash = Column(BigInteger)
    netChangeInCash = Column(BigInteger)
    cashAtEndOfPeriod = Column(BigInteger)
    cashAtBeginningOfPeriod = Column(BigInteger)
    operatingCashFlow = Column(BigInteger)
    capitalExpenditure = Column(BigInteger)
    freeCashFlow = Column(BigInteger)

    link = Column(String)
    finalLink = Column(String)
