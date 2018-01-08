# Twitter-Research

This repository contains a library of functions that can be used for research on Twitter, including a method for setting up
Twitter bots.

## Following new users based on retweets

You can follow new users using the follow_retweeted script:
```
python follow_retweeted.py [botnum]
```
Make sure to edit handle, username, password, etc. in the ```__init__.py``` file.

Do it for all the bots:
```
./exp1.sh
```


## Following new users based on Twitter's recommendations

You can folow new users using the follow_recommended script:
```
python follow_recommended.py [botnum]
```

Do it for all the bots:
```
./exp2.sh
```


## Liking random posts in the newsfeed using Selenium

```
python like_and_retweet.py [botnum]
```

Do it for all:
```
./like.sh
```


## Collecting followee bio data

You can scrape the followee bios using the util script:
```
python util.py [botnum]
```

## Collecting news feed content data

You can scrape the tweets in the news feed ranked by Best Tweets First using the clasify_nf script:
```
python classify_nf.py [botnum]
```

## Data analysis of news feed content
You can calculate the proportions and counts of news feed tweets using the cnlstats script:
```
python cnlstats.py [filenames]
```