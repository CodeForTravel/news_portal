import logging
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import get_user_model
from newsapi import NewsApiClient
from news_portal.apps.news import models as models_news
from news_portal.apps.news import send_grid

User = get_user_model()
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
        for headline_dict in headlines_list:
            author =  headline_dict.get("author")
            title =  headline_dict.get("title")
            description =  headline_dict.get("description")
            url =  headline_dict.get("url")
            urlToImage =  headline_dict.get("urlToImage")
            publishedAt =  headline_dict.get("publishedAt")
            content =  headline_dict.get("content")

            headline_obj, created = models_news.TopHeadline.objects.get_or_create(content=content,publishedAt=publishedAt,urlToImage=urlToImage,url=url,description=description,author=author,title=title)

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
        self.send_news_notification()

    def send_news_notification(self):
        newly_created_headline = models_news.TopHeadline.objects.filter(is_notified=False)
        user_list = User.objects.all()
        for user in user_list:
            q = Q()
            for _keyword in user.news_keywords:
                q |= Q(title__icontains = _keyword)
                q |= Q(description__icontains = _keyword)

            filter_dict = {}
            country_of_news = [s.lower() for s in user.country_of_news]
            if country_of_news:
                filter_dict["source__country__in"] = country_of_news

            if user.news_sources.all():
                filter_dict["source__in"] = user.news_sources.all()

            if filter_dict:
                newly_created_headline = newly_created_headline.filter(**filter_dict)

            filtered_news = newly_created_headline.filter(q)
         # TODO: update the is_notified to true after test (newly_created_headline) 

            if filtered_news:
                self.send_notification(user, filtered_news)

    def send_notification(self, user, filtered_news):
        message_header = f"Hello {user.username}, there are some important news you might be interested!\n"
        message_body = ""
        for news in filtered_news:
            message_body = f"{message_body}{news.title}\n\n"
        send_grid.send_mail(user, message_header, message_body)        
            

    
# from news_portal.apps.news.services import NewsApiData
# obj = NewsApiData()
# obj.fetch_top_headlines()