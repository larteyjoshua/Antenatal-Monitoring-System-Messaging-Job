from celery import Celery
from celery.utils.log import get_task_logger
from celery.schedules import crontab


celery = Celery(
    broker="pyamqp://guest@localhost//",
      include=['tasks']
    )

celery.conf.update(
    task_serializer='json',
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,  
)

celery_log = get_task_logger(__name__)


celery.conf.beat_schedule = {
    'sum_number': {
        'task': 'tasks.sum_number',
        'schedule': 30.0,
        'args': (16, 16)
    },
     'process_text_message': {
        'task': 'tasks.process_text_message',
        'schedule': 200.0,
    },
}
#crontab(minute=0,hour='11,12,13,14,15,16,17,18,19,20, 21, 22, 23, 0')
# if __name__ == '__main__':
#     celery.start()

#celery -A celeryWorker beat --loglevel=info
#celery -A celeryWorker worker -l info -P eventlet

#docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management