from os import environ as env

try:
    # OAuth2 client ID and secret
    CLIENT_ID = env['9a05e766bcbe2e041cf4f2de7c47d1fece342123']
    CLIENT_SECRET = env['b81de923a944e070c397b08a78b133f813b83522']

    # Just use client secret as key for signing session cookies
    SECRET_KEY = CLIENT_SECRET

except KeyError:
    print('You need to set CLIENT_ID and CLIENT_SECRET in the environment for this app')
    print ('e.g `CLIENT_ID=XXXX CLIENT_SECRET=YYYY python app.py`')
    exit(1)

