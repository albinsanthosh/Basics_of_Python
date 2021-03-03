import requests
import pandas as pd
access_token="Personal access token"
org_url = f"https://api.github.com/repos/Hashicorp/consul/contributors?since=2021-01-15&until=2021-01-19&access_token={access_token}"
commit_info = requests.get(org_url).json()
dm = pd.DataFrame(commit_info)
dm.to_excel("dm.xlsx")
