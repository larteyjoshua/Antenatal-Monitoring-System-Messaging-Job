from celeryWorker import celery, celery_log
import time
import json
from json import JSONEncoder
from sqlalchemy.orm import Session
from helpers import arkeselTextMessage
import processTextMessage

@celery.task(name ='tasks.sum_number')
def sum_number(x, y):
    add = x + y
    celery_log.info("I am suppose to run")
    return add

@celery.task(name ='tasks.process_today_message')
def process_today_message():
    processTextMessage.processingTodayTextMessaging()
   
    return {"message": "Processing Text Messaging"}

@celery.task(name ='tasks.process_one_day_message')
def process_one_day_message():
    processTextMessage.processingDayBeforeTextMessaging()
   
    return {"message": "Processing Text Messaging"}

@celery.task(name ='tasks.send_text_message')
def send_text_message(sender: str, message: str, phone_numbers):
    time.sleep(5)
    celery_log.info("Sending Text Message to Expected Mother")
    sendMessage = arkeselTextMessage.sendSMS(sender, message, phone_numbers)
    return sendMessage





