import pychaterr

import requests


response = requests.get("https://run.mocky.io/v3/4044c77a-b473-456d-a6ec-83c5a52871ac", json={})
response.raise_for_status()
