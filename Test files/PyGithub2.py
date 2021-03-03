import pandas as pd
from github import Github
import requests
#Github API Use

#info_url = 'https://api.github.com/repos/'

#info_url = 'https://api.github.com/repos/nic-delhi/AarogyaSetu_Android'
info_url = 'https://api.github.com/repos/albinsanthosh/hello-world/'

user_info = requests.get(info_url).json()
print(user_info)
print("*******************************")

g = Github("Token")
for repo in g.get_user().get_repos():
    print(repo)
print("*******************************")

'''
#lst = ['Anubhav', 'Saketh', 'Albin', 'Jansy', 'Poornima']
lst = {'Name':['Tom', 'Nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], 'Grade':['A', 'B', 'F', 'B']}

df=pd.DataFrame(lst)
df.to_excel("5_Feb.xlsx")
df.to_excel("output.xlsx",
             sheet_name='LEAP')
print(df)
print("*******************************")

#use 'Get' to fetch the insights//// Research
'''