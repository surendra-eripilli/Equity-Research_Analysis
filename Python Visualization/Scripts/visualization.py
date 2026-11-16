import os
import pandas as pd
import matplotlib.pyplot as plt

from data_exploration import load_tables

def plot_quarterly_revenue_profit(quarterly_df):

    print("\nCREATING QUARTERLY REVENUE AND PROFIT CHART")

    # Create output directory
    output_directory = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "outputs",
        "charts"
    )

    os.makedirs(output_directory, exist_ok=True)

    # Prepare chart data
    quarters = quarterly_df["Quarters"]
    revenue = quarterly_df["Revenue_Cr"]
    net_profit = quarterly_df["Net_Profit_Cr"]

    # Create figure
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Revenue line - left axis
    ax1.plot(
        quarters,
        revenue,
        marker="o",
        linewidth=2,
        label="Revenue (₹ Cr)"
    )
    ax1.set_xlabel("Financial Quarters")
    ax1.set_ylabel("Revenue (₹ Crores)")
    ax1.set_title(
        "Quarterly Revenue and Net Profit Trend - Apex Technologies Ltd."
    )

    ax1.grid(True, linestyle="--", alpha=0.5)

    # Net profit line - right axis
    ax2 = ax1.twinx()

    ax2.plot(
        quarters,
        net_profit,
        marker="s",
        linewidth=2,
        linestyle="--",
        label="Net Profit (₹ Cr)"
    )

    ax2.set_ylabel("Net Profit (₹ Crores)")

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()

    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc="upper left"
    )
    plt.xticks(rotation=15)
    plt.tight_layout()

    # Save chart
    file_path = os.path.join(
        output_directory,
        "Quarterly_Revenue_Profit_Trend.png"
    )
    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    print("Chart successfully saved:", file_path)

def plot_monthly_stock_prices(stock_df):
    print("\nCREATING MONTHLY STOCK PRICE CHART")
    output_directory = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "outputs",
        "charts"
    )
    os.makedirs(output_directory, exist_ok=True)

    # Prepare date column
    stock_df["Dates"] = pd.to_datetime(stock_df["Dates"])
    stock_df = stock_df.sort_values("Dates")

    # Create chart
    plt.figure(figsize=(12, 6))
    plt.plot(
        stock_df["Dates"],
        stock_df["Closes"],
        marker="o",
        linewidth=2,
        label="Monthly Closing Price"
    )

    plt.plot(
        stock_df["Dates"],
        stock_df["MA_3_Month"],
        marker="s",
        linewidth=2,
        linestyle="--",
        label="3-Month Moving Average"
    )

    plt.title("Monthly Stock Price Trend - Apex Technologies Ltd.")
    plt.xlabel("Month")
    plt.ylabel("Stock Price (₹)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart
    file_path = os.path.join(
        output_directory,
        "Monthly_Stock_Price_Trend.png"
    )
    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    print("Chart successfully saved:", file_path)

def plot_peer_revenue_profit(peer_df):
    print("\nCREATING PEER REVENUE AND PROFIT COMPARISON")
    output_directory = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "outputs",
        "charts"
    )
    os.makedirs(output_directory, exist_ok=True)

    # Prepare data
    companies = peer_df["Company"]
    revenue = peer_df["Revenue_Cr_FY2026"]
    net_profit = peer_df["Net_Profit_Cr_FY2026"]

    # Create chart
    fig, ax = plt.subplots(figsize=(12, 6))
    x = range(len(companies))
    width = 0.35
    ax.bar(
        [i - width / 2 for i in x],
        revenue,
        width,
        label="Revenue (₹ Cr)"
    )

    ax.bar(
        [i + width / 2 for i in x],
        net_profit,
        width,
        label="Net Profit (₹ Cr)"
    )

    ax.set_title("Peer Company Revenue and Net Profit Comparison")
    ax.set_xlabel("Companies")
    ax.set_ylabel("Amount (₹ Crores)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(companies, rotation=10)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Save chart
    file_path = os.path.join(
        output_directory,
        "Peer_Revenue_Profit_Comparison.png"
    )
    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    print("Chart successfully saved:", file_path)

def plot_peer_roe_pe(peer_df):

    print("\nCREATING PEER ROE AND P/E COMPARISON")
    output_directory = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "outputs",
        "charts"
    )
    os.makedirs(output_directory, exist_ok=True)

    # Prepare data
    companies = peer_df["Company"]
    roe = peer_df["ROE_Pct"]
    pe_ratio = peer_df["PE_Ratio"]

    # Create chart
    fig, ax1 = plt.subplots(figsize=(12, 6))
    x = range(len(companies))
    width = 0.35

    # ROE bars
    ax1.bar(
        [i - width / 2 for i in x],
        roe,
        width,
        label="ROE (%)"
    )
    ax1.set_xlabel("Companies")
    ax1.set_ylabel("ROE (%)")
    ax1.set_title("Peer Company ROE and P/E Ratio Comparison")

    # P/E line on second axis
    ax2 = ax1.twinx()

    ax2.plot(
        x,
        pe_ratio,
        marker="o",
        linewidth=2,
        linestyle="--",
        label="P/E Ratio"
    )
    ax2.set_ylabel("P/E Ratio (times)")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(companies, rotation=10)

    # Combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc="upper left"
    )
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Save chart
    file_path = os.path.join(
        output_directory,
        "Peer_ROE_PE_Comparison.png"
    )

    plt.savefig(file_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    print("Chart successfully saved:", file_path)

if __name__ == "__main__":
    print("EQUITY RESEARCH - DATA VISUALIZATION")
    financial_data = load_tables()

    if financial_data:

        quarterly_df = financial_data["Quarterly_Financials"]
        plot_quarterly_revenue_profit(quarterly_df)
        stock_df = financial_data["Monthly_Stock_Prices"]
        plot_monthly_stock_prices(stock_df)
        peer_df = financial_data["Peer_Comparison"]
        plot_peer_revenue_profit(peer_df)
        plot_peer_roe_pe(peer_df)