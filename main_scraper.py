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

# Get all rows and store them as lists in a list.
rows = [[x.text for x in row.find_all('td')] for row in table.find_all('tbody')]
#print(rows)

# Create the dataframe.
df = pd.DataFrame(rows, columns=titles)

df.head()