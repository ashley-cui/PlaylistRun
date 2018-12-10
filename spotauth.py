from __future__ import print_function

import sys
import spotipy
import os


import os
from spotipy import oauth2
import spotipy


class spt:
	def __init__(self,username):
		client_id = os.environ["SPOTIPY_CLIENT_ID"]
		client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
		redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
		scope = 'playlist-read-private'

		cache_path =".cache-" + username
		self.sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, 
        scope=scope, cache_path=cache_path)


	def auth(self):
		# token_info = self.sp_oauth.get_cached_token()
		# if not token_info:
		auth_url = self.sp_oauth.get_authorize_url()
		return auth_url
	def callback(self,url):
		code = self.sp_oauth.parse_response_code(url)
		token_info = self.sp_oauth.get_access_token(code)
		token=token_info['access_token']
		self.sp = spotipy.Spotify(auth=token)
		return
	def playlist(self):
		results = self.sp.current_user_playlists(limit=5)
		lst=[]
		for i, item in enumerate(results['items']):
			lst.append(item['name'])
		return lst
		

