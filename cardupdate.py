from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from youtube_search import YoutubeSearch

PLAYLISTS = [['PlaylistSơn Tùng M-TP','https://open.spotify.com/playlist/2vRAVVZPHYkhLi6emhLGr4', "RDEMeyKnYmm7ScRhnRO9nwOSNA"]
, ['MONO:Spotlight','https://open.spotify.com/playlist/4i4XBc2v8PiaYjofYZnBz3', "RDEMn8P8-bKscmoNGYJ0nOCTqQ"],
['tlinh playlist','https://open.spotify.com/playlist/5lFpHDSs2pbS4OFb5LkJ4A', "RDEMOqgEKnqXR2T0L-KTM3WhQQ"]

]
client_credentials_manager = SpotifyClientCredentials(client_id='e5d66c188ef64dd89afa4d13f9555411',
                client_secret='d070988d7bd5479a9e0818fa23839544')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



CONTAINER = []
for playlist in PLAYLISTS:
    Name,Link,playlistid = playlist
    playlistcard = []
    count = 0
    PlaylistLink = "http://www.youtube.com/watch_videos?video_ids="
    for i in (sp.playlist_tracks(Link)['items']):
        if count == 50:
            break
        try:
            song = i['track']['name'] + i['track']['artists'][0]['name']
            songdic = (YoutubeSearch(song, max_results=1).to_dict())[0]
            playlistcard.append([songdic['thumbnails'][0],songdic['title'],songdic['channel'],songdic['id']])
            PlaylistLink += songdic['id'] + ','
        except:
            continue
        count += 1

    from urllib.request import urlopen
    req = urlopen(PlaylistLink)
    PlaylistLink = req.geturl()
    print(PlaylistLink)
    PlaylistId = PlaylistLink[PlaylistLink.find('list')+5:]

    CONTAINER.append([Name,playlistcard,playlistid])

import json

json.dump(CONTAINER,open('card.json', 'w'),indent = 6) 
