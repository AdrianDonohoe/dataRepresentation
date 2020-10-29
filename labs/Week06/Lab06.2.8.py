import requests, json

## removed apiKey 

url = 'https://api.github.com/user/repos'


data = { "name": "Hello" }
#data = { "name": "Hello-World", "description": "This is your first repository", "homepage": "https://github.com", "private": "false", "has_issues": "true", "has_projects": "true", "has_wiki": "true"}
response = requests.post(url, auth=('token', apiKey), json=data)


print(response.status_code)
print(response.json())
