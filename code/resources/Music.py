import pprint
import sys
import spotipy
import spotipy.util as util
from flask_restful import Resource, Api
from flask import Flask, request, render_template

class Music(Resource):
    def getSavedTracks():
        scope = 'user-library-read'

        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print ("Usage: "+sys.argv[0]+" username")
            sys.exit()

        token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

        if token:
            sp = spotipy.Spotify(auth=token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print (track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print ("Can't get token for", username)

    def getPlaylists():
        if len(sys.argv) > 3:
            username = sys.argv[1]
            playlist_id = sys.argv[2]
            track_ids = sys.argv[3:]
        else:
            print ("Usage: username playlist_id track_id ...")
            sys.exit()

        scope = 'playlist-modify-public'
        token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
            print (results)
        else:
            print ("Can't get token for", username)

    def show_tracks(tracks):
        for i, item in enumerate(tracks['items']):
            track = item['track']
            print (i, track['artists'][0]['name'],
                track['name'])

    def getPlaylist():
        scope = 'playlist-read-private'
        if len(sys.argv) > 1:
            username = sys.argv[1]
        else:
            print ("Whoops, need your username!")
            print ("usage: python user_playlists.py [username]")
            sys.exit()

        token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(username)
            for playlist in playlists['items']:
                if playlist['owner']['id'] == username:
                    print (playlist['name'])
                    print ('  total tracks', playlist['tracks']['total'])
                    results = sp.user_playlist(username, playlist['id'],
                        fields="tracks,next")
                    tracks = results['tracks']
                    show_tracks(tracks)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        show_tracks(tracks)
        else:
            print ("Can't get token for", username)

    def addTrackToPlaylist():
        if len(sys.argv) > 3:
            username = sys.argv[1]
            playlist_id = sys.argv[2]
            track_ids = sys.argv[3:]
        else:
            print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
            sys.exit()

        scope = 'playlist-modify-public'
        token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
            print(results)
        else:
            print("Can't get token for", username)

    def searchPlaylist():
        scope = 'user-read-private'
        #need to prompt user to get username
        username = '22stxr3b7ebjtbaziyqo2f4uq'
        token = util.prompt_for_user_token(username, scope,client_id='e960201f128b45449faf1fae16868a11',client_secret='6a40f65f1ee54c54a38eaa6df0680adf',redirect_uri='http://localhost:8080/playlists')

        sp = spotipy.Spotify(auth=token)

        results = sp.search(q="Rain", type="playlist", limit=10)
        for i, t in enumerate(results['playlists']['items']):
            print (' ', i, t['external_urls']['spotify'])

        return results