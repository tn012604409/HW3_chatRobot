import requests
import time
from bs4 import BeautifulSoup


def get_web_page(url):
    resp = requests.get(
        url=url,
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom):
    soup = BeautifulSoup(dom, 'html.parser')
    tag = soup.find_all('a','recipe-name')
    articles=tag
               
    return articles


def run():
    page = get_web_page('https://icook.tw/recipes/popular?ref=icook-footer')
    if page:
        current_articles = get_articles(page)
        i=1
        s=''
        for post in current_articles:   
            temp=str(post)
            num=int(temp.find("\" href="))
            #print('The Number {0}: {1}'.format(i, temp[35:num]))
            s=s+'The Number {0}: {1}\n'.format(i, temp[35:num])
            i=i+1
    return s
            
