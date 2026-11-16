import os
import pandas as pd
from data_exploration import load_tables


def calculate_quarterly_kpis(quarterly_df):
    print("\nSTARTING QUARTERLY FINANCIAL ANALYSIS")

    # Create a copy of the original dataframe
    df = quarterly_df.copy()

    # Arrange records chronologically
    df = df.sort_values(
        by=["Financial_Year", "Quarters"]
    ).reset_index(drop=True)

    # 1. Revenue Growth
    df["Revenue_Growth_Pct"] = (
        df["Revenue_Cr"].pct_change(fill_method=None) * 100
    )

    # 2. Operating Profit Growth
    df["Operating_Profit_Growth_Pct"] = (
        df["Operating_Profit_Cr"].pct_change(fill_method=None) * 100
    )

    # 3. Net Profit Growth
    df["Net_Profit_Growth_Pct"] = (
        df["Net_Profit_Cr"].pct_change(fill_method=None) * 100
    )

    # 4. Operating Profit Margin
    df["Operating_Profit_Margin_Pct"] = (
        df["Operating_Profit_Cr"] / df["Revenue_Cr"] * 100
    )

    # 5. Net Profit Margin
    df["Net_Profit_Margin_Pct"] = (
        df["Net_Profit_Cr"] / df["Revenue_Cr"] * 100
    )

    # 6. Debt-to-Equity Ratio
    df["Debt_to_Equity_Ratio"] = (
        df["Total_Debt_Cr"] / df["Total_Equity_Cr"]
    )

    # 7. Operating Cash Flow to Net Profit
    df["Operating_Cash_Flow_to_Net_Profit_Pct"] = (
        df["Operating_Cash_Flow_Cr"] / df["Net_Profit_Cr"] * 100
    )

    # Round calculated columns
    calculated_columns = [
        "Revenue_Growth_Pct",
        "Operating_Profit_Growth_Pct",
        "Net_Profit_Growth_Pct",
        "Operating_Profit_Margin_Pct",
        "Net_Profit_Margin_Pct",
        "Debt_to_Equity_Ratio",
        "Operating_Cash_Flow_to_Net_Profit_Pct"
    ]

    df[calculated_columns] = (
        df[calculated_columns]
        .apply(pd.to_numeric, errors="coerce")
        .round(2)
    )

    # Display all seven KPIs
    print("\nQUARTERLY FINANCIAL KPI RESULTS")
    print("=" * 100)

    display_columns = [
        "Quarters",
        "Revenue_Cr",
        "Revenue_Growth_Pct",
        "Operating_Profit_Cr",
        "Operating_Profit_Growth_Pct",
        "Operating_Profit_Margin_Pct",
        "Net_Profit_Cr",
        "Net_Profit_Growth_Pct",
        "Net_Profit_Margin_Pct",
        "Debt_to_Equity_Ratio",
        "Operating_Cash_Flow_to_Net_Profit_Pct"
    ]

    print(
        df[display_columns].to_string(
            index=False,
            float_format=lambda value: f"{value:.2f}"
        )
    )

    print("\nQuarterly financial analysis completed!")
    return df


