#!/usr/bin/python3
import os
import pandas as pd
import xlsxwriter as xw

def check_duplicates(df1, df2):
    keys = ['date', 'amount', 'currency']
    # Count occurrences in each file
    count1 = df1.groupby(keys).size().reset_index(name='source_count')
    count2 = df2.groupby(keys).size().reset_index(name='compared_count')
    merged = count1.merge(count2, on=keys, how='outer').fillna(0)
    merged['source_count'] = merged['source_count'].astype(int)
    merged['compared_count'] = merged['compared_count'].astype(int)
    # Find mismatches
    diff_counts = merged[merged['source_count'] != merged['compared_count']]

    if diff_counts.empty:
        return None, "No duplicate differences found"

    else:
        # Extract actual duplicate rows from both files
        dup1 = df1[df1.duplicated(keys, keep=False)]
        dup2 = df2[df2.duplicated(keys, keep=False)]
    return {
            "differences": diff_counts,
            "source_duplicates": dup1,
            "compared_duplicates": dup2
        }, " Duplicate mismatch found - please check"    
