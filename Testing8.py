from github import Github
personal_token = 'Personal Access Token'
# First create a Github instance using an access token
g = Github(personal_token)

s_repo = g.get_repo("Hashicorp/consul")
# Then play with your Github objects:

#for repo in g.get_user().get_repos():
#    print(repo)
for commit in s_repo.get_commits():
    print(commit.author.company,commit.commit.author.date)