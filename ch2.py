import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'dataset/ch2.txt'
records = [json.loads(line) for line in open(path)]

frame = DataFrame(records)
# print(frame)
# print(frame['tz'][:10]) # print 10 time zones

# tz_counts = frame['tz'].value_counts() # use value_counts() to count the frequency of a value
# print(tz_counts[:10])


# display the graph of top 10 timezones
# clean_tz = frame['tz'].fillna('Missing') # fill missing values
# clean_tz[clean_tz == ''] = 'Unknown' # fill empty strings with Unknown
# tz_counts = clean_tz.value_counts()
# # print(tz_counts[:10])
# tz_counts[:10].plot(kind='barh', rot=0) # make a horizonal bar plot using the plot method
# # print(frame['a'][1])
# plt.show() # display the top 10 time zones 

results = Series([x.split()[0] for x in frame.a.dropna()])
# print(results[:5])

# print(results.value_counts()[:8]) 

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows') # check if the string contains 'Windows'
# print(operating_system[:5]) # return the first 5 records whether windows or not


by_tz_os = cframe.groupby(['tz', operating_system]) # group by timezone and os
agg_counts = by_tz_os.size().unstack().fillna(0) # use unstack to reshape the results into a table; use size to coumpute the counts
# print(agg_counts[:10])

# use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
# print(indexer[:10])

# slice the last 10 rows
count_subset = agg_counts.take(indexer)[-10:0] # use take() to select rows in an order
print(count_subset)
