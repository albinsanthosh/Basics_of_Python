import requests
import pandas as pd
personal_token = 'Personal Access Token'

org_dict = {'Misc': 0}
org_element = {"total_contributions": 0, "unique_contributors": 0}

commits_data = pd.read_excel('commits.xlsx')
i=0
total_commits = len(commits_data)
while(i<total_commits):
    commits_extract = commits_data[['commit']].iloc[i].values[0]        #eval to string to dic
    commits_extract_eval=eval(commits_extract)
    author = commits_extract_eval['author']
    author_name = author['name']
    date_split = author['date'].split('T')
    commit_date = date_split[0]
    print(commit_date,author_name,)
    i = i + 1
