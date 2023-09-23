import requests
from bs4 import BeautifulSoup
from lxml import etree

newsJSON = {}

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

def scrapeReuters(url):
    url = 'https://www.reuters.com/'+url+'/'
    response=requests.get(url,headers=HEADERS)
    responseSoup=BeautifulSoup(response.content, 'html.parser')
    responseDom=etree.HTML(str(responseSoup))
    newscards=responseSoup.find_all('div', {"data-testid":"MediaStoryCard"})
    #print(responseDom.xpath("//*[@class='media-story-card__playlist__2ESDd story-card']"))


def scrapeCNN(url):
    url = 'https://edition.cnn.com/'+url+'/'


def scrapeNews():
    reutersURLs = ['world',]
                #    'sports',
                #    'technology',
                #    'markets']
    for i in reutersURLs:
        scrapeReuters(i)

    cnnURLs = ['entertainment']
    for i in cnnURLs:
        scrapeCNN(i)
    return newsJSON


if __name__ == "__main__":
    scrapeNews()
