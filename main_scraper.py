# Importing the required libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd



# Single page download
url = "http://fuseki.info/games_list.php?sb=full&id=M4335SG0"
currentPage = requests.get(url)

# Create BeautifulSoup Object
soup = BeautifulSoup(currentPage.content, 'lxml')

table = soup.find_all('table')
df = pd.read_html(str(table))

for row in soup.find('table',id="gameslist").find_all('tr'):
    print(' '.join([x.text for x in row.find_all('td')]))
    # Or just use '[x.text for x in row.find_all('td')]' in your data frame.