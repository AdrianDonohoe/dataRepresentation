import requests, json
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)

data = response.json()

#print(data)

filename = 'githubusers.json'

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('github followers')
row = 0
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
row += 1

for user in data:
    ws.write(row,0,user["login"])
    ws.write(row,1,user["id"])
    ws.write(row,2,user["node_id"])
    ws.write(row,3,user["avatar_url"])
    row += 1

w.save('users.xls')
