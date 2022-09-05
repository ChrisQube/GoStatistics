# Importing the required libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Single page download
url = "http://fuseki.info/games_list.php?sb=full&id=M4335SG0"
currentPage = requests.get(url)

# Testing page response
# print(currentPage)

soup = BeautifulSoup(currentPage.content, 'html.parser')

currentTable = soup.find("table", id="gameslist")
tableRows = currentTable.tbody.find_all("td")
#tableElements = soup.find_all('table', id="gameslist")

# tableData = []
# for data in tableRows:
#     tableData.append(data)

print(tableRows)

# for child in soup.find_all('table', id="gameslist").children:
#     for td in child:
#         print(td)


# with open('GoStatistics/dummy website.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find('table',)
#     print(tags)