def analyze_cash_flow(cash_flow_df, quarterly_df):

    print("\nSTARTING CASH FLOW ANALYSIS")

    # Create copies to protect the original data
    cash_df = cash_flow_df.copy()
    quarterly = quarterly_df.copy()

    # Merge revenue and net profit into cash flow data
    df = cash_df.merge(
        quarterly[
            [
                "Financial_Year",
                "Quarters",
                "Revenue_Cr",
                "Net_Profit_Cr"
            ]
        ],
        on=["Financial_Year", "Quarters"],
        how="left",
        validate="one_to_one"
    )

    # Sort quarterly records
    df = df.sort_values(
        by=["Financial_Year", "Quarters"]
    ).reset_index(drop=True)

    # 1. Operating Cash Flow Growth
    df["OCF_Growth_Pct"] = (
        df["Operating_Cash_Flow_Cr"].pct_change(fill_method=None) * 100
    )

    # 2. Free Cash Flow Growth
    df["FCF_Growth_Pct"] = (
        df["Free_Cash_Flow_Cr"].pct_change(fill_method=None) * 100
    )

    # 3. Free Cash Flow Margin
    df["FCF_Margin_Pct"] = (
        df["Free_Cash_Flow_Cr"] / df["Revenue_Cr"] * 100
    )

    # 4. Capital Expenditure to Operating Cash Flow
    df["CapEx_to_OCF_Pct"] = (
        df["Capital_Expenditure_Cr"] /
        df["Operating_Cash_Flow_Cr"] * 100
    )

    # 5. Operating Cash Flow to Net Profit
    df["OCF_to_Net_Profit_Pct"] = (
        df["Operating_Cash_Flow_Cr"] /
        df["Net_Profit_Cr"] * 100
    )

    # Round calculated values
    calculated_columns = [
        "OCF_Growth_Pct",
        "FCF_Growth_Pct",
        "FCF_Margin_Pct",
        "CapEx_to_OCF_Pct",
        "OCF_to_Net_Profit_Pct"
    ]

    df[calculated_columns] = (
        df[calculated_columns]
        .apply(pd.to_numeric, errors="coerce")
        .round(2)
    )

    # Display results
    display_columns = [
        "Quarters",
        "Operating_Cash_Flow_Cr",
        "OCF_Growth_Pct",
        "Capital_Expenditure_Cr",
        "Free_Cash_Flow_Cr",
        "FCF_Growth_Pct",
        "FCF_Margin_Pct",
        "CapEx_to_OCF_Pct",
        "OCF_to_Net_Profit_Pct"
    ]

    print("\nCASH FLOW ANALYSIS RESULTS")
    print("=" * 110)
    print(
        df[display_columns].to_string(
            index=False,
            float_format=lambda value: f"{value:.2f}"
        )
    )

    print("\nCash flow analysis completed!")
    return df


def analyze_balance_sheet(balance_sheet_df):
    print("\nSTARTING BALANCE SHEET ANALYSIS")

    # Create a copy of the original DataFrame
    df = balance_sheet_df.copy()

    # Sort quarterly records
    df = df.sort_values(
        by=["Financial_Year", "Quarters"]
    ).reset_index(drop=True)

    # 1. Total Assets Growth
    df["Assets_Growth_Pct"] = (
        df["Total_Assets_Cr"].pct_change(fill_method=None) * 100
    )

    # 2. Total Liabilities Growth
    df["Liabilities_Growth_Pct"] = (
        df["Total_Liabilities_Cr"].pct_change(fill_method=None) * 100
    )

    # 3. Total Equity Growth
    df["Equity_Growth_Pct"] = (
        df["Total_Equity_Cr"].pct_change(fill_method=None) * 100
    )

    # 4. Debt-to-Equity Ratio
    df["Debt_to_Equity_Ratio"] = (
        df["Total_Debt_Cr"] / df["Total_Equity_Cr"]
    )

    # 5. Debt-to-Assets Ratio
    df["Debt_to_Assets_Pct"] = (
        df["Total_Debt_Cr"] / df["Total_Assets_Cr"] * 100
    )

    # 6. Equity Ratio
    df["Equity_Ratio_Pct"] = (
        df["Total_Equity_Cr"] / df["Total_Assets_Cr"] * 100
    )

    # 7. Liabilities-to-Assets Ratio
    df["Liabilities_to_Assets_Pct"] = (
        df["Total_Liabilities_Cr"] / df["Total_Assets_Cr"] * 100
    )

    # Round calculated values
    calculated_columns = [
        "Assets_Growth_Pct",
        "Liabilities_Growth_Pct",
        "Equity_Growth_Pct",
        "Debt_to_Equity_Ratio",
        "Debt_to_Assets_Pct",
        "Equity_Ratio_Pct",
        "Liabilities_to_Assets_Pct"
    ]

    df[calculated_columns] = (
        df[calculated_columns]
        .apply(pd.to_numeric, errors="coerce")
        .round(2)
    )

    # Select columns for display
    display_columns = [
        "Quarters",
        "Total_Assets_Cr",
        "Assets_Growth_Pct",
        "Total_Liabilities_Cr",
        "Liabilities_Growth_Pct",
        "Total_Equity_Cr",
        "Equity_Growth_Pct",
        "Total_Debt_Cr",
        "Debt_to_Equity_Ratio",
        "Debt_to_Assets_Pct",
        "Equity_Ratio_Pct",
        "Liabilities_to_Assets_Pct"
    ]

    print("\nBALANCE SHEET ANALYSIS RESULTS")
    print("=" * 120)

    print(
        df[display_columns].to_string(
            index=False,
            float_format=lambda value: f"{value:.2f}"
        )
    )
    print("\nBalance sheet analysis completed!")
    return df


