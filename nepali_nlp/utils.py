import re
import urllib

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def load_multiple_link_dataset(file_loc = 'nep-eng.txt'):
    with open(file_loc,'r') as fp:
        file_content = []
        file_ = fp.read().splitlines()

        for ind,item in enumerate(file_):
            if item:
                if not item.isspace():
                    file_content.append(item)

    file_content[0] = 'aba'
    unicode_ = []; preeti=[]; pos=[]; meaning=[]
    c = 0
    for ind, item in enumerate(file_content):
        if c==0:
            unicode_.append(item)
            c = c + 1
        elif c==1:
            preeti.append(item)
            c = c + 1
        elif c==2:
            pos.append(item)
            c = c + 1
        else:
            meaning.append(item)
            c = 0
    
    return unicode_,preeti,pos,meaning


def top_news_link(portal='onlinekhabar',top_n =5):
    """This function fetch the top_n trending news
    
    Keyword Arguments:
        portal {str} -- [news portal that you want to see trending of] (default: {'onlinekhabar'})
        top_n {int} -- [number of top trending news] (default: {5})
    
    Returns:
        [list] -- [links of trending news]
    """
    assert portal in ['onlinekhabar','ekantipur'], "Currently we support 'onlinekhabar' and 'ekantipur' only"
    links = []
    req = Request('https://www.' + portal +'.com/', headers={'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage)
    if portal=='onlinekhabar':
        for link in soup.find_all('a', href=True):
            if 'https://www.onlinekhabar.com' in link['href']:
                try:
                    link_ = link['href'][-14:].replace('/','')
                    int(link_)
                    links.append(link['href'])
                except:
                    pass
        return links[:top_n]
    
    for link in soup.find_all('a', href=True):
        if 'https://ekantipur.com' in link['href']:
            try:
                int(link['href'][-34:][0:-5].replace('/',''))
                links.append(link['href'])
            except:
                pass

    return links[:top_n]
