import requests
from pprint import pprint
access_token='Personal access token'
username = "albinsanthosh"
url = f"https://api.github.com/users/adrifer/orgs?access_token={access_token}"
user_data = requests.get(url).json()
pprint(user_data)
