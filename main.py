#!/bin/python3

import requests
from secrets import client_id, client_secret

track_uri = '6y0igZArWVi6Iz0rj35c1Y'

def get_access_token(client_id, client_secret):
    ''' Uses a client's ID and Secret in order to retreive an access token using the client credentials flow. '''
    # https://developer.spotify.com/documentation/general/guides/authorization-guide/

    auth_url = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })

    # converting the response to JSON
    auth_response_data = auth_response.json()

    # returning the access token
    return auth_response_data['access_token']