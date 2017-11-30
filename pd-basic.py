import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# s = pd.Series([1,3,5,np.nan,6,8])
# print(s)

dates = pd.date_range('20130101', periods=6)
# # print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # create a 6*4 dataframe, column name ABCD, use dates as index
# print(df)
# print(df.head) # displays the top 5 rows
# print(df.tail(3)) # displays the bottom 3 rows
# print(df.index) # display the index, columns, and the underlying numpy data
# print(df.columns) # display the columns
# print(df.values) # displays the values
# print(df.describe()) # show a quick statistics summary of the data

# print(df.T) # transpose

# print(df.sort_index(axis=1, ascending=False)) # sort decending by axis

# print(df.sort_values(by='B')) # sort by the values of B

# print(df['A']) # select column A

# print(df[0:3]) # select row 0-3

# print(df['20130102':'20130104']) # select row 20130102 to 20130104

# print(df.loc[dates[0]]) # select the first row by label

# print(df.loc[:,['A','B']]) # select the a and b columns

# print(df.loc['20130102':'20130104',['A','B']]) # select a, b columns between 20130102 and 20130104

# print(df.loc[dates[0],'A']) # locate a value at row dates[0] and column A

# print(df.at[dates[0],'A']) # faster access to a value

# print(df.iloc[3]) # select the 4th row

# print(df.iloc[3:5,0:2]) # select values between row 3 to 4, columns 0 to 1

# print(df.iloc[[1,2,4],[0,2]]) # select row 1,2,4 and column 0, 2

# print(df.iloc[1:3,:]) # select row 1 and 2

# print(df.iloc[:,1:3]) # select column 1 and 2

# print(df.iloc[1,1]) # get a value explicitly

# print(df[df.A > 0]) # select values where column A >0


# df2 = df.copy()
# df2['E'] = ['one', 'one','two','three','four','three']
# print(df2) # copy df and add a E column
# print(df2[df2['E'].isin['two','four']]) # filter data where the E column value is two or four

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6)) # create a series with date as index
# print(s1)
# print(df)

df['F'] = s1
df.at[dates[0],'A'] = 0 # set value by label: set date[0] column A as 0
df.iat[0,1] = 0 # set value by position
df.loc[:,'D'] = np.array([5] * len(df)) # set by aligning with a numpy array
print(df)

# df2 = df.copy()
# df2[df2 > 0] = -df2 # where a value >0, make it -
# print(df2)

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1 # set E column top 2 rows to 1
print(df1)

# print(df1.dropna(how='any')) # print the rows without NA
# print(df1.fillna(value=5)) # fill the NA valus with 5
print(pd.isna(df1)) # display whether value is nan

# df2 = pd.DataFrame({'A':1.,
#                     'B':pd.Timestamp('20130102'),
#                     'C':np.array([3] * 4,dtype='int32'),
#                     'E':pd.Categorical(["test","train","test","train"]),
#                     'F':'foo'})
# print(df2)
# print(df2.dtypes)
