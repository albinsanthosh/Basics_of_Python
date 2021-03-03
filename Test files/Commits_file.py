import requests
import pandas as pd

access_token="Personal access token"
df = pd.DataFrame()
n = 1
total_commits = 0
while requests.get(f'https://api.github.com/repos/hashicorp/consul/commits?page={n}&per_page=100&access_token={access_token}).json():
    info_url = f'https://api.github.com/repos/hashicorp/consul/commits?page={n}&per_page=100&access_token=1bc39f552049b711d3a748c8d8b0d4082f6c86fb'
    commit_info = requests.get(info_url).json()
    no_of_items = len(commit_info)
    total_commits = total_commits + no_of_items
    dm = pd.DataFrame(commit_info)
    df = pd.concat([df, dm], ignore_index=True)
    n = n + 1
    print(f"Loading..{no_of_items}.", end=".")

df.to_excel(f'commits.xlsx',
            sheet_name='Test')
print(f"\nTotal commits", total_commits)

