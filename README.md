***A short python script to see how many people are checking out your repositories.***

![Repo Traffic](traffic.gif)


## Dependencies
- Pandas: to print out a nice table
- requests

`$ pip3 install -r requirements.txt`

## Initial Setup
- Create a GitHub API [Personal Access Token]( https://github.com/settings/tokens) if you don't already have one.
- Set the `GH_API` environment variable from your shell:
  - `$ export GH_API=<your_access_key_here>`
- ... or hardcode yours as the `key` variable in `traffic.py`:
- Change `user` to your Github username in `traffic.py`

## Run
`$ python3 traffic.py`
