from __future__ import print_function

import sys
import spotipy
import os


import os
from spotipy import oauth2
import spotipy

class spot:
	def __init__(self):
		client_id = os.environ["SPOTIPY_CLIENT_ID"]
		client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
		redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
		scope = 'playlist-read-private'

		cache_path =".cache-" + username
		sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, 
        scope=scope, cache_path=cache_path)


	def auth(self):
		token_info = sp_oauth.get_cached_token()
		if not token_info:
			auth_url = sp_oauth.get_authorize_url()
		return auth_url
	def songs(self,url):
		lst=[]
		code = sp_oauth.parse_response_code(url)
		token_info = sp_oauth.get_access_token(code)
		token=token_info['access_token']
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_playlists(limit=5)
		for i, item in enumerate(results['items']):
			lst.append(item['name'])
		return lst
		





    # if not client_id:
    #     print("set env varibles")
    #     raise spotipy.SpotifyException(550, -1, 'no credentials set')

    # sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, 
    #     scope=scope)

#     # try to get a valid token for this user, from the cache,
#     # if not in the cache, the create a new (this will send
#     # the user to a web page where they can authorize this app)

#     token_info = sp_oauth.get_cached_token()



#     if not token_info:
#         auth_url = sp_oauth.get_authorize_url()



#     #     code = sp_oauth.parse_response_code(INSERTURL;)
#     #     token_info = sp_oauth.get_access_token(code)
#     # # Auth'ed API request
#     # if token_info:
#     #     return token_info['access_token']
#     # else:
#     #     return None






# def callback(authurl):
# 	client_id = os.environ["SPOTIPY_CLIENT_ID"]
# 	client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
# 	redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
# 	scope = 'user-library-read'

# 	sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope)
# 	code = sp_oauth.parse_response_code(authurl)
# 	token_info = sp_oauth.get_access_token(code)


# 	if token:
# 	    sp = spotipy.Spotify(auth=token)
# 	    results = sp.current_user_saved_tracks()
# 	    return results['items']
# #         track = item['track']
# #         print track['name'] + ' - ' + track['artists'][0]['name']
# # else:
# #     print "Can't get token for", username




