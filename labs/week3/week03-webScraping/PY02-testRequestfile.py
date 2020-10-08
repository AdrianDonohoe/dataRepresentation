from bs4 import BeautifulSoup

with open('../../week2/lab2.html') as fp:
    soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify)