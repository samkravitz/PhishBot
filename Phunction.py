import random
from musixmatch import Musixmatch
from credentials import *

musixmatch = Musixmatch(music_key)

def getTweet(albums):
    num_albums = len(albums)
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
