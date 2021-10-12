import requests
response = requests.get(
    "https://api.todoist.com/rest/v1/projects",
    headers={
        "Authorization": "Bearer 0123456789abcdef0123456789"
    }).json()
print(response)