import requests
import json
import time

external_ip = "20.85.171.201"

# Start time
start_time = time.time()

# Sync
print("####################### SYNC #######################")

endpoint = 'http://'+ external_ip +':5000/vision/v3.2/read/syncAnalyze'

# file = 'https://raw.githubusercontent.com/mdrakiburrahman/cognitive-services-k8s/main/test-files/mortgage.pdf' # 2 pages
file = 'https://raw.githubusercontent.com/mdrakiburrahman/cognitive-services-k8s/main/test-files/go-book-20.pdf' # 20 pages
response = requests.post(endpoint, \
                         headers={'accept': 'application/json'
                         , 'Content-Type': 'application/json'},
                         json={'url': file
                         })

print(json.dumps(json.loads(response.content), indent=4, sort_keys=True))

# Print difference in time
end_time = time.time()
print("Time taken: ", end_time - start_time)

# Async
print("####################### ASYNC #######################")

# Start time
start_time = time.time()
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
failed = 0

while (succeeded != 1) and (failed != 1):
  response = requests.get(response_url)
  j = response.json() 
  print("Status: " + j["status"])
  
  if j["status"] == "succeeded":
    succeeded = 1
    print("Done!")
  elif j["status"] == "failed":
    failed = 1
    print("Try again :(")
  else:
    time.sleep(1)

# End time
end_time = time.time()

# Print content
print(response.content)

# Print number of characters in response
print("\nLength of response:" + str(len(response.content)))

# Save response to file
filename = "response_" + str(time.time()) + ".json"
with open("inference/{}".format(filename), "w") as outfile:
  json.dump(json.loads(response.content), outfile, indent=4, sort_keys=True)

# Print difference in time
print("Time taken: ", end_time - start_time)