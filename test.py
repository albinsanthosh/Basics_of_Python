import requests
import pandas as pd
from openpyxl import load_workbook

n = 1
total = 0

while requests.get(f'https://api.github.com/repos/hashicorp/consul/contributors?page={n}&per_page=100&access_token=1bc39f552049b711d3a748c8d8b0d4082f6c86fb').json():
    info_url = f'https://api.github.com/repos/hashicorp/consul/contributors?page={n}&per_page=100&access_token=1bc39f552049b711d3a748c8d8b0d4082f6c86fb'
    commit_info = requests.get(info_url).json()
    print(len(commit_info))
    total = len(commit_info) + total
    df = pd.DataFrame(commit_info)
    df.to_excel(f'hello{n}.xlsx')
    n = n + 1

print(total)
#df.reset_index(drop=True, inplace=True)
