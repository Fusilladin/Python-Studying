import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')
years = list(range(1991, 2022))
# print(years)
url_start = 'https://www.basketball-reference.com/awards/awards_{}.html'
# print(url)

for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    with open('mvp/{}.html'.format(year), "w+") as f:
        f.write(data.text)
# print(url)
# print(data)

soup.find('tr', class_='over_header').decompose()
soup.find_all(id='all_mvp')

mvp_1991 = pd.read_html(str(mvp_table))
