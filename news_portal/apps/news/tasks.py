import logging
from huey.contrib.djhuey import periodic_task, task
from huey import crontab, RedisHuey
from news_portal.apps.news import services


logger = logging.getLogger("task_logger")


@periodic_task(crontab(minute="*/7"))
def task_fetch_news_headline():
    logger.info("[task_fetch_news_headline] Executing ...")

    try:
        service_obj =  services.NewsApiData()
        service_obj.fetch_top_headlines()
    except Exception as e:
        logger.exception(e)
        logger.info("[task_fetch_news_headline] Executed - Failed")

    logger.info("[task_fetch_news_headline] Executed - Successful")


@periodic_task(crontab(hour="*/24"))
def task_fetch_news_sources():
    logger.info("[task_fetch_news_sources] Executing ...")

    try:
        service_obj =  services.NewsApiData()
        service_obj.fetch_sources()
    except Exception as e:
        logger.exception(e)
        logger.info("[task_fetch_news_sources] Executed - Failed")

    logger.info("[task_fetch_news_sources] Executed - Successful")
    

@task()
def task_send_news_notification():
    logger.info("[task_send_news_notification] Executing ...")

    try:
        service_obj =  services.NewsApiData()
        service_obj.send_news_notification()()
    except Exception as e:
        logger.exception(e)
        logger.info("[task_send_news_notification] Executed - Failed")

    logger.info("[task_send_news_notification] Executed - Successful")


