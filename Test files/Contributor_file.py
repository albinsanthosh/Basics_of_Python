import requests
import pandas as pd

company_repo = input('Enter the Company/repo:')
personal_token = 'Personal access token'

df = pd.DataFrame()
n = 1
while requests.get(f'https://api.github.com/repos/{company_repo}/contributors?page={n}&per_page=100&access_token={personal_token}').json():
    info_url = f'https://api.github.com/repos/{company_repo}/contributors?page={n}&per_page=100&access_token={personal_token}'
    contri_info = requests.get(info_url).json()
    print(len(contri_info))
    dm = pd.DataFrame(contri_info)
    df = pd.concat([df, dm], ignore_index=True)
    n = n + 1

df.to_excel(f'contributors.xlsx')


