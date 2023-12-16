import pandas as pd
import dask.dataframe as dd
import os
temp = {}
for file_name in os.listdir("./data"):
    csv_path = os.path.join("data",file_name)
    ticker = file_name[:file_name.index("-")]
    if ticker not in temp:
        temp[ticker]=[]
    df = pd.read_csv(csv_path)
    temp[ticker].append(df)

for ticker,value in temp.items():
    pd.concat(value).to_csv(os.path.join("data_csv",str(ticker)+".csv"))
