import os
import pandas as pd
from database_connection import create_connection

def load_tables():
    connection = create_connection()
    if connection is None:
        print("Database connection failed.")
        return

    tables = [
        "Company_Overview",
        "Quarterly_Financials",
        "Income_Statement",
        "Balance_Sheet",
        "Cash_Flow",
        "Monthly_Stock_Prices",
        "Peer_Comparison"
    ]

    dataframes = {}

    try:
        cursor = connection.cursor(dictionary=True)

        for table in tables:

            query = f"SELECT * FROM `{table}`"
            cursor.execute(query)

            records = cursor.fetchall()

            df = pd.DataFrame(records)

            dataframes[table] = df

            print("\n" + "=" * 50)
            print("TABLE:", table)
            print("Number of Rows:", df.shape[0])
            print("Number of Columns:", df.shape[1])

            print("\nFirst 5 Records:")
            print(df.head())

        cursor.close()

    except Exception as e:
        print("Data Loading Error:", e)

    finally:
        connection.close()
        print("\nDatabase connection closed.")

    return dataframes

def analyze_data_quality(dataframes):

    for table_name, df in dataframes.items():

        print("\n" + "=" * 60)
        print("DATA QUALITY REPORT:", table_name)
        print("=" * 60)

        # 1. Dataset dimensions
        print("\n1. Dataset Dimensions")
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])
        # 2. Column data types
        print("\n2. Column Data Types")
        print(df.dtypes)
        # 3. Missing values
        print("\n3. Missing Values")
        missing_values = df.isnull().sum()
        print(missing_values)
        print("Total Missing Values:", missing_values.sum())
        # 4. Duplicate records
        print("\n4. Duplicate Records")
        duplicate_count = df.duplicated().sum()
        print("Total Duplicate Rows:", duplicate_count)
        # 5. Overall status
        print("\n5. Data Quality Summary")

        if missing_values.sum() == 0 and duplicate_count == 0:
            print("No missing values or duplicate rows found.")
        else:
            print("Data quality issues detected. Further inspection required.")


def prepare_data_types(dataframes):
    print("\nSTARTING DATA TYPE CONVERSION")
    for table_name, df in dataframes.items():

        # Convert date column into datetime format
        if table_name == "Monthly_Stock_Prices":
            df["Dates"] = pd.to_datetime(df["Dates"])

        # Check object columns and convert numeric values
        for column in df.columns:

            if column == "Dates":
                continue

            if df[column].dtype == "object":

                converted = pd.to_numeric(
                    df[column],
                    errors="coerce"
                )
                # Convert only when all existing non-null
                # values are successfully converted
                if converted.notna().sum() == df[column].notna().sum():
                    df[column] = converted

        print("\n" + "=" * 50)
        print("TABLE:", table_name)
        print("\nUpdated Data Types:")
        print(df.dtypes)
    print("\nData type conversion completed!")
    return dataframes

def generate_statistical_summary(dataframes):
    print("\nSTARTING STATISTICAL SUMMARY")
    for table_name, df in dataframes.items():

        print("\n" + "=" * 60)
        print("STATISTICAL SUMMARY:", table_name)
        print("=" * 60)

        # Select only numerical columns
        numeric_df = df.select_dtypes(include="number")
        if numeric_df.empty:
            print("No numerical columns available.")
            continue

        # Generate descriptive statistics
        summary = numeric_df.describe()
        print("\nDescriptive Statistics:")
        print(summary)
    print("\nStatistical summary completed!")

def export_statistical_reports(dataframes):
    print("\nSTARTING STATISTICAL REPORT EXPORT")
    # Create the reports folder if it does not exist
    reports_folder = os.path.join("outputs", "reports")
    os.makedirs(reports_folder, exist_ok=True)
    for table_name, df in dataframes.items():
        # Select only numerical columns
        numeric_df = df.select_dtypes(include="number")
        # Skip tables without numerical columns
        if numeric_df.empty:
            print(f"\nSkipped: {table_name} - No numerical columns.")
            continue
        # Generate statistical summary
        summary = numeric_df.describe().round(2)
        # Create CSV file name
        file_name = f"{table_name}_statistical_summary.csv"
        # Create complete file path
        file_path = os.path.join(reports_folder, file_name)
        # Export summary to CSV
        summary.to_csv(file_path, index_label="Statistic")
        print(f"Successfully saved: {file_path}")
    print("\nAll statistical reports exported successfully!")

if __name__ == "__main__":

    print("EQUITY RESEARCH - DATA EXPLORATION")
    financial_data = load_tables()
    if financial_data:
        financial_data = prepare_data_types(financial_data)
        print("\n\nSTARTING DATA QUALITY ANALYSIS")
        analyze_data_quality(financial_data)
        print("\n\nSTARTING STATISTICAL ANALYSIS")
        generate_statistical_summary(financial_data)
        print("\n\nEXPORTING STATISTICAL REPORTS")
        export_statistical_reports(financial_data)
        print("\nData quality analysis completed!")