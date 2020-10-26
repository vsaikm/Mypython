#download beautiful soup
'''
If you don't have it on your computer already.
Again we just use it using requests.
It essentially allows us to grab a CML files like Hacker News.
'''
import requests# to get the html file
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
#print(res.text)
'''Hacker News at least on the page that we requested and we saw
here that we received all this HMO information which is great.
This is just a string that we received.
What beautiful soup allows us to do is to do something called Pass.
That is we can use beautiful soup to convert this from a string to an actual object that we can manipulate
and use using Python to modify this data to what we want.
'''
soup = BeautifulSoup(res.text,'html.parser')#scrap the html ,there are diffeernet types of parsers in  the beautiful soup
print(soup.find_all('a'))

