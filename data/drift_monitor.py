# Data Drift Monitoring System

"""
Project: Data Drift Monitoring System
Description: Detects data drift in a dataset over time using statistical techniques.
            Runs as a scheduled task via Airflow and alerts via email.
"""

import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
import smtplib
from email.mime.text import MIMEText

def load_data():
    ref_df = pd.read_csv('data/reference.csv')
    new_df = pd.read_csv('data/new_data.csv')
    return ref_df, new_df

def detect_drift(ref_df, new_df, threshold=0.05):
    drift_report = {}
    for col in ref_df.select_dtypes(include=np.number).columns:
        ks_stat, p_val = ks_2samp(ref_df[col].dropna(), new_df[col].dropna())
        drift_report[col] = {
            'ks_stat': ks_stat,
            'p_value': p_val,
            'drift_detected': p_val < threshold
        }
    return drift_report

def report_drift(drift_report):
    msg_lines = []
    for feature, metrics in drift_report.items():
        if metrics['drift_detected']:
            line = f"Drift detected in {feature}: KS={metrics['ks_stat']:.3f}, p={metrics['p_value']:.4f}"
        else:
            line = f"No drift in {feature}: KS={metrics['ks_stat']:.3f}, p={metrics['p_value']:.4f}"
        msg_lines.append(line)
    message = "\n".join(msg_lines)
    print(message)
    return message

def send_email_alert(message):
    sender = 'youremail@example.com'
    recipient = 'stakeholder@example.com'
    msg = MIMEText(message)
    msg['Subject'] = 'Data Drift Alert'
    msg['From'] = sender
    msg['To'] = recipient
    try:
        with smtpllib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, 'yourpassword')
            server.sendmail(sender, [recipient], msg.as_string())
    except Exception as e:
        print("Failed to send email:", e)

def run_pipeline():
    ref_df, new_df = load_data()
    drift_report = detect_drift(ref_df, new_df)
    message = report_drift(drift_report)
    send_email_alert(message)

if __name__ == '__main__':
    run_pipeline()
