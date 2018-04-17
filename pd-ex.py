import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

s = pd.Series([1,3,5,np.nan,6,8]) # create a list of values with Series
# print(s)

dates = pd.date_range('20130101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # create a data frame of 6*4, dates as row, abcd as columns
# print(df)

# df2 = pd.DataFrame({'A':1.,
#                     'B':pd.Timestamp('20130102'),
#                     'C':pd.Series(1,index=list(range(4)),dtype='float32'),
#                     'D':np.array([3]*4,dtype='int32'),
#                     'E':pd.Categorical(["test","train","test","train"]),
#                     'F':'foo'}) # create a dataframe by passing a dict of objects that can be converted to series-like
# print(df2)
# print(df2.dtypes)