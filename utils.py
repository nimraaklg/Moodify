import base64
import os
import requests

access_token_uri = 'https://accounts.spotify.com/api/token'

def getClientId():
    return os.environ.get('SPOTIPY_CLIENT_ID')

def getClientSecret():
    return os.environ.get('SPOTIPY_CLIENT_SECRET')

def getAccessToken(userToken):
    data = {}
    headers = {}

    data['grant_type'] = 'authorization_code'
    data['code'] = userToken
    data['redirect_uri'] = 'http://localhost:8000/callback'

    stringToEncode = getClientId()+':'+getClientSecret()
    headers['Authorization'] = 'Basic '+ base64.b64encode(stringToEncode.encode("ascii")).decode("ascii")
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    return requests.post(url=access_token_uri,data=data,headers=headers)

