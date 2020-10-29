import requests, json

f = open('../week2/lab2.html', 'r')
html = f.read()
#print(html)

# removed apiKey
url = 'https://api.html2pdf.app/v1/generate'

data = {'html' : html, 'apiKey': apiKey }

response = requests.post(url, json=data)
print(response.status_code)

newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)