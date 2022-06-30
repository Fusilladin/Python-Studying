import csv
from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# starts things off

#####

# prints out the html text
print(soup.prettify())
match = soup.p.text  # only get the text of it
print(match)

#####

# finds the first footer class div of the html
match1 = soup.find('div', class_='footer')
print(match1)

# same for article
article = soup.find('div', class_='article')
print(article)

#####

# finds the first headline, anchor, then prints the text
headline = article.h2.a.text
print(headline)

# same foor summary
summary = article.p.text
print(summary)

#####

# For loop that prints all of the headlines and summaries and then leaves a space afterwards in the html page
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

#####

# pulls all the html from a webpage
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

#####

# gets all html for the first article
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

article = soup.find('article')
print(article.prettify())

#####

# prints out the first article headline form the html as text
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
headline = article.h2.a.text
print(headline)

#####

# prints out the summary for the headline because we looked up that the summary is within a 'div' class called entry-content
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

summary = article.find('div', class_='entry-content').p.text
print(summary)

#####

# the video is within the iframe section, pulls the html where the video link is, then shortens it to the src section only
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)

#####

# prints out the vid src and then splits each value by the / so you can read it easier to find the vid id or etc. You can count the index starting at 0.
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')
print(vid_id)

#####

# now that we found the index of the video id, we can add the index on the end the print out the vid id index only. The question mark (?) splits where the video url continues so, anything before that is apart of the vid id
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')[4]  # fourth index here
print(vid_id)

#####

# we now want to split the 4th index by another parameter, namely the question mark (?). So we just add in another line and split it at the 0 index
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

#####

# now that we have found the vid id we can take it and put it into an object and then put that object into a template url [for youtube in this example] and then we cna take that vid id to generate ana actual working yt_link
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

#####

# prints out the html's first article header, paragraph, and then the video id yt_link
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

headline = article.h2.a.text
print(headline)

summary = article.find('div', class_='entry-content').p.text
print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

#####

# in a for loop, prints out every single article headline with their paragraphs and also with their youtube video link if they have one in. ends with a spacer to seperate the text for readability. Indented to be inside the for loop

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    print()

#####

# for the error in the text where is says something like "Traceback (most recent call last):"" or "TypeError: 'NoneType' object is not subscriptable" you can add a try except block to remove that to keep it clean. cut/copy the video information into the try block

# try except block template:
try:
    pass
except Exception as e:
    raise e

# the youtube link variable will only go thru as long as the link is correct and succeeds at the yt_link = part
# many times will leave "pass" after the except clause
# if it fails we want to see that, so we set it to "None"
# print the yt_link variable outside of the try except block afterwards
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print()
# currently we are just printing this data out, but we can save it to a file like a csv

#####

# have to add the import csv part and the csv_file object and the writer clause for the csv
# then at the bottom inside the for loop add the writerow function for each parameter
# then on the bottom outside the for loop we need to close the file because we did not use a context manager

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('training_scrape1.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
