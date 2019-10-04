import requests
from bs4 import BeautifulSoup
import sys


if len(sys.argv) != 2 :
  print("Example Usage:python web_info.py https://www.google.com")
  sys.exit (1)
else :
  url = sys.argv[1]	
  html = requests.get(url).text
  bs = BeautifulSoup(html,"html.parser")
  possible_links = bs.find_all('a')
  for link in possible_links:
    if link.has_attr('href'):
      print(link.attrs['href'])