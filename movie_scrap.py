from googlesearch import search
from bs4 import BeautifulSoup
import requests
import os

# Get user input for the movie name
user_input = input("Please enter the name of the movie: ")
print(user_input)

# Define the query to search for
query = "{} rotten tomatoes".format(user_input)

# Perform the search and iterate through the results
first_tab = []
for j, result in enumerate(search(query, num_results=10)):
    first_tab.append(result)

# Get the first search result URL
url = first_tab[0]
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
div_element = soup.find('div', class_='media-scorecard no-border')

# Extract and print the Rotten Tomatoes rating
critic_element_a = div_element.find('rt-text')
text_ = critic_element_a.get_text()
print("Rotten Tomatoes rating is {}".format(text_))

# Extract and print the content summary
content_element = div_element.find('rt-text', slot='content')
print(content_element.get_text().strip())

# Extract and print the movie duration
div_element_dur = soup.find('div', class_='media-hero-wrap')
time_element = div_element_dur.find_all('rt-text', slot="metadataProp")[-1]
#time_element =  div_element_dur.find('rt-text', slot='duration')
print("Duration is {}".format(time_element.get_text()))
