#! /usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import LED
from TwitterAPI import TwitterAPI
from oauth import *
import time

# set up 2 pins for LEDs
yLed = LED(20)
rLed = LED(21)

#### specify hashtags to follow
# can be separated by comma: '#jesus,#pizza,#selfie'
TRACK_TERM = '#jesus'

# set up the TwitterAPI object
api = TwitterAPI(CONSUMER_KEY,CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)

# this is the responseobject from twitter.
# it gets updated everytime a new tweet comes in with the TRACK_TERMs
response = api.request('statuses/filter', {'track': TRACK_TERM})

# this goes through the tweets availalble in the response object
for tweet in response:
    print(tweet['text'] if 'text' in tweet else '')
    rLed.blink(on_time=1, n=1)
    yLed.blink(on_time=1, n=1)
