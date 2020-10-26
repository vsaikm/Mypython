import requests# to get the html file
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/', 'https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')#scrap the html ,there are diffeernet types of parsers in  the beautiful soup
#print(soup.find(id="score_22774839"))

links = soup.select('.storylink ')#scraping all the links in the site
subtext = soup.select('.subtext')
#print(votes[0].get("score_22774057"))

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k: k['vote'], reverse = True)

def create_custom_hn(links, subtext):
    hn= []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href' , None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 100:
                hn.append({'title': title , 'link' : href, 'vote' : points})#combinig both title and href
        #points = votes[idx].getText()
        #print(points)   

    return sort_stories_by_votes(hn)#we want to return nowly  the text none of the hml


pprint.pprint(create_custom_hn(links, subtext))


################################################################################################
#################################Learn scraping by using scrapy framework#######################
################################################################################################






