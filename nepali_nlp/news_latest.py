from utils import top_news_link
from news_scrap import extract_news

class Update_news:
    def __init__:
        pass

    def show_latest(self, portal='onlinekhabar', number_of_news=5):
        assert portal in ['onlinekhabar','ekantipur'], "we currently support only ekantipur and onlinekhabar"
        extracted_link = top_news_link(portal=portal, top_n=number_of_news)
        summar_ = Summerize()
        for link_ in extract_news:
            title,text = extract_news(link)
            print(title)
            summary_news = summar_.show_summary(text,7)
            print(summary_news)
            print(' ')
        
        return 0
        