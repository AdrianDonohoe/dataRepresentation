from github import Github
import requests

g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0")

repo = g.get_repo("datarepresentationstudent/aPrivateOne")

fileInfo = repo.get_contents("test.txt")
#print(fileInfo)
urlOfFile = fileInfo.download_url
#print (urlOfFile )

response = requests.get(urlOfFile)
contentOfFile = response.text

newContents = contentOfFile + " more stuff \n"

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents, fileInfo.sha)
print (gitHubResponse)