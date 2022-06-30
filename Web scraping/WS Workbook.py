from requests_html import HTML, HTMLSession
# 1. https: // www.youtube.com/watch?v = a6fIbtFB46g
# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html=source)

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
