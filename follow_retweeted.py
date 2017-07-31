from __init__ import TwitterBot
import sys

retweeted_users = []

if(len(sys.argv) < 2):
	print ("Error: Expected bot number as argument")
else:
    i = sys.argv[1]
    convergeNum = 100
    # construct the TwitterBot - supply the path to the config text file specific to this bot
    my_bot = TwitterBot(TwitterBot.CONFIG_FOLDER + "/" + TwitterBot.CONFIG_PRESTRING + str(i) + TwitterBot.DOT_TXT)
    my_bot.sync_follows()                                                          
    retweeted_users = my_bot.follow_retweeted_users(i, 20)
    if len(retweeted_users) > convergeNum:
        my_bot.sync_follows()
        diff = len(retweeted_users)-convergeNum
        my_bot.auto_unfollow_convergance(diff, i)
