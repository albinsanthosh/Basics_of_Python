import requests
import pandas as pd

org_url = "https://api.github.com/repos/Hashicorp/consul/contributors?since=2021-01-15&until=2021-01-19&access_token=1bc39f552049b711d3a748c8d8b0d4082f6c86fb"
commit_info = requests.get(org_url).json()
dm = pd.DataFrame(commit_info)
dm.to_excel("dm.xlsx")
