# Python Visualization – Apex Equity Research Analysis

## 1. Overview

This module performs data exploration, financial analysis, and data visualization for the Apex Technologies Ltd. Equity Research Analysis project.

It uses Python to retrieve synthetic financial data from MySQL, perform data quality checks, calculate financial metrics, and generate charts and analytical reports.

**Note:** Apex Technologies Ltd. is a fictional company. All financial figures, stock prices, and competitor information are synthetic and intended for educational and portfolio purposes only.

## 2. Technologies and Libraries

| Technology | Purpose |
|---|---|
| Python | Data analysis and automation |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Financial data visualization |
| MySQL Connector | MySQL database connectivity |
| python-dotenv | Environment variable management |
| MySQL | Financial data storage |

## 3. Project Structure

```text
Python Visualization/
│
├── Scripts/
│   ├── database_connection.py
│   ├── data_exploration.py
│   ├── financial_analysis.py
│   └── visualization.py
│
├── Outputs/
│   ├── Charts/
│   └── Reports/
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

**Note:** The `.venv/` virtual environment and `.env` credentials file are excluded from version control. The `.env.example` file provides a template for database configuration.

## 4. Environment Setup

### Step 1: Install Python

Install Python on your system if it is not already installed.

Verify the installation:

```powershell
python --version
```

### Step 2: Navigate to the Project Folder

Open PowerShell in the Python Visualization directory:

```powershell
cd "Python Visualization"
```

### Step 3: Create a Virtual Environment

```powershell
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 5: Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

## 5. MySQL Database Configuration

This project connects to the MySQL database:

```text
Database Name: apex_equity_research
```

### Step 1: Configure Environment Variables

Create a `.env` file in the Python Visualization root directory using `.env.example` as a template.

Add your own MySQL credentials:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=apex_equity_research
DB_PORT=3306
```

Replace `your_mysql_password` with your actual MySQL password.

### Step 2: Test the Database Connection

Run:

```powershell
python Scripts/database_connection.py
```

A successful connection displays a confirmation message:

```text
Successfully connected to MySQL!
Database: apex_equity_research
MySQL connection closed.
```

## 6. Running Python Scripts

Execute the scripts from the Python Visualization directory with the virtual environment activated.

### 6.1 Database Connection

```powershell
python Scripts/database_connection.py
```

Establishes and tests the connection to MySQL.

### 6.2 Data Exploration

```powershell
python Scripts/data_exploration.py
```

Performs data exploration and quality checks, including:

- Dataset dimensions and structure.
- Column information and data types.
- Missing value checks.
- Duplicate record checks.
- Statistical summaries.

### 6.3 Financial Analysis

```powershell
python Scripts/financial_analysis.py
```

Performs financial calculations and analysis using the project datasets.

### 6.4 Data Visualization

```powershell
python Scripts/visualization.py
```

Generates financial and stock market visualizations.

## 7. Generated Outputs

The Python analysis generates output files in the following directories:

### Charts

Location:

```text
Outputs/Charts/
```

Contains generated PNG charts for financial performance and stock market analysis.

### Reports

Location:

```text
Outputs/Reports/
```

Contains generated CSV reports and statistical summaries.

## 8. Database Tables

The Python module works with seven MySQL tables:

| Table | Records |
|---|---:|
| Company_Overview | 9 |
| Quarterly_Financials | 4 |
| Income_Statement | 4 |
| Balance_Sheet | 4 |
| Cash_Flow | 4 |
| Monthly_Stock_Prices | 12 |
| Peer_Comparison | 3 |
| **Total** | **40** |

Database: `apex_equity_research`

## 9. Troubleshooting

| Issue | Suggested Solution |
|---|---|
| Python command not recognized | Verify Python installation and PATH configuration. |
| Virtual environment activation blocked | Apply the PowerShell execution policy command provided above. |
| Module not found | Activate `.venv` and install dependencies using `requirements.txt`. |
| MySQL connection error | Verify MySQL server status and `.env` credentials. |
| Database not found | Confirm that `apex_equity_research` exists in MySQL. |
| Missing environment variables | Ensure `.env` is located in the Python Visualization root directory. |
| Output files not generated | Check the script execution output and required database tables. |

## 10. Skills Demonstrated

- Python programming
- Data exploration and data quality analysis
- Pandas and NumPy
- MySQL database connectivity
- Financial data analysis
- Data visualization using Matplotlib
- Environment and dependency management
- Analytical report generation

## 11. Data Disclaimer

This project uses fictional company information and synthetic educational datasets. It does not use live market data or actual financial statements and should not be interpreted as investment advice.