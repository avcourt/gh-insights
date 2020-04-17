***A short Python script to see how many people are checking out your repositories.***

![Repo Traffic](screenshot.gif)


## Dependencies

- python3.6 for f-strings 
- requests

`$ pip3 install -r requirements.txt`

OR:

`$ pip3 install requests`

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
  ***Note:** If `GH_USER` or `GH_API` is not found (either in your environment or in `ghinsights` source itself), you will be prompted for them at the console upon running `ghinsights`.*

## Run

You have several options for how you'd like to set your credentials:
  - through env vars
  - passing them in as args to `ghinsights`
  - hardcoding them in the python source
  - do none of the above and enter them when prompted
  
If you've set the above environment vars:
```bash
$ ./ghinsights
```
or pass them in via the command-line:
```bash
$ GH_API=xyourxsecretxapixkeyx GH_USER=avcourt python3 ghinsights
```  
or hardcode them in `ghinsights` source (careful not expose these to the public!):
```python
GH_USERNAME = ""  # your github username
GH_API_TOKEN = ""  # your github api token <https://github.com/settings/tokens>
```
or pass them in when prompted:
```bash
$ ./ghinsights
```
