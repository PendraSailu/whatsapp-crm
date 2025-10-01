import requests

url = "http://127.0.0.1:8000/messages/generate-message"
data = {"prompt": "create a diwali wish"}

response = requests.post(url, json=data)
print(response.json())
