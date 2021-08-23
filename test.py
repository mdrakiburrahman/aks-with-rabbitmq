import requests
import json

external_ip = "40.88.53.141"

# Sync
print("####################### SYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/syncAnalyze?language=en&readingOrder=natural'

file = 'https://raw.githubusercontent.com/mdrakiburrahman/form-recognizer/main/artifacts/mortgage.pdf'
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         })

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))

# Async
print("####################### ASYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/Analyze?language=en&readingOrder=natural'

response = requests.post(endpoint, headers={"accept": "application/json", 
                        "Content-Type" : "application/json"},  
                        json={'url': file
                        })

print(response)
print(response.headers)
print(response.content)

# TODO Get Async response back