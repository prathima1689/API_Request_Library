import requests

base_url = "https://simple-tool-rental-api.glitch.me"

# Get request:

response = requests.get(base_url+"/status")
print(response.status_code)
print(response.json())

# Get tools:

response= requests.get(base_url+"/tools")
print(response.status_code)
print(response.json())




