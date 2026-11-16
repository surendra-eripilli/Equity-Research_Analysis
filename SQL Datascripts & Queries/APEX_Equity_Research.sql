create database APEX_Equity_Research;
use APEX_Equity_Research;

-- 1 Company Overview
create table Company_overview(
    Attribute varchar(100) primary key,
    Valuess varchar(255)
);

-- 2 Quarterly Financials
create table Quarterly_Financials(
    Financial_Year int not null,
    Quarters varchar(10) not null,
    Revenue_Cr decimal(12,2),
    Operating_Profit_Cr decimal(12,2),
    Net_Profit_Cr decimal(12,2),
    Total_Assets_Cr decimal(12,2),
    Total_Liabilities_Cr decimal(12,2),
    Total_Equity_Cr decimal(12,2),
    Cash_Equivalents_Cr decimal(12,2),
    Total_Debt_Cr decimal(12,2),
    Operating_Cash_Flow_Cr decimal(12,2),
    Eps_Rs decimal(10,2),
    Dividend_Per_Share_Rs decimal(10,2),
    primary key (Financial_Year, Quarters)
);

-- 3 Income Statement
create table Income_Statement(
    Financial_Year int not null,
    Quarters varchar(10) not null,
    Revenue_Cr decimal(12,2),
    Operating_Profit_Cr decimal(12,2),
    Net_Profit_Cr decimal(12,2),
    Eps_Rs decimal(10,2),
    Total_Expenses_Cr decimal(12,2),
    Profit_Before_Tax_Cr decimal(12,2),
    Tax_Expense_Cr decimal(12,2),
    primary key(Financial_Year, Quarters),
    foreign key(Financial_Year, Quarters)
        references Quarterly_Financials(Financial_Year, Quarters)
);

-- 4 Balance Sheet
create table Balance_Sheet(
    Financial_Year int not null,
    Quarters varchar(10) not null,
    Total_Assets_Cr decimal(12,2),
    Total_Liabilities_Cr decimal(12,2),
    Total_Equity_Cr decimal(12,2),
    Cash_Equivalents_Cr decimal(12,2),
    Total_Debt_Cr decimal(12,2),
    Other_Assets_Cr decimal(12,2),
    Liabilities_And_Equity_Cr decimal(12,2),
    primary key(Financial_Year, Quarters),
    foreign key(Financial_Year, Quarters)
        references Quarterly_Financials(Financial_Year, Quarters)
);

-- 5 Cash Flow
create table Cash_Flow(
    Financial_Year int not null,
    Quarters varchar(10) not null,
    Operating_Cash_Flow_Cr decimal(12,2),
    Investing_Cash_Flow_Cr decimal(12,2),
    Financing_Cash_Flow_Cr decimal(12,2),
    Capital_Expenditure_Cr decimal(12,2),
    Free_Cash_Flow_Cr decimal(12,2),
    primary key(Financial_Year, Quarters),
    foreign key(Financial_Year, QuarterS)
        references Quarterly_Financials(Financial_Year, Quarters)
);

-- 6 Monthly Stock Prices
create table Monthly_Stock_Prices(
    Dates date primary key,
    Opens decimal(10,2),
    High decimal(10,2),
    Low decimal(10,2),
    Closes decimal(10,2),
    Volume bigint,
    Turnover_Cr decimal(12,2),
    Monthly_Return_Pct decimal(8,2),
    MA_3_Month decimal(10,2)
);

-- 7 Peer Comparison
create table Peer_Comparison(
    Company varchar(150) primary key,
    Revenue_Cr_FY2026 decimal(12,2),
    Net_Profit_Cr_FY2026 decimal(12,2),
    EPS_Rs decimal(10,2),
    Debt_Cr decimal(12,2),
    PE_Ratio decimal(8,2),
    ROE_Pct decimal(8,2)
);
show tables;
select *from Company_Overview;
select *from Quarterly_Financials;
select *from Income_Statement;
select *from Balance_Sheet;
select *from Cash_Flow;
select *from Monthly_Stock_Prices;
select *from Peer_Comparison;

-- --
select 'Company_Overview' as Table_Name,
count(*) as Total_Records
from Company_Overview
union all
select 'Quarterly_Financials', count(*)
from Quarterly_Financials
union all
select 'Income_Statement', count(*)
from Income_Statement
union all
select 'Balance_Sheet', count(*)
from Balance_Sheet
union all
select 'Cash_Flow', count(*)
from Cash_Flow
union all
select 'Monthly_Stock_Prices', count(*)
from Monthly_Stock_Prices
union all
select 'Peer_Comparison', count(*)
from Peer_Comparison;