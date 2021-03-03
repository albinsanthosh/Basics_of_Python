import requests

personal_token = '1Personal Access Token'
url = f"https://api.github.com/repos/hashicorp/consul/contributors?access_token={personal_token}"
response = requests.get(url)
data = response.json()
print(data)
for item in data:
    name = item["login"]
    commits = item["contributions"]
    org_url = item["organizations_url"]
    print(name, commits)
    org_response = requests.get(org_url + f"?access_token={personal_token}").json()
    for item1 in org_response:
        org_name = item1["login"]
        if org_name == []:
            org_name = name
        print(org_name)