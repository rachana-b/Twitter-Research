# springIW


## Following new users based on retweets

You can follow new users using the follow_retweeted script:
```
python follow_retweeted.py [botnum]
```

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



## Generating graphs for the bots in experiment 1

We use networkx, graphviz, and dot to visualize the Follow Forests of the bots in experiment 1. Run the following, where inputfile is one of the log files from experiment 1. The outputfile should have the .dot extension:
```
python grapher.py [inputfile] [outputfile]
```

Do it for all the bots (won't color the nodes, though):
```
./generate_graphs.sh
```