import requests
import plotly.express as px

# API URL
url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars:>10000"

# Get the requests
headers={"Accept": "application/vnd.github.v3+json"}
r=requests.get(url,headers)
print(f"Status code: {r.status_code}")

# Handle the response
response_dict=r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Analyze the stars of the repos
repo_dicts=response_dict["items"]
repo_links,repo_stars,hover_texts=[],[],[]
for repo_dict in repo_dicts:
    repo_name=repo_dict["name"]
    repo_url=repo_dict["html_url"]
    repo_link=f"<a href='{repo_url}>{repo_name}</a>"
    repo_links.append(repo_link)
    repo_stars.append(repo_dict["stargazers_count"])

    # Create hover texts
    owner=repo_dict["owner"]["login"]
    description=repo_dict["description"]
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Visualize

# Set the title and labels
title="Most-starred Python projects on GitHub"
labels={'x':"Repo", 'y':"Stars"}


# Show
fig=px.bar(x=repo_links,y=repo_stars,
    title=title,labels=labels,
    hover_name=hover_texts)

fig.update_layout(title_font_size=28, 
    xaxis_title_font_size=20,
    yaxis_title_font_size=20)

fig.update_traces(marker_color="SteelBlue",marker_opacity=0.6)

fig.show()