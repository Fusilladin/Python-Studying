import requests
from bs4 import BeautifulSoup
from collections import defaultdict
# import pandas as pd

url = "https://www.1mg.com/drugs-all-medicines"
res = requests.get(url)
print(res)
print(res.all)
