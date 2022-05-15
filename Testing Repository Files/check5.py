from sqlalchemy import create_engine
import requests
import pandas as pd
from datetime import date
import json

personal_token = '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'
# org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": []}}

# Getting all Commits data
since_date = '2021-02-15'
until_date = '2021-02-25'
repo_name = 'Hashicorp/consul'
date_range_parameter= f'{since_date} to {until_date}'
date_of_run = date.today()
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": [],'repo_name': f'{repo_name}', 'date_range_parameter': f'{date_range_parameter}', 'date_of_run':f'{date_of_run}'}}

df = pd.DataFrame()
n = 1
total_commits = 0
while True:
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&access_token={personal_token}&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url).json()
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

data = df


# Credentials to database connection
hostname="localhost"
dbname="mydb_name"
uname="my_user_name"
pwd="my_password"

# Create dataframe
df = pd.DataFrame(data=[[111,'Thomas','35','United Kingdom'],
		[222,'Ben',42,'Australia'],
		[333,'Harry',28,'India']],
		columns=['id','name','age','country'])

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table
df.to_sql('users', engine, index=False)
