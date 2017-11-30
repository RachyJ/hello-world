import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

dates = pd.date_range('20130101', periods=6)
# # print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # create a 6*4 dataframe, column name ABCD, use dates as index

# print(df.mean()) # calculate the mean of column 0
# print(df.mean(1))

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
print(s) # move the series down by 2 places 
print(df.sub(s, axis='index'))
