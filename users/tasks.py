from celery import shared_task
# import requests

from project15.celery import celery_app


@celery_app.task(
    name='send_sms',
    bind=True,
    default_retry_delay=5,
    max_retries=1,
    acks_late=True
)
def send_sms(self, phone, otp):
    phone_num = str(phone)
    url = '' + phone_num + '&text=' + otp + ''
    # requests.get(url)
    print('===== SENT SMS ====', phone, otp, '=====')