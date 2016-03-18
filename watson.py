import requests as r
from requests.auth import HTTPBasicAuth

UN = "USERNAME"
PW = "PASSWORD"
text = """
add the email text here
"""
print(r.get("https://gateway.watsonplatform.net/tone-analyzer-beta/api/v3/tone?version=2016-02-11&text={}".format(text),
                                                                                                                  auth=HTTPBasicAuth(UN, PW)).text)