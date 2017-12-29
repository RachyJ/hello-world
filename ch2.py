import json
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt

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
operating_system[:5]

