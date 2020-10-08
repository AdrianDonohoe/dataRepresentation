from bs4 import BeautifulSoup
import csv

with open('../../week2/lab2.html') as fp:
    soup = BeautifulSoup(fp,'html.parser')

#print(soup.tr)

employee_file = open('employee_file.csv',mode='w')
employee_writer = csv.writer(employee_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll('tr')

for row in rows:
    dataList = []
    #print(row)
    cols = row.findAll('td')
    for col in cols:
        if (col.text != 'update' and col.text != 'delete'):
            dataList.append(col.text)
    employee_writer.writerow(dataList)

employee_file.close()