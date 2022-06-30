import requests
from bs4 import BeautifulSoup

topics_url = 'https://github.com/topics'  # create a object for the website
response = requests.get(topics_url)  # using the requests to get the url

#####

print(len(response.text))  # print how many char in the webpage

#####

page_contents = response.text  # object for url text
print(page_contents[:100])  # printing out a portion of the page


#####

with open('webpage.html', 'w') as f:
    f.write(page_contents[:3900])
    # doing it once creates a blank file
    # doing it twice put that webpage text into the file

    # changing the number rewrites the entire file

#####

doc = BeautifulSoup(page_contents, 'html.parser')
type(doc)
# print(doc) # pulls the page into

#####

topic_title_tags = doc.find_all('p')
print(len(topic_title_tags))  # finds all of the p
# print(topic_title_tags[:5]) # find the first few to see it is the correct tag
print(topic_title_tags[:1])

#####

# right clock the inspected part and put it here
desc_selector = 'f5 color-text-secondary mb-0 mt-1'
topic_desc_tags = doc.find_all('p', {'class': desc_selector})

print(topic_desc_tags[:5])  # prints out the desc

#####
