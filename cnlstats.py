import pandas as pd
import sys
import re

filenames = open(sys.argv[1])

counts = [['c', 'n', 'l']]
props = [['c', 'l']] # proportion out of political content

print(filenames)
for name in filenames:
    print(name)
    name = 'classifications/'+name[:-1]
    f = [line for line in open(name) if 'RACHANA_TAG' in line]

    ccnt = lcnt = ncnt = 0
    handle_tweet_dict = {}

    for line in f:
        words = line.split(' ', 2)
        handle = re.sub(' Retweeted', '', words[2])
        if handle not in handle_tweet_dict:
            handle_tweet_dict[handle] = 1
        else:
            handle_tweet_dict[handle] = handle_tweet_dict[handle] + 1
        if words[1] == 'RACHANA_TAGc':
            ccnt += 1
        elif words[1] == 'RACHANA_TAGn':
            ncnt += 1
        elif words[1] == 'RACHANA_TAGl':
            lcnt += 1
        else:
            print("Nothing matched: " + words[0])

    counts.append([ccnt, ncnt, lcnt])
    cprop = ccnt/(ccnt+lcnt)
    lprop = lcnt/(ccnt+lcnt)
    props.append([cprop, lprop])

print(counts)
headers = counts.pop(0)
dfcount = pd.DataFrame(counts, columns=headers)

headers = props.pop(0)
dfprops = pd.DataFrame(props, columns=headers)

output = 'output.xlsx'
writer  = pd.ExcelWriter(output)
dfcount.to_excel(writer,'Sheet1')
dfprops.to_excel(writer,'Sheet2')
