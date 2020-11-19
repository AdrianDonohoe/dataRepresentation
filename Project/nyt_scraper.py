import requests
from bs4 import BeautifulSoup
import csv

with open('us_states.csv', newline='') as f:
    reader = csv.reader(f)
    states = list(reader)

states_file = open('my_states.csv', mode='w')
states_writer = csv.writer(states_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for state in (states):
    votes = []
    page = requests.get("https://www.nytimes.com/interactive/2020/11/03/us/elections/results-" + state[1].lower().replace(' ','-') + "-president.html")
    print(page)

    soup1 = BeautifulSoup(page.content, 'html.parser')

    table = soup1.find("table")

    trump = table.findAll("tr", class_="e-donald-j-trump")
    biden = table.findAll("tr", class_="e-joseph-r-biden")

    trump = trump[0].find_all('span')
    biden = biden[0].find_all('span')

    trump_votes = trump[12].text
    votes.append(trump_votes)
    biden_votes = biden[10].text
    votes.append(biden_votes)

    electoral_votes = table.findAll("td", class_="e-ev")[0]
    electoral_votes = electoral_votes.find_all("span", class_="e-ev-display")
    electoral_votes = electoral_votes[0].text
    votes.append(electoral_votes)
    
    votes.append(state[1])
    votes.append(state[2])

    states_writer.writerow(votes)
states_file.close()
    

    