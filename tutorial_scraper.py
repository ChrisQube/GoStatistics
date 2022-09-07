# Importing the required libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Downloading contents of the web page
url = "https://pt.wikipedia.org/wiki/Lista_de_bairros_de_Manaus"
data = requests.get(url).text

# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# Verifying tables and their classes
print('Classes of each table:')
for table in soup.find_all('table'):
    print(table.get('class'))

# Creating list with all tables
allTables = soup.find_all('table')

#  Looking for the table with the classes 'wikitable' and 'sortable'
table = soup.find('table', class_='wikitable sortable')


#### Defining of the dataframe
df = pd.DataFrame(columns=['Neighborhood', 'Zone', 'Area', 'Population', 'Density', 'Homes_count'])

# Collecting Ddata
for row in table.tbody.find_all('tr'):    
    # Find all data for each column
    columns = row.find_all('td')
    
    if(columns != []):
        neighborhood = columns[0].text.strip()
        zone = columns[1].text.strip()
        area = columns[2].span.contents[0].strip('&0.')
        population = columns[3].span.contents[0].strip('&0.')
        density = columns[4].span.contents[0].strip('&0.')
        homes_count = columns[5].span.contents[0].strip('&0.')

        #df = df.append({'Neighborhood': neighborhood,  'Zone': zone, 'Area': area, 'Population': population, 'Density': density, 'Homes_count': homes_count}, ignore_index=True)
        df = df.append([neighborhood, zone, area, population, density, homes_count], ignore_index=True)

df.head()