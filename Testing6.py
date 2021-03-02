import requests
import pandas as pd
personal_token = '1bc39f552049b711d3a748c8d8b0d4082f6c86fb'

org_element = {"total_contributions": 0, "unique_contributors": 0}

commits_data = pd.read_excel('commits.xlsx')
i=0
total_commits = len(commits_data)
while(i<total_commits):
    author_extract = commits_data[['author']].iloc[i].values[0]       #eval to string to dic
    try:
        author_data = eval(author_extract)
    except Exception as err:
        print(f"Information not found of {i} row, Error =", err)
    author_username = author_data['login']
    author_id = author_data['id']
    author_org_url= author_data['organizations_url']
    date_extract = commits_data[['commit']].iloc[i].values[0]  # eval to string to dic
    author_commit_data = eval(date_extract)
    author_commit_data_extract = author_commit_data['author']
    date_data = author_commit_data_extract['date'].split('T')        # To split the string at T
    author_date = date_data[0]
    usr_org_info = requests.get(author_org_url + f"?access_token={personal_token}").json()
    author_org_tup = []
    mm = pd.DataFrame(usr_org_info)
    #try:
    if not usr_org_info:
        author_org_tup = []
    else:
        for items in mm['login']:
            author_org_tup.append(items)
            # except Exception as err1:
        # print(f"No organization information found, Error =", err1)
    print(author_date,author_username, author_id, author_org_tup)
    i = i + 1
