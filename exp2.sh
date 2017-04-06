#!/bin/bash

## Update Follow List for bots 6, 7

echo "Logging into Twitter..."
echo "Finding new people to follow based on Twitter's recommendations..."
python follow_recommended.py 6 &
python follow_recommended.py 7 &
python follow_recommended.py 8
wait
echo "Follow Lists updated"
echo "springiwthc6 : conservative"
echo "springiwthc7 : liberal"
echo "springiwthc8 : 50-50 split"