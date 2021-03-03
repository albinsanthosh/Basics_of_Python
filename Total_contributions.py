import requests
import pandas as pd
personal_token = 'Personal Access Token'
org_dict = {'Misc':{'unique_contributors':0,'total_contributions':0}}

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
    else:
        for items in co['login']:
            if items in org_dict.keys():
                org_dict[items]['total_contributions'] = org_dict[items]['total_contributions'] + 1
            else:
                org_dict[items] = {'total_contributions':1}

print(org_dict)