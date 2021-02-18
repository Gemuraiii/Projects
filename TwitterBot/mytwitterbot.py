# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name:       
# netid:      
# Student ID: 

import sys
import time
import simple_twit 


def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()]

    simple_twit.version()
    
    # Project 04 Exercises

   
    # Exercise 1 - Get and print 10 tweets from your home timeline
    tweet10 = simple_twit.get_home_timeline(api=api, count=20)
    for t in tweet10:
        print(t.full_text)
    
    # Exercise 2 - Get and print 10 tweets from another user's timeline
    Spy10 = simple_twit.get_user_timeline(api = api, user= "heymyy__", count = 20)
    for st in Spy10:
        print(st.full_text)
    # Exercise 3 - Post 1 tweet to your timeline.
    simple_twit.send_tweet(api=api, text="I tweeted my first tweet, Hold my head")
    
    # Exercise 4 - Post 1 media tweet to your timeline.
    simple_twit.send_media_tweet(api=api, text="This is a picture from my archives", filename= "C:/Users/Glen F/OneDrive/Desktop/test.png")
    
    simple_twit.send_tweet(api=api, text="test #2 I think, media isn't working")

    # YOUR BOT CODE BEGINS HERE
    
# end def main()

if __name__ == "__main__":
       main()
