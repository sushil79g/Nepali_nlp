import sys
sys.path.append('..')

from .utils import top_news_link
from .news_scrap import extract_news
from .summerization import Summerize


class UpdateNews:
    def __init__(self):
        pass

    def show_latest(self, word_vec, portal='onlinekhabar', number_of_news=5):
        """his function returns tile of latest news, link for latest news and summerize news 
        
        Keyword Arguments:
            portal {str} -- [news portal sites; for now either 'onlinekhabar' or 'ekantipur'] (default: {'onlinekhabar'})
            number_of_news {int} -- [Number of top trending news] (default: {5})
        
        Returns:
            [tuple] -- [tuple of (titles, links, news_summerises)]
        """
        assert portal in ['onlinekhabar', 'ekantipur'], "we currently support only ekantipur and onlinekhabar"
        extracted_link = top_news_link(portal=portal, top_n=number_of_news)
        summary_ = Summerize()
        links = []
        titles = []
        news_summerises = []
        for link in extracted_link:
            title, text = extract_news(link)
            summary_news = summary_.show_summary(word_vec, text, length_sentence_predict=7)
            links.append(link)
            titles.append(title)
            news_summerises.append(summary_news)

        return (titles, links, news_summerises)
