import pandas as pd
import sys
import re

filename = sys.argv[1]
cycle = sys.argv[2]

f = [line for line in open(filename) if 'RACHANA_TAG' in line]

handle_tweet_dict = {}
table = [['Class', 'Handle']]

for line in f:
    words = line.split(' ', 2)
    handle = re.sub(' Retweeted', '', words[2])
    if handle not in handle_tweet_dict:
        handle_tweet_dict[handle] = 1
    else:
        handle_tweet_dict[handle] = handle_tweet_dict[handle] + 1
    if words[1] == 'RACHANA_TAGc':
        table.append(['c', handle])
    elif words[1] == 'RACHANA_TAGn':
        table.append(['n', handle])
    elif words[1] == 'RACHANA_TAGl':
        table.append(['l', handle])
    else:
        print("Nothing matched: " + words[0])

headers = table.pop(0)
df = pd.DataFrame(table, columns=headers)
print(df)
print(handle_tweet_dict)

output = 'output'+str(cycle)+'.xlsx'

writer  = pd.ExcelWriter(output)
df.to_excel(writer,'Sheet1')