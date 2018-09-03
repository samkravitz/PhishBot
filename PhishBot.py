import tweepy
import time
import random

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('Phish_Bot')

f= open('lyrics.txt', 'r')

myList = []
for line in f:
    myList.append(line)

f.close()

myFollowers = api.followers_ids('krav1tz')
myFollowersLength = len(myFollowers)

counter = myFollowersLength - 105


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

def followUser(userIndex):
    api.create_friendship(myFollowers[userIndex])

