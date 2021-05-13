import requests

url = "https://sskgimnq5h.execute-api.us-east-2.amazonaws.com/Test/buckets"

body = {
    "name": "Test2"
}

#response = requests.post(url, json=body)
response = requests.get(url)

print(response.text)