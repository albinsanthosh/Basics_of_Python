import requests
import pandas as pd
personal_token = 'Personal access token'
org_dict = {'Misc':{'unique_contributors': 0,'total_contributions': 0, "id": []}}
cd = pd.read_excel('check_commits.xlsx')

# To get the users organization api url of the commits
k = 0
for i in cd['author']:
    j = eval(i)
    org_url = j['organizations_url']
    k = k+1
    print(f"loading..{k}.", end='.')
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

print(org_dict)