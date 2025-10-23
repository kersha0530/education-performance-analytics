"""
data_cleaning.py
Cleans and preprocesses the Student Performance dataset.
"""

import pandas as pd
import numpy as np
import os

# Paths
RAW_PATH = r"C:\Projects\education-performance-analytics\data\student_performance_socioeconomic.csv"
CLEAN_PATH = r"C:\Projects\education-performance-analytics\data\student_performance_socioeconomic_cleaned.csv"

def clean_student_data(input_path=RAW_PATH, output_path=CLEAN_PATH):
    df = pd.read_csv(input_path)

    # Drop missing IDs
    df = df.dropna(subset=["Student_ID"])

    # Fill missing semester grades with mean
    df["Semester_Average_Grade"].fillna(df["Semester_Average_Grade"].mean(), inplace=True)

    # Drop duplicates
    df = df.drop_duplicates()

    # Derived metrics
    df["Performance_Efficiency_Ratio"] = df["Semester_Approved_Units"] / df["Semester_Enrolled_Units"]
    df["Grade_Consistency_Index"] = df["Semester_Average_Grade"] / df["Grade_Average"]

    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned dataset saved to: {output_path}")

if __name__ == "__main__":
    clean_student_data()
