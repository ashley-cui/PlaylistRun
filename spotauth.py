from __future__ import print_function

import sys
import spotipy
import os


import os
from spotipy import oauth2
import spotipy


class spt:
    def __init__(self,username):
        client_id = '1710c52bbc1147a1883149ff69f5c6ac'
        client_secret  = 'd7efbb25844d4618ab422a518efacb49'
        redirect_uri  = 'http://127.0.0.1:5000/callback'
        scope  = 'playlist-read-private'
        cache_path  =".cache-" + username
        self.sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, cache_path=cache_path)
        
    def auth(self):
        # oken_info = self.sp_oauth.get_cached_token()
        # f not token_info:
        auth_url  = self.sp_oauth.get_authorize_url()
        return auth_url
        
    def callback(self,url):
        code  = self.sp_oauth.parse_response_code(url)
        token_info  = self.sp_oauth.get_access_token(code)
        token = token_info['access_token']
        self.sp = spotipy.Spotify(auth=token)
        return

    def get_length(self, tracks):
        res = 0
        for i, item in enumerate(tracks['items']):
            track = item['track']
            de = self.sp.track(track['id'])
            res += int(de['duration_ms'])
        return res
    
    def playlist(self):
        results = self.sp.current_user_playlists(limit=5)
        lst = []
        #for i, item in enumerate(results['items']):
        #    lst.append(item['name'])
        for playlist in results['items']:
            ls = []
            ls.append(playlist['name'])
            trks = self.sp.user_playlist(self.sp, playlist['id'], fields="tracks,next")
            tracks = trks['tracks']
            ls.append(self.get_length(tracks))
            lst.append(ls)
        return lst