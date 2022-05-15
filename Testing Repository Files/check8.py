import requests
import pandas as pd
from datetime import date

personal_token = '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'
HEADER = {'Authorization': f'{personal_token}'}

# Short header code
# HEADER = {'Authorization': f'{personal_token}'}
# commit_info = requests.get(info_url, HEADER).json()


# Getting all Commits data
since_date = '2020-10-15'
until_date = '2021-02-25'
repo_name = 'Hashicorp/consul'
date_range_parameter= f'{since_date} to {until_date}'
date_of_run = date.today()
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": [],'repo_name': f'{repo_name}', 'date_range_parameter': f'{date_range_parameter}', 'date_of_run':f'{date_of_run}'}}

df = pd.DataFrame()
n = 1
total_commits = 0
while True:
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url, HEADER).json()
    if commit_info:
        no_of_items = len(commit_info)
        print(no_of_items)
        total_commits = total_commits + no_of_items
        print("Total commits ",total_commits)
        df = pd.concat([df, pd.DataFrame(commit_info)], ignore_index=True)
        n = n + 1
        print(df.shape)
    else:
        print("Completed")
        break

