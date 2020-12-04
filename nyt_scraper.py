# Created by Adrian Donohoe 19/11/2020
# This script scrapes the New York Times election website and writes the results to a csv (habits of a Data Analytics student, JSON would have better), which I later transform into JSON to use in the DB.


import requests
from bs4 import BeautifulSoup
import csv

# I used this file to compile a list of states. Seems it was missing Washington DC. Added manually later.
with open('us_states.csv', newline='') as f:
    reader = csv.reader(f)
    states = list(reader)

#file to write state information from NYT
states_file = open('my_states.csv', mode='w')
states_writer = csv.writer(states_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for state in (states):
    votes = []
    #URL for each state
    page = requests.get("https://www.nytimes.com/interactive/2020/11/03/us/elections/results-" + state[1].lower().replace(' ','-') + "-president.html")
    print(page)

    # This section navigates the page and extracts the required information and writes to the file
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
    trump_percent = trump[14].text
    votes.append(trump_percent)
    biden_percent = biden[11].find_all("span")[0].text
    votes.append(biden_percent)
    electoral_votes = table.findAll("td", class_="e-ev")[0]
    electoral_votes = electoral_votes.find_all("span", class_="e-ev-display")
    electoral_votes = electoral_votes[0].text
    votes.append(electoral_votes)
    votes.append(state[1])
    votes.append(state[2])
    states_writer.writerow(votes)
states_file.close()
    

    