import requests
import pandas as pd
personal_token = 'Personal access token'
since_date = '2021-01-15'
until_date = '2021-01-30'
repo_name = 'Hashicorp/consul'
df = pd.DataFrame()
n = 1
total_commits = 0
while requests.get(f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&access_token={personal_token}&since={since_date}&until={until_date}').json():
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&access_token={personal_token}&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url).json()
    no_of_items = len(commit_info)
    total_commits = total_commits + no_of_items
    dm = pd.DataFrame(commit_info)
    df = pd.concat([df, dm], ignore_index=True)
    n = n + 1
    print(f"Loading..{no_of_items}.", end=".")

df.to_excel(f'check_commits.xlsx',
            sheet_name='Test')
print(f"\nTotal commits", total_commits)

