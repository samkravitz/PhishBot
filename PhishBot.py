#PhishBot
#this bot tweets random lyrics from the legendary rock band from Vermont Phish's extensive catalog
#link to the bot is https://twitter.com/Phish_Bot
#Created by Sam Kravitz

import tweepy
import time
import random
from musixmatch import Musixmatch

musixmatch = Musixmatch('<key>')

#values changed for security purposes.
#access apps.twitter.com to find the values for your specific project
auth = tweepy.OAuthHandler('<consumer_key>', '<consumer_secret>')
auth.set_access_token('<access_token>', '<access_token_secret>')

#authorizes the bot and loads in its username
api = tweepy.API(auth)
user = api.get_user('Phish_Bot')

#at the moment the bot also follows follower of my main account, @krav1tz
#myFollowers is an array containing each user who follows @krav1tz
myFollowers = api.followers_ids('krav1tz')
myFollowersLength = len(myFollowers)

#artist
phish = musixmatch.artist_search('phish', 1, 1, 0, 0)
phish_id = phish['message']['body']['artist_list'][0]['artist']['artist_id']

#albums
albums = musixmatch.artist_albums_get(phish_id,0,1,100,0)
album_list = albums['message']['body']['album_list']

new_album_list = []
new_album_dic = {}

# filter live albums
for album in album_list:
    name = album['album']['album_name']
    if name[:1].isdigit():
        pass
    elif 'Phish' in name:
        pass
    elif 'Live' in name:
        pass
    elif 'At' in name:
        pass
    elif "'" in name:
        pass
    elif 'Want to Do' in name:
        pass
    elif name not in new_album_dic:
        new_album_dic[name] = album
        new_album_list.append(album)

def getTweet():
    num_albums = len(new_album_list)
    albums = new_album_list
    random_album = albums[random.randint(0, num_albums - 1)]

    # tracks
    tracks = musixmatch.album_tracks_get(random_album['album']['album_id'], 1, 100, 0)
    tracks = tracks['message']['body']['track_list']
    num_tracks = len(tracks)
    rand = int(random.randint(0, num_tracks - 1))
    random_track = tracks[rand]

    # lyrics
    lyrics = musixmatch.track_lyrics_get(random_track['track']['track_id'])
    lyrics = lyrics['message']['body']['lyrics']['lyrics_body']

    lyricsf = ''
    for line in lyrics.split('\n'):
        if '...' in line:
            pass
        elif 'Lyrics' in line:
            pass
        elif '(' in line:
            pass
        elif not line.strip() == '':
            lyricsf += line + '\n'

    lyricsf = lyricsf.rstrip()

    lines = lyricsf.splitlines()
    nlines = len(lines)
    rline = random.randint(0, nlines - 1)

    tweet = ''

    while rline < nlines and len(tweet) < 150:
        tweet += lines[rline]
        tweet += '\n'
        rline += 1
    return tweet.rstrip()    


#this loop goes until all of my followers have been followed, will be changed later to run indefinitely
while (True):
    tweet = getTweet()
    try:
        api.update_status(tweet)
    except tweepy.error.TweepError:
        api.update_status(getTweet)
    
    time.sleep(1800)
