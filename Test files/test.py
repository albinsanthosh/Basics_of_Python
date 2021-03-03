import requests
import pandas as pd
from openpyxl import load_workbook

n = 1
total = 0
access_token='Personal Access Token'
while requests.get(f'https://api.github.com/repos/hashicorp/consul/contributors?page={n}&per_page=100&access_token={access_token}').json():
    info_url = f'https://api.github.com/repos/hashicorp/consul/contributors?page={n}&per_page=100&access_token={access_token}'
    commit_info = requests.get(info_url).json()
    print(len(commit_info))
    total = len(commit_info) + total
    df = pd.DataFrame(commit_info)
    df.to_excel(f'hello{n}.xlsx')
    n = n + 1

print(total)
#df.reset_index(drop=True, inplace=True)
