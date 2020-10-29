import requests, json

apiKey = '160244469f8c71bdf7211cdb20499d3cfb6dfa54'


url = 'https://api.github.com/users/AdrianDonohoe/repos'

response = requests.get(url, auth=('token', apiKey))

repoJSON = response.json()
print(repoJSON)

#file = open('repos.json', 'w')
#json.dump(repoJSON, file, indent=4)