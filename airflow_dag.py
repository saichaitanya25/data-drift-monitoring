from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from drift_monitor import run_pipeline

def run():
    run_pipeline()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'data_drift_monitoring',
    default_args=default_args,
    description='Monitor data drift daily',
    schedule_interval='@daily',
)

detect_drift = PythonOperator(
    task_id='check_data_drift',
    python_callable=run,
    dag=dag,
)
