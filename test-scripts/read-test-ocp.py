import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

external_ip = "https://raki-cognitive-read.apps.ocp-env.your-route.com"

# Sync
print("####################### SYNC #######################")

endpoint = external_ip +'/vision/v3.2/read/syncAnalyze'

file = 'https://raw.githubusercontent.com/mdrakiburrahman/form-recognizer/main/artifacts/mortgage.pdf'
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         },
                         verify=False)

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))

# Async
print("####################### ASYNC #######################")

endpoint = external_ip +'/vision/v3.2/read/analyze'

response = requests.post(endpoint, headers={"accept": "application/json", 
                        "Content-Type" : "application/json"},  
                        json={'url': file
                        },
                        verify=False)

print(response)
print(response.headers)

# Get Async response back
response_url = response.headers["Operation-Location"].replace('http', 'https')
succeeded = 0

while succeeded != 1:
  response = requests.get(response_url, verify=False)
  print(response.content)
  j = response.json() 
  
  print("Status: " + j["status"])
  
  if j["status"] == "succeeded":
    succeeded = 1

  time.sleep(5)