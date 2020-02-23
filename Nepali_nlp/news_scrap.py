import sys
sys.path.append('..')

import re
import urllib

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from newsplease import NewsPlease


def get_content_onlinekhabar(link):
    """This function extract the contants from onlinakhabar.com
    
    Arguments:
        link {string} -- [Link for onlinekhabar news]
    
    Returns:
        [string] -- [News content from the link]
    """
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage)
    text = ''
    for tex_ in soup.find_all("p")[:-1]:
        text = text + " " + tex_.getText()
    return ''.join(text)


def get_content_ekantipur(link):
    """This function helps in extracting the news from ekantipur.com
    
    Arguments:
        link {string} -- [News link from ekantipur site.]
    
    Raises:
        ValueError: [If unable to extract news from given link]
    
    Returns:
        [string] -- [News content from the link]
    """
    req = Request(link, headers={'User-Agent': 'mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage)

    try:
        for text_ in soup.find_all(attrs={'class': 'description'}):
            return text_.text[:text_.text.find('प्रकाशित ')]
    except:
        raise ValueError('Unable to extract from the link given.')


def extract_news(link):
    """This function extract news from given link.
    
    Arguments:
        link {string} -- [Link of news article.]
    
    Raises:
        ValueError: [Raise error if link is not for ekantipur/onlinekhabar]
    
    Returns:
        [tuple(title, sample_text)] -- [Title: Title of the news, sample_text: news article that has been extracted from the link given.]
    """
    if 'onlinekhabar.com' in link:
        sample_text = get_content_onlinekhabar(link)
    elif 'ekantipur.com' in link:
        sample_text = get_content_ekantipur(link)
    else:
        raise ValueError('Currently we work with onlinekhabar and ekantipur only. Other sites will be addedd soon.')

    article = NewsPlease.from_url(link)
    title = article.title

    return (title, sample_text)
