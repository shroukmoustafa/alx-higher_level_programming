#!/usr/bin/python3
import os
import pandas as pd
import xlsxwriter as xw
from duplicate_comparison import check_duplicates

sourcefile = input ("enter the source file path: ")
comparedfile = input ("enter the compared file path: ")
if not os.path.exists(sourcefile) or not os.path.exists(comparedfile):
    print("Error: One or both files do not exist. Please check the paths.")
    exit()

try:
    content1 = pd.read_excel(sourcefile, skiprows=0)
    content2 = pd.read_excel(comparedfile, skiprows=0)
# remove rows where all values are None (empty rows)
    content1 = content1.dropna(how='all')
    content2 = content2.dropna(how='all')
    content1.columns = content1.columns.str.strip().str.lower()
    content2.columns = content2.columns.str.strip().str.lower()

    required_cols = {'date', 'amount', 'currency'}
    if not required_cols.issubset(content1.columns) or not required_cols.issubset(content2.columns):
        print("Error: Required columns (date, amount, currency) are missing.")
        exit()
    content1['date'] = pd.to_datetime(content1['date'], errors='coerce')
    content2['date'] = pd.to_datetime(content2['date'], errors='coerce')
    content1['amount'] = pd.to_numeric(content1['amount'], errors='coerce')
    content2['amount'] = pd.to_numeric(content2['amount'], errors='coerce')
    content1['currency'] = content1['currency'].astype(str).str.strip().str.upper()
    content2['currency'] = content2['currency'].astype(str).str.strip().str.upper()
#keep only the relevant columns for comparison
    df1 = content1[['date', 'amount', 'currency']]
    df2 = content2[['date', 'amount', 'currency']]
    dup_result, dup_message = check_duplicates(df1, df2)
    diff = df2.merge(
    df1,
    on=['date', 'amount', 'currency'],
    how='left',
    indicator=True)
    comparison = diff[diff['_merge'] == 'left_only'].drop(columns=['_merge'])
    
    output_file = 'comparison_result.xlsx'
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    # Missing rows sheet
        comparison.to_excel(writer, sheet_name='missing_rows', index=False)

    # Duplicate check
        if dup_result is None:
            # No differences → simple message
            pd.DataFrame({"message": [dup_message]}).to_excel(
                writer, sheet_name='duplicates_check', index=False
            )
        else:
            dup_result["differences"].to_excel(writer, sheet_name='dup_count_diff', index=False)
            dup_result["source_duplicates"].to_excel(writer, sheet_name='source_duplicates', index=False)
            dup_result["compared_duplicates"].to_excel(writer, sheet_name='compared_duplicates', index=False)

    print(f"Comparison completed. Results saved to {output_file}")
    print(dup_message)
except Exception as e:
    print(f"An error occurred: {e}")