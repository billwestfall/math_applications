import requests
import base64

client_id = "abcdef1234567890abcdef1234567890"
client_secret = "0987654321fedcba0987654321fedcba"

encoded = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")

headers = {
     "Content-Type": "application/x-www-form-urlencoded",
     "Authorization": "Basic " + encoded
}
 
payload = {
     "grant_type": "client_credentials"
}
 
response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
print(response)
print(response.text)
