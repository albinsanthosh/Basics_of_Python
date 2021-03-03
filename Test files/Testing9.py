import requests
import pandas as pd
personal_token = 'Personal Access Token'
org_dict = {'Misc':{'unique_contributors':0}}

dd = pd.read_excel('contributors.xlsx')

# To get the users organization api url of the contributors
i = 0
while i < len(dd):
    org_url = dd[['organizations_url']].iloc[i].values[0]
    i = i+1
    print(f"loading..{i}.", end='.')
    usr_org_info = requests.get(org_url+f"?access_token={personal_token}").json()
    # if the organization is empty
    mm = pd.DataFrame(usr_org_info)
    if not usr_org_info:
        org_dict['Misc']['unique_contributors'] = org_dict['Misc']['unique_contributors'] + 1
    else:
        for items in mm['login']:
            if items in org_dict.keys():
                org_dict[items]['unique_contributors'] = org_dict[items]['unique_contributors'] + 1
            else:
                org_dict[items] = {'unique_contributors':1}

print(org_dict)
