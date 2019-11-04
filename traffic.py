#!/usr/bin/env python3

import os
from urllib.parse import urljoin

import pandas
import requests
from requests.auth import HTTPBasicAuth


def main():
    """Main cli"""

    # check for user/key environment variables, uses 2nd param if none found
    user = os.environ.get("GH_USER", "avcourt")  # your github username
    key = os.environ.get("GH_API", "yourkey")  # your secret access token

    repos_url = f"https://api.github.com/users/{user}/repos"
    repo_names = [repo["name"] for repo in requests.get(repos_url).json()]

    insights = []
    base_url = f"https://api.github.com/repos/{user}/"

    print("Getting traffic insights for repos:")
    for repo in repo_names:
        print(f"\t- github.com/{user}/{repo}/")
        repo_url = urljoin(base_url, repo + "/")
        traffic = requests.get(
            urljoin(repo_url, "traffic/views"), auth=HTTPBasicAuth(user, key)
        ).json()

        clones = requests.get(
            urljoin(repo_url, "traffic/clones"), auth=HTTPBasicAuth(user, key)
        ).json()["count"]

        insights.append(
            {
                "repo": repo,
                "views": traffic["count"],
                "uniques": traffic["uniques"],
                "clones": clones,
            }
        )

    print("\n-- INSIGHTS --------------- Views / Clones --")
    print("---------------------------------------------")
    print(pandas.DataFrame(insights).to_string(index=False))


if __name__ == "__main__":
    main()
