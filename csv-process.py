import pandas as pd
data = pd.read_csv("D:\Downloads\Download (23).csv")
count = len(data)
count_us = len(data[data['Country']=='United States'])
rate_us = count_us/count
print("下载总数 %",count)