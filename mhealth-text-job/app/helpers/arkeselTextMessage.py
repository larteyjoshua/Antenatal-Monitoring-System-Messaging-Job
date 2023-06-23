import requests
from app.utils.config import settings
import json
from loguru import logger


def sendSMS(sender: str, message: str, phone_numbers):
    data = {
        'sender': sender,
        'message': message,
        'recipients': phone_numbers
    }

    headers = {
        'api-key': settings.API_KEY,
        "Content-Type": "application/json"
    }
    params = json.dumps(data)
    messageResponse = requests.post(
        url=settings.SEND_SMS_URL,
        data=params,
        headers=headers)
    logger.info(messageResponse.json())
    return messageResponse.json()
