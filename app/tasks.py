from app.celeryWorker import celery
import time
from app.helpers import arkeselTextMessage
from loguru import logger


@celery.task(name='tasks.sum_number')
def sum_number(x, y):
    add = x + y
    logger.info("I am suppose to run")
    return add


@celery.task(name='tasks.send_text_message')
def send_text_message(sender: str, message: str, phone_numbers):
    time.sleep(5)
    logger.info("Sending Text Message to Expected Mother")
    sendMessage = arkeselTextMessage.sendSMS(sender, message, phone_numbers)
    return sendMessage


@celery.task(name='tasks.send_voice_message')
def send_voice_message(phone_numbers: str):
    time.sleep(5)
    logger.info("Sending Voice Message to Expected Mother")
    sendMessage = arkeselTextMessage.sendVoiceSMS(phone_numbers)
    return sendMessage
