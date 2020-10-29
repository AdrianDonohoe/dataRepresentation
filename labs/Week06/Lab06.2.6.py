import requests, json

## apiKey removed


url = 'https://api.github.com/users/datarepresentationstudent/repos'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
#print(repoJSON)

file = open('repos.json', 'w')
json.dump(repoJSON, file, indent=4)