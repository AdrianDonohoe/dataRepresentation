import requests, json

# removed apiKey


url = 'https://api.github.com/users/AdrianDonohoe/repos'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
print(repoJSON)

#file = open('repos.json', 'w')
#json.dump(repoJSON, file, indent=4)