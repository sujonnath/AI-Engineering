# API Call
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
print("\n")
print(response.text)
print("\n")
print(response.status_code)

url ="https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Learn APIs",
    "body": "POST example with requests",
    "userId":1
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())


# API
params = {'userId':1}
response = requests.get("https://jsonplaceholder.typicode.com/posts",params=params)
print(response.json())
print(response.text)
