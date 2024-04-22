import requests

# Get API URL
url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"

# Get the requests
headers={"Accept":"application/vnd.github.v3+json"}
r=requests.get(url,headers=headers)
print(f"status code: {r.status_code}")

# Transfer the response into a dict
response_dict=r.json()

# Total repos
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts=response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Let's dive into some repos
print("Selected info about each repo:")
for repo_dict in repo_dicts:
    # print(f"Keys: {len(repo_dict)}")
    # for key in sorted(repo_dicts[0].keys()):
    #     print(key)
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repo URL: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print()