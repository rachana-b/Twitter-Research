from __init__ import TwitterBot

retweeted_users = []

for i in range(2):
    my_bot = TwitterBot(TwitterBot.CONFIG_FOLDER + "/" + TwitterBot.CONFIG_PRESTRING_THC + str(i) + TwitterBot.DOT_TXT)
    my_bot.sync_follows()                                                          
    retweeted_users = my_bot.follow_retweeted_users()

#r = open(TwitterBot.RETWEET_ORIGIN, "a")

#record who has been followed
#r.write("\n".join([str(i) for i in retweeted_users]))
#r.write("\n")






