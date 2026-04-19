#!/usr/bin/python3
import os
import pandas as pd
import xlsxwriter as xw

def check_duplicates(df1, df2):
    keys = ['date', 'amount', 'currency']

    # Count occurrences
    count1 = df1.groupby(keys).size().reset_index(name='source_count')
    count2 = df2.groupby(keys).size().reset_index(name='compared_count')

    merged = count1.merge(count2, on=keys, how='outer').fillna(0)

    merged['source_count'] = merged['source_count'].astype(int)
    merged['compared_count'] = merged['compared_count'].astype(int)

    # 🔹 ALL duplicates for counting (even equal ones)
    all_dups = merged[
        (merged['source_count'] > 1) | (merged['compared_count'] > 1)
    ].copy()

    if all_dups.empty:
        return None, "No duplicates found"

    # 🔹 Only mismatched duplicates for listing
    mismatch = all_dups[
        all_dups['source_count'] != all_dups['compared_count']
    ]

    # 🔹 Extract FULL rows (not partial counts)
    source_dups = df1.merge(mismatch[keys], on=keys, how='inner')
    compared_dups = df2.merge(mismatch[keys], on=keys, how='inner')

    return {
        "differences": all_dups,              # ALL duplicate counts
        "source_duplicates": source_dups,    # FULL rows (only mismatched keys)
        "compared_duplicates": compared_dups
    }, "Duplicate analysis completed"