import requests
from pprint import pprint
username = "albinsanthosh"
url = f"https://api.github.com/users/adrifer/orgs?access_token=1bc39f552049b711d3a748c8d8b0d4082f6c86fb"
user_data = requests.get(url).json()
pprint(user_data)
