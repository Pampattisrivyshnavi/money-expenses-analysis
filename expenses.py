import pandas as pd

data = {
    'Category': ['Food', 'Transport', 'Shopping', 'Bills'],
    'Amount': [2500, 800, 1200, 1500]
}

df = pd.DataFrame(data)
print(df)
print("Total:", df['Amount'].sum())
