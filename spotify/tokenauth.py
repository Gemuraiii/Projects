import base64
from secrets import *
import requests
import json

headers = {}
data = {}
client_id = ""
secret_id = ""
redirect_uri = ""

ml_creds = f"{client_id}:{secret_id}"
messageid = ml_creds.encode('ascii')
client_creds64 = base64.b64encode(messageid)
client_message64 = client_creds64.decode('ascii')

token_url = "https://accounts.spotify.com/api/token"
headers['Authorization'] = f"Basic {client_message64}"
data['grant_type'] = "client_credentials"
r = requests.post(token_url, headers=headers, data=data)

print(json.dumps(r.json(), indent=2))

token = r.json()['access_token']
print(token)

recently_played = f"https://api.spotify.com/v1/me/player/recently-played?limit=10&after=1484811043508"
headers = {
    "Authorization": "Bearer " + token
}
res = requests.get(url=recently_played, headers = headers)

print(json.dumps(res.json(), indent=2))
