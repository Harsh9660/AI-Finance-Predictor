import pandas as pd
import numpy as np 
from Data import Budget.csv, personal_transactions.csv

df = pd.read_csv(Budget.csv)
print(df.head())