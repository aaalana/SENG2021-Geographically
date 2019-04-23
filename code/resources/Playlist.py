import pprint
import sys
import os
import subprocess

import spotipy
import spotipy.util as util
from flask_restful import Resource, Api
from flask import Flask, request, render_template

scope = 'user-library-read user-read-private playlist-modify-private playlist-modify-public'
username = '22stxr3b7ebjtbaziyqo2f4uq'
token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

class Playlist(Resource):
    def getSavedTracks():
        #scope = 'user-library-read user-read-private playlist-modify-private playlist-modify-public'

        # if len(sys.argv) > 1:
        #     username = sys.argv[1]
        # else:
        #     print ("Usage: "+sys.argv[0]+" username")
        #     sys.exit()
        #username = 'dzjycnhgjo8pi9jdc51lq03p6'
        #token = util.prompt_for_user_token(username, scope,client_id='bc86092a5ca04208aedcfe36beeba7c6',client_secret='97f76e9a5cf943349ec3a750708d6b32',redirect_uri='http://localhost:8888/callback/')

        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print (track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print ("Can't get token for", username)

    def searchTracks(weather):
        #scope = 'user-read-private'
        #need to prompt user to get username
        #username = 'dzjycnhgjo8pi9jdc51lq03p6'
        #token = util.prompt_for_user_token(username, scope,client_id='bc86092a5ca04208aedcfe36beeba7c6',client_secret='97f76e9a5cf943349ec3a750708d6b32',redirect_uri='http://localhost:8888/callback/')

        sp = spotipy.Spotify(auth=token)

        results = sp.search(q=weather, type="track", limit=10)
        for i, t in enumerate(results['tracks']['items']):
            print (' ', i, t['uri'])
        return results

    def createPlaylist(weather, location):
        print("WE ARE HERE")
        #if len(sys.argv) > 2:
        #username = 'dzjycnhgjo8pi9jdc51lq03p6'
        playlist_name = location
        playlist_description = location + "on a" + weather + "day"
        # else:
        #     print("Usage: %s username playlist-name playlist-description" % (sys.argv[0],))
        #     sys.exit()

        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            playlists = sp.user_playlist_create(username, playlist_name, public=False, description=playlist_description)
            tracks = Playlist.searchTracks(weather)
            li = []
            for t in enumerate(tracks['tracks']['items']):
                li.append(t[1]['uri'])
            results = sp.user_playlist_add_tracks(username, playlists['id'], li)

        else:
            print("Can't get token for", username)
