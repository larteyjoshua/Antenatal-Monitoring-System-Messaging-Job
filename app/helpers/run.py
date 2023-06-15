from celery.apps.beat import Beat
from celeryWorker import celery

from celery.bin import worker

# b = Beat(app=celery, loglevel='info')
# b.run()



if __name__ == '__main__':
   
    w = worker.worker(app=celery)

    options = {
        'loglevel': 'INFO',
        'traceback': True,
    }

    w.run(**options)