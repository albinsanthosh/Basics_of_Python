import requests
import pandas as pd
personal_token = 'Personal Access Token'
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": []}}

# Getting all Commits data
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

# Data processing
cd = pd.read_excel('check_commits.xlsx')

# To get the users organization api url of the commits
k = 0
for i in cd['author']:
    j = eval(i)
    org_url = j['organizations_url']
    usr_org_info = requests.get(org_url+f"?access_token={personal_token}").json()
    co = pd.DataFrame(usr_org_info)
    # if the organization is empty
    if not usr_org_info:
        org_dict['Misc']['total_contributions'] = org_dict['Misc']['total_contributions'] + 1
        if j['id'] not in org_dict['Misc']['id']:
            org_dict['Misc']['id'].append(j['id'])  # org id List
            org_dict['Misc']['unique_contributors'] = org_dict['Misc']['unique_contributors'] + 1  # Addition of unique id to unique contributions
        else:
            pass
    else:
        for items in co['login']:
            if items in org_dict.keys():
                org_dict[items]['total_contributions'] = org_dict[items]['total_contributions'] + 1
            else:
                org_dict[items] = {'total_contributions': 1, 'unique_contributors': 0, 'id': []}
            if j['id'] not in org_dict[items]['id']:
                org_dict[items]['id'].append(j['id'])       # org id List
                org_dict[items]['unique_contributors'] = org_dict[items]['unique_contributors'] + 1 # Addition of unique id to unique contributions
            else:
                pass
    k = k + 1
    print(f"loading..{k}.", end='.')

for organization in org_dict:
    org_dict[organization].pop('id')

print(org_dict)