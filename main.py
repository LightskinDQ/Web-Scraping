"""

Imported a url from a wikipedia page and organized web scrapped the data into a table using a dataframe

"""
# Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
#adjusting the display limitations in python allowing us to visualize the whole table
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#Variables
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


table = soup.find_all("table")[1]
world_titles = table.find_all("th")
world_table_titles = [title.text.strip() for title in world_titles]
df = pd.DataFrame(columns = world_table_titles)
column_data = table.find_all("tr")

#looping through the columnn data starting at position 1 because position 0 is an empty list
for row in column_data[1:]:
    row_data = row.find_all('td')#tag to find the individual data
    individual_row_data = [data.text.strip() for data in row_data]#strips /n to make it look clean
    #checks the length of the data frame and move it to the next position appending it to the data frame itself
    length = len(df)
    df.loc[length] = individual_row_data

print (df.to_string(index=False))

    