***A short Python script to see how many people are checking out your repositories.***

![Repo Traffic](screenshot.gif)


## Dependencies
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
  **Note:** If `GH_USER` or `GH_API` is not found (either in your environment or in `ghinsights` source itself), you will be prompted for them at the console upon running `ghinsights`.

## Run
If you've set the above environment vars:
```bash
$ ./ghinsights`
```
or pass them in via the command-line:
```bash
$ GH_API=xyourxsecretxapixkeyx GH_USER=avcourt python3 ghinsights
```
or pass them in when prompted:
`$ ./ghinsights`
