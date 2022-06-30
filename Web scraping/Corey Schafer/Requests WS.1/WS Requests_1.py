from requests_html import HTML, HTMLSession
from requests_html import HTML
# 1. https: // www.youtube.com/watch?v = a6fIbtFB46g

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

print(html.html)
# access the html from the object

#####

# print out the first title element
with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('title')
print(match[0])


#####

# find the first element within that search
with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('title', first=True)
print(match.text)

#####

# print the first article headline and summary
with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

article = html.find('div.article', first=True)
print(article.text)

#####

# print out the first headline and the first paragraph
article = html.find('div.article', first=True)
headline = article.find('h2', first=True)
summary = article.find('p', first=True)
print(headline)
print(summary)

#####

# adding .text shows the text of it instead of the html
article = html.find('div.article', first=True)
headline = article.find('h2', first=True).text
summary = article.find('p', first=True).text
print(headline)
print(summary)

#####

# this will get the headline and summary for every article
articles = html.find('div.article')
for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(headline)
    print(summary)
    print()

#####

# adding the import HTMLSession helps us get online requests
# prints out the html wensite url

session = HTMLSession()
r = session.get('https://coreyms.com/')

print(r.html)

#####

# all of the html from the first articles
# requests doesn't have a prettify function
session = HTMLSession()
r = session.get('https://coreyms.com/')

article = r.html.find('article', first=True)
print(article.html)

#####

# Now that we have pulled the html we can see the headline class tag and then we can use the find function to find the headline and then print it out from the html
session = HTMLSession()
r = session.get('https://coreyms.com/')

article = r.html.find('article', first=True)
# print(article.html)

headline = article.find('.entry-title', first=True).text
print(headline)

#####

# you have to still find in the article tag
# then you also have to add the p tagg at the end of the string in the fin function to be able to print the summary
# similar syntax to CSS
summary = article.find('.entry-content p', first=True).text
print(summary)

#####

# prints out the url and video id/link
vid_src = article.find('iframe', first=True)
print(vid_src.html)

#####

# getting the scr attr drops just the link alone
vid_src = article.find('iframe', first=True)
print(vid_src.attrs['src'])

#####

# this is the same as the prev one
vid_src = article.find('iframe', first=True).attrs['src']
print(vid_src)

#####

# break up the url by the delimiter /
# select the correct index [4]
vid_src = article.find('iframe', first=True).attrs['src']
vid_id = vid_src.split('/')[4]
print(vid_id)

#####

# split it on a 2nd delimiter ?
# get the correct index[0]
vid_src = article.find('iframe', first=True).attrs['src']
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

#####

# prints out the correct full url youtube link
vid_src = article.find('iframe', first=True).attrs['src']
vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)

#####

# change the article object name and then put all into a for loop and then we can get every single headline, summary, and yt link
session = HTMLSession()
r = session.get('https://coreyms.com/')

articles = r.html.find('article')

for article in articles:

    headline = article.find('.entry-title', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text
    print(summary)

    vid_src = article.find('iframe', first=True).attrs['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    print(vid_id)

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    print()