def analyze_peer_comparison(peer_df):

    print("\nSTARTING PEER COMPARISON ANALYSIS")

    # Create a copy of the original DataFrame
    df = peer_df.copy()

    # Convert financial columns into numeric data types
    numeric_columns = [
        "Revenue_Cr_FY2026",
        "Net_Profit_Cr_FY2026",
        "EPS_Rs",
        "Debt_Cr",
        "PE_Ratio",
        "ROE_Pct"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Calculate Net Profit Margin
    df["Net_Profit_Margin_Pct"] = (
        df["Net_Profit_Cr_FY2026"] /
        df["Revenue_Cr_FY2026"] * 100
    )

    # Calculate Debt-to-Revenue Ratio
    df["Debt_to_Revenue_Pct"] = (
        df["Debt_Cr"] /
        df["Revenue_Cr_FY2026"] * 100
    )

    # Round calculated columns
    calculated_columns = [
        "Net_Profit_Margin_Pct",
        "Debt_to_Revenue_Pct"
    ]

    df[calculated_columns] = (
        df[calculated_columns].round(2)
    )

    # Display comparison results
    display_columns = [
        "Company",
        "Revenue_Cr_FY2026",
        "Net_Profit_Cr_FY2026",
        "Net_Profit_Margin_Pct",
        "EPS_Rs",
        "Debt_Cr",
        "Debt_to_Revenue_Pct",
        "PE_Ratio",
        "ROE_Pct"
    ]

    print("\nPEER COMPARISON RESULTS")
    print("=" * 120)

    print(
        df[display_columns].to_string(
            index=False,
            float_format=lambda value: f"{value:.2f}"
        )
    )

    # Identify the leading company for selected metrics
    print("\nPEER COMPARISON HIGHLIGHTS")
    print("=" * 60)

    highest_revenue = df.loc[
        df["Revenue_Cr_FY2026"].idxmax(), "Company"
    ]

    highest_profit = df.loc[
        df["Net_Profit_Cr_FY2026"].idxmax(), "Company"
    ]

    highest_eps = df.loc[
        df["EPS_Rs"].idxmax(), "Company"
    ]

    lowest_debt = df.loc[
        df["Debt_Cr"].idxmin(), "Company"
    ]

    highest_roe = df.loc[
        df["ROE_Pct"].idxmax(), "Company"
    ]

    highest_pe = df.loc[
        df["PE_Ratio"].idxmax(), "Company"
    ]

    print(f"Highest Revenue: {highest_revenue}")
    print(f"Highest Net Profit: {highest_profit}")
    print(f"Highest EPS: {highest_eps}")
    print(f"Lowest Debt: {lowest_debt}")
    print(f"Highest ROE: {highest_roe}")
    print(f"Highest P/E Ratio: {highest_pe}")
    print("\nPeer comparison analysis completed!")
    return df


def export_financial_analysis_reports(
    quarterly_results,
    cash_flow_results,
    balance_sheet_results,
    peer_results
):

    print("\nSTARTING FINANCIAL REPORT EXPORT")

    # Define report output directory
    output_directory = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "outputs",
        "reports"
    )

    # Create directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Define reports
    reports = {
        "Quarterly_Financial_KPIs.csv": quarterly_results,
        "Cash_Flow_Analysis.csv": cash_flow_results,
        "Balance_Sheet_Analysis.csv": balance_sheet_results,
        "Peer_Comparison_Analysis.csv": peer_results
    }

    # Export each DataFrame
    for file_name, dataframe in reports.items():

        file_path = os.path.join(
            output_directory,
            file_name
        )

        dataframe.to_csv(
            file_path,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"Successfully exported: {file_name}")

    print("\nAll financial analysis reports exported!")


if __name__ == "__main__":

    print("EQUITY RESEARCH - FINANCIAL ANALYSIS")

    financial_data = load_tables()

    if financial_data:

        quarterly_df = financial_data["Quarterly_Financials"]
        kpi_results = calculate_quarterly_kpis(quarterly_df)

        cash_flow_df = financial_data["Cash_Flow"]
        cash_flow_results = analyze_cash_flow(
            cash_flow_df,
            quarterly_df
        )

        balance_sheet_df = financial_data["Balance_Sheet"]
        balance_sheet_results = analyze_balance_sheet(
            balance_sheet_df
        )

        peer_df = financial_data["Peer_Comparison"]
        peer_results = analyze_peer_comparison(peer_df)

        # Export all financial analysis reports
        export_financial_analysis_reports(
            kpi_results,
            cash_flow_results,
            balance_sheet_results,
            peer_results
        )
