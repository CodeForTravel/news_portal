import logging
from django.conf import settings
from newsapi import NewsApiClient
from news_portal.apps.news import models as models_news

logger = logging.getLogger(__name__)


class NewsApiData:
    def __init__(self) :
        self.NEWS_API_KEY = settings.NEWS_API_KEY
        self.news_api_client = NewsApiClient(self.NEWS_API_KEY)


    def fetch_sources(self):
        logger.info(f"fetching sources ...")
        sources_response = self.news_api_client.get_sources()
        if sources_response.get("status") == 'ok':
            self.create_source(sources_response.get("sources"))
            


    def fetch_top_headlines(self):
        response_headlines = self.news_api_client.get_top_headlines()
        logger.info(f"fetching topheaders:{response_headlines} ...")
        if response_headlines.get("status") == 'ok':
            self.create_headlines(response_headlines.get("articles"))

    def create_source(self, sources_list):
        for source_dict in sources_list:
            source_id = source_dict.get("id")
            name =  source_dict.get("name")
            description =  source_dict.get("description")
            url =  source_dict.get("url")
            category =  source_dict.get("category")
            language =  source_dict.get("language")
            country =  source_dict.get("country")
            source_obj, created = models_news.Source.objects.get_or_create(source_id=source_id,name=name,description=description,url=url,category=category,language= language,country=country)

    def create_headlines(self, headlines_list):
        newly_created_headline = []
        for headline_dict in headlines_list:
            author =  headline_dict.get("author")
            title =  headline_dict.get("title")
            description =  headline_dict.get("description")
            url =  headline_dict.get("url")
            urlToImage =  headline_dict.get("urlToImage")
            publishedAt =  headline_dict.get("publishedAt")
            content =  headline_dict.get("content")

            headline_obj, created = models_news.TopHeadline.objects.get_or_create(content=content,publishedAt=publishedAt,urlToImage=urlToImage,url=url,description=description,author=author,title=title)
            if created:
                newly_created_headline.append(headline_obj)

            source_name = headline_dict.get("source").get("name")
            source_id = headline_dict.get("source").get("id")
            if source_id:
                source_qs = models_news.Source.objects.filter(name=source_name,source_id=source_id)
            else:
                source_qs = models_news.Source.objects.filter(name=source_name)
            if source_qs:
                source_obj = source_qs.first()
                headline_obj.source = source_obj
                headline_obj.save()

        if newly_created_headline:

            self.send_notification(newly_created_headline)

    def send_notification(self, newly_created_headline):
        # send notification based on keywords
        pass

        


            

            

            

