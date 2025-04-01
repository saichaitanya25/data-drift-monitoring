# Data Drift Monitoring System

A lightweight, production-style system for monitoring data drift in machine learning pipelines using the Kolmogorov–Smirnov (KS) test.

## 🚀 Features
- Compares new data batches against reference data.
- Detects distribution drift on numeric features.
- Logs alerts and optionally sends email notifications.
- Can be scheduled using Apache Airflow.

## 📂 Folder Structure
```
data-drift-monitoring/
├── data/
│   ├── reference.csv
│   └── new_data.csv
├── drift_monitor.py
├── generate_data.py
├── airflow_dag.py
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions
1. Clone the repository
2. Install dependencies
3. Run `generate_data.py` to create sample CSVs
4. Execute `drift_monitor.py` to detect drift

## 📧 Email Notifications
Edit SMTP settings in `drift_monitor.py` to enable alerts.

## ⏰ Airflow
Place `airflow_dag.py` in your Airflow DAG folder and start the scheduler.
