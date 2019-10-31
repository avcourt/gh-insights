import pandas
import os
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

user = 'avcourt'
key = os.environ.get('GH_API')

repos_url = f'https://api.github.com/users/{user}/repos'
repo_names = [repo["name"] for repo in requests.get(repos_url).json()]

insights = []
base_url = f'https://api.github.com/repos/{user}/'

print("Getting traffic insights for repos:")
for repo in repo_names:
    print(f"\t- github.com/{user}/{repo}/")
    repo_url = urljoin(base_url, repo + '/')
    traffic = requests.get(urljoin(repo_url, 'traffic/views'),
                           auth=HTTPBasicAuth('avcourt', key)).json()

    clones = requests.get(urljoin(repo_url, 'traffic/clones'),
                        auth=HTTPBasicAuth('avcourt', key)).json()["count"]

    insights.append({'repo': repo,
                     'views': traffic['count'],
                     'uniques': traffic['uniques'],
                     'clones': clones
                     })

print("\n-- STATS ------------------ Views / Clones --")
print("---------------------------------------------")
print(pandas.DataFrame(insights).to_string(index=False))
