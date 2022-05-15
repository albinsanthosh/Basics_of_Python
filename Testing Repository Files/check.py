import requests
import pandas as pd
from datetime import date
import json

personal_token = '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'
# org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": []}}

# Getting all Commits data
since_date = '2020-10-01'
until_date = '2021-03-25'
repo_name = 'Hashicorp/consul'
date_range_parameter= f'{since_date} to {until_date}'
date_of_run = date.today()
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": [],'repo_name': f'{repo_name}', 'date_range_parameter': f'{date_range_parameter}', 'date_of_run':f'{date_of_run}'}}

def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

n = 1
total_commits = 0
while True:
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&access_token={personal_token}&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url).json()
    print(commit_info)
    if commit_info:
        no_of_items = len(commit_info)
        print(no_of_items)
        total_commits = total_commits + no_of_items
        print("Total commits ",total_commits)
        with open('data.json') as json_file:
            data = json.load(json_file)
        temp = data['Commits Info']
        temp.append(commit_info)
        write_json(data)
        n = n + 1
    else:
        print("Completed")
        break

print(temp)
