"""Demo module."""

import pandas as pd

file_name = '/Users/macharya/Downloads/CTGAN/2000Q1_filtered.csv'
#file_name = '/Users/macharya/Downloads/CTGAN/sample_processed.csv'

def load_demo():

    return pd.read_csv(file_name)
