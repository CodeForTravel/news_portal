import logging
from django.conf import settings
from newsapi import NewsApiClient


logger = logging.getLogger(__name__)


class NewsApiData:
    def __init__(self) :
        self.NEWS_API_KEY = settings.NEWS_API_KEY
        self.news_api_client = NewsApiClient(api_key=self.NEWS_API_KEY)


    def fetch_sources(self):
        sources = self.news_api_client.get_sources()
        print("======================")
        print(sources)
        logger.info(f"fetching sources : {sources} ...")

        # TODO: create source with tasks


    def fetch_top_headlines(self):
        top_headlines = self.news_api_client.get_top_headlines()
        logger.info(f"fetching topheaders:{top_headlines} ...")

        # TODO: create source with tasks

    
    def fetch_article(self):
        all_articles = self.news_api_client.get_everything()
        logger.info(f"fetching articles:{all_articles} ...")
        # TODO: create article with and send notification with tasks


# from news_portal.apps.news.services import NewsApiData
# obj = NewsApiData()
# obj.fetch_sources()
# obj.fetch_top_headlines()
# obj.fetch_article()