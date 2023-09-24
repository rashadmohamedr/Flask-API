import requests
from bs4 import BeautifulSoup
from lxml import etree
from rich import print

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
    link=newscards[5].a['href']
    image_src=newscards[5].a.img['src']
    title=newscards[5].h3.text
    time=newscards[5].time.text
    logo_src='https://1000logos.net/wp-content/uploads/2017/06/Reuters-Logo-500x333.png'

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
