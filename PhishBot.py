#PhishBot
#this bot tweets random lyrics from the legendary rock band from Vermont Phish's extensive catalog
#link to the bot is https://twitter.com/Phish_Bot
#Created by Sam Kravitz

import tweepy
import time
import random

#values changed for security purposes.
#access apps.twitter.com to find the values for your specific project
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#authorizes the bot and loads in its username
api = tweepy.API(auth)
user = api.get_user('Phish_Bot')

f= open('lyrics.txt', 'r')

#array that contains every line from lyrics.txt as a sepparate element
myList = []
for line in f:
    myList.append(line)

f.close()

#at the moment the bot also follows follower of my main account, @krav1tz
#myFollowers is an array containing each user who follows @krav1tz
myFollowers = api.followers_ids('krav1tz')
myFollowersLength = len(myFollowers)

counter = myFollowersLength - 105

#followUser: follows the user who is located at a given index in my list of followers
#@param: integer value of index of user
#@return: void
def followUser(userIndex):
    api.create_friendship(myFollowers[userIndex])

#this loop goes until all of my followers have been followed, will be changed later to run indefinitely
while (counter > 0):
    toTweet = random.choice(myList)
    try:
        api.update_status(toTweet)
    except tweepy.error.TweepError:
        api.update_status(random.choice(myList))
    followUser(counter)
    print(api.get_user(myFollowers[counter]).screen_name)
    counter = counter - 1
    time.sleep(1800)
