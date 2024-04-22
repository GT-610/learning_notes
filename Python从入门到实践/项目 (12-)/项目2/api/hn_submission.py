from operator import itemgetter
import requests
import plotly.express as px

# Get the API response
url="https://hacker-news.firebaseio.com/v0/topstories.json"
r=requests.get(url)
print(f"Status code: {r.status_code}")

# Handle every article's information
submission_ids=r.json()
submission_dicts=[]
for submission_id in submission_ids[:30]:
    # Call the API for every article listed in the topstories.json
    url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r=requests.get(url)
    print(f"Status code for {submission_id}: {r.status_code}")
    response_dict=r.json()

    # Create a dict for every article
    try:
        submission_dict={
            'title':response_dict['title'],
            'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict['descendants'],
        }
    except KeyError:
        print(f"The article {submission_id} forbids comments. Skipped.")
    submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

titles,comments=[],[]
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    comments.append(submission_dict['comments'])

# Visualize

# Set the title
title="Most commented articles on Hacker News"
labels={'x':"Article",'y':"Comments"}

# Show
fig=px.bar(
    x=titles,y=comments,
    title=title,labels=labels
)

fig.update_layout(title_font_size=28, 
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)

fig.update_traces(marker_color="SteelBlue",marker_opacity=0.6)

fig.show()

