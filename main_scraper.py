# Importing the required libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Single page download
url = "http://fuseki.info/games_list.php?sb=full&id=M4335SG0"
currentPage = requests.get(url)

# Create BeautifulSoup Object
soup = BeautifulSoup(currentPage.content, 'lxml')

table = soup.find('table', id='gameslist')

# Get all the column titles.
titles = [x.text for x in table.find('thead').find_all('td')]
#print(titles)

df = pd.DataFrame(columns=titles)

# Get list of each URL from file
filePath = "C:/Users/Chris/Documents/GitHub/GoStatistics/Database sample.txt"
with open(filePath, 'r') as file:
    lines = file.readlines()
    urls = [line.rstrip() for line in lines]

# For each URL in list capture the table --> rows
for url in urls:
    currentPage = requests.get(url)
    soup = BeautifulSoup(currentPage.content, 'lxml')
    table = soup.find('table', id='gameslist')
    # Get all rows and store them as lists in a list.
    rows = [[x.text for x in row.find_all('td')] for row in table.find('tbody').find_all('tr')]
    # Append rows to the dataframe: df = pd.concat(df, pd.DataFrame(rows, columns=titles))
    df = pd.concat(df, pd.DataFrame(rows, columns=titles))

# close file
file.close()

df.head()

# Export csv