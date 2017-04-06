#!/bin/bash

## Update Follow List for bots 0, 1, 2, 3, 4, 5

echo "Getting Twitter feeds..."
echo "Finding new people to follow based on retweets..."
python follow_retweeted.py 0 &
python follow_retweeted.py 1 &
python follow_retweeted.py 2 &
python follow_retweeted.py 3 &
python follow_retweeted.py 4 &
python follow_retweeted.py 5 
wait
echo "Follow Lists updated"