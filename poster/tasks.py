import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_job, register_events

from core import settings
from poster.models import Poster

scheduler = BackgroundScheduler()


@register_job(scheduler, "interval", seconds=25)
def post_to_telegram():
    all_posts = Poster.objects.all()
    for post in all_posts:
        post_status = post.get_post_status()
        if  not post_status:
            print(post_status)
            telegram_bot_sendtext("hello world")


def telegram_bot_sendtext(bot_message):
    bot_token = settings.TELEGRAM.get('bot_token')
    bot_chatID = '759218619'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

scheduler.start()
print("Scheduler started!")