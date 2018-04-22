from __init__ import TwitterBot
import sys

import credentials

if(len(sys.argv) < 3):
    print ("Error: Expected bot number and flag as argument")
else:
    i = sys.argv[1]
    flag = sys.argv[2]

    # construct the TwitterBot - supply the path to the config text file specific to this bot
    my_bot = TwitterBot(TwitterBot.CONFIG_FOLDER + "/" + TwitterBot.CONFIG_PRESTRING + str(i) + TwitterBot.DOT_TXT)   

    if flag == 'c':
        keywords = credentials.con
    elif flag == 'l':
        keywords = credentials.lib

    for k in keywords:
        print(k)
        my_bot.sync_follows()
        my_bot.auto_rt(k, count=5)
