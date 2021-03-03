import requests
import pandas as pd
import datetime
e = datetime.datetime.now()

personal_token = 'Personal Access Token'
# database_dict={"Unique ID":0, "Repo Name":0, "Domain Name":0, "Count":0, "Date_range_parameter":0, "Date of Run":0}
database_dict={"Unique_ID":[], "Domain_Name":[], "Date":[], "Date_of_Run":[]}

commits_data = pd.read_excel('commits.xlsx')
i=0
total_commits = len(commits_data)
while i<total_commits:
    author_extract = commits_data[['author']].iloc[i].values[0]       #eval to string to dic
    if type(author_extract) == float:
        print('Empty no author data in author column', type(author_extract))
    elif author_extract:
        author_data = eval(author_extract)
        author_username = author_data['login']
        author_id = author_data['id']
        author_org_url = author_data['organizations_url']
        date_extract = commits_data[['commit']].iloc[i].values[0]
        author_commit_data = eval(date_extract)
        author_commit_data_extract = author_commit_data['author']
        date_data = author_commit_data_extract['date'].split('T')  # To split the string at T
        author_date = date_data[0]
        usr_org_info = requests.get(author_org_url + f"?access_token={personal_token}").json()
        author_org_tup = []
        mm = pd.DataFrame(usr_org_info)
        if not usr_org_info:
            author_org_tup = []
        else:
            for items in mm['login']:
                author_org_tup.append(items)
        date_of_run = e.strftime("%Y-%m-%d")
        database_dict["Unique_ID"].append(author_id)
        database_dict["Domain_Name"].append(author_org_tup)
        database_dict["Date"].append(author_date)
        database_dict["Date_of_Run"].append(date_of_run)
    else:
        print(author_extract)
    print(i)
    i = i + 1

database_frame=pd.DataFrame(database_dict)
database_frame.to_excel('databasefile.xlsx')