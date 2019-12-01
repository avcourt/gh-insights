***A short Python script to see how many people are checking out your repositories.***

![Repo Traffic](screenshot.gif)


## Dependencies
- Pandas: to print out a nice table
- requests

`$ pip3 install -r requirements.txt`

## Initial Setup
- Create a GitHub API [Personal Access Token](
  https://github.com/settings/tokens) if you don't already have one. Needs only
  the 'admin:public_repo' permission.
- Set the `GH_API` environment variable from your shell:
  ```bash
  $ export GH_API=<your_access_key_here>
  ```
- Set the `GH_USER` environment variable from your shell:
  ```bash
  $ export GH_USER=<your username>
  ```

## Run
If you've set the above environment vars:
```bash
$ python3 traffic.py`
```

or pass them in via the command-line:
```bash
$ GH_API=xxx GH_USER=avcourt python3 traffic.py
```
