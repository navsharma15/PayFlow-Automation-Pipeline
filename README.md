#                                    🚀 PhonePe Transaction Automation & Analytics Pipeline

## 📌 Project Overview

The **PhonePe Transaction Automation & Analytics Pipeline** is an end-to-end ETL automation project built using **Python, SQL Server, and Power BI**.

The project automates the complete data pipeline by generating daily transaction data, appending it to the master dataset, cleaning and validating the data, loading it into SQL Server, and visualizing business insights through Power BI dashboards.

To eliminate manual intervention, the entire workflow is scheduled using **Windows Task Scheduler**, while a logging system records every execution step for monitoring and debugging.

---

# 🎯 Project Objectives

* Automate the complete ETL pipeline.
* Eliminate manual data processing.
* Store clean data in SQL Server.
* Build interactive Power BI dashboards.
* Monitor automation using logging.
* Schedule the pipeline for daily execution.

---

# ✨ Features

* ✅ Automated Daily Transaction Generation
* ✅ Data Appending
* ✅ Data Cleaning & Validation
* ✅ SQL Server Integration
* ✅ Interactive Power BI Dashboard
* ✅ Windows Task Scheduler Automation
* ✅ Logging & Monitoring
* ✅ Exception Handling

---

# 🛠️ Tech Stack

| Technology             | Purpose                    |
| ---------------------- | -------------------------- |
| Python                 | ETL Automation             |
| Pandas                 | Data Cleaning & Processing |
| SQL Server             | Database Storage           |
| pyodbc                 | SQL Server Connection      |
| Power BI               | Dashboard & Visualization  |
| Windows Task Scheduler | Daily Automation           |
| Logging                | Execution Monitoring       |
| Git & GitHub           | Version Control            |

---

# 🔄 Project Workflow

```text
Task Scheduler
        │
        ▼
run_automation.bat
        │
        ▼
main.py
        │
        ▼
Generate Daily Data
        │
        ▼
Append Data
        │
        ▼
Clean & Validate Data
        │
        ▼
Load into SQL Server
        │
        ▼
Power BI Dashboard
        │
        ▼
automation.log
```

---

# 📂 Project Structure

```text
PhonePe-Automation-Project
│
├── automation/
│   ├── main.py
│   ├── run_automation.bat
│   ├── 02_generate_daily_data.py
│   ├── 03_append_data.py
│   ├── 04_clean_data.py
│   └── 05_load_sql.py
│
├── dashboard/
│   └── PhonePe_Automation.pbix
│
├── data/
│
├── logging/
│   └── automation.log
│
├── notebooks/
│
├── screenshots/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📋 Prerequisites

Before running the project, ensure the following software is installed:

* Python 3.x
* SQL Server
* SQL Server Management Studio (SSMS)
* Power BI Desktop

### Required Python Libraries

* pandas
* pyodbc
* openpyxl

---

# ▶️ Running the Project

### Run the complete ETL pipeline

```bash
python main.py
```

### Or execute using Batch File

```text
run_automation.bat
```

### Daily Automation

Configure **Windows Task Scheduler** to execute `run_automation.bat` at your preferred time for fully automated daily execution.

---

# 📊 Dashboard

The Power BI dashboard provides insights including:

* Total Transactions
* Total Revenue
* Successful vs Failed Transactions
* Daily Transaction Trend
* Service-wise Revenue
* Top Users
* Payment Status Analysis

*(Add screenshots inside the `screenshots` folder and display them here after uploading.)*

---

# 📝 Logging

Execution logs are automatically stored in:

```text
logging/automation.log
```

The log file records:

* Automation Started
* Data Generation Completed
* Data Append Completed
* Data Cleaning Completed
* SQL Loading Completed
* Automation Completed Successfully
* Error Messages (if any)

---

# 💡 Key Skills Demonstrated

* ETL Pipeline Development
* Python Automation
* Data Cleaning & Transformation
* SQL Server Integration
* Power BI Dashboard Development
* Windows Task Scheduler
* Logging & Monitoring
* Version Control using Git & GitHub

---

# 🚀 Future Enhancements

* Email Notifications after Automation
* Machine Learning-based Fraud Detection
* Cloud Database Integration
* REST API Data Integration
* Power BI Service Auto Refresh
* Docker Deployment

---

# 👨‍💻 Author

**Nav Sharma**

Computer Science Engineering Student

**Skills:** Python, SQL, Power BI, Pandas, Data Analytics, Automation

---

## ⭐ If you found this project useful, consider giving it a Star!
