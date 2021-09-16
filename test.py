import requests
import json
import time
import polling

external_ip = "52.188.143.206"

# Sync
print("####################### SYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/syncAnalyze'

file = 'https://raw.githubusercontent.com/mdrakiburrahman/form-recognizer/main/artifacts/mortgage.pdf'
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         })

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))

# Async
print("####################### ASYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/analyze'

response = requests.post(endpoint, headers={"accept": "application/json", 
                        "Content-Type" : "application/json"},  
                        json={'url': file
                        })

print(response)
print(response.headers)

# Get Async response back
response_url = response.headers["Operation-Location"]
succeeded = 0

while succeeded != 1:
  response = requests.get(response_url)
  print(response.content)
  j = response.json() 
  
  print("Status: " + j["status"])
  
  if j["status"] == "succeeded":
    succeeded = 1

  time.sleep(5)