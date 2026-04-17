#!/usr/bin/python3
import os
import pandas as pd
import xlsxwriter as xw

sourcefile = input ("enter the source file path: ")
comparedfile = input ("enter the compared file path: ")
if not os.path.exists(sourcefile) or not os.path.exists(comparedfile):
    print("Error: One or both files do not exist. Please check the paths.")
    exit()

try:
    content1 = pd.read_excel(sourcefile, skiprows=0)
    content2 = pd.read_excel(comparedfile, skiprows=0)
    content1 = content1.dropna(how='all')
    content2 = content2.dropna(how='all')
    required_cols = {'date', 'amount'}
    if not required_cols.issubset(content1.columns) or not required_cols.issubset(content2.columns):
        print("Error: Required columns (date, amount) are missing.")
        exit()
    content1['date'] = pd.to_datetime(content1['date'], errors='coerce')
    content2['date'] = pd.to_datetime(content2['date'], errors='coerce')
    sum1 = content1.groupby('date')['amount'].sum()
    sum2 = content2.groupby('date')['amount'].sum()
    comparison = pd.DataFrame({
        'source_sum': sum1,
        'compared_sum': sum2
    }).fillna(0)
    comparison['difference'] = comparison['source_sum'] - comparison['compared_sum']
    output_file = 'comparison_result.xlsx'
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        comparison.to_excel(writer, sheet_name='Comparison', index=True)
    print(f"Comparison completed. Results saved to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")