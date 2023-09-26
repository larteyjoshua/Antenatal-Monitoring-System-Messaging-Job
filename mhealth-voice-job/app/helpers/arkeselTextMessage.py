import requests
from app.utils.config import settings
from pathlib import Path
from loguru import logger


def sendVoiceSMS(phone_number: str):
    voice_file = Path("app/static/voice/announcement.mp3")
    data = {'recipients[]': [phone_number],
            'voice_id': ''}
    files = {
        'voice_file': (
            'announcement.mp3', open(voice_file, 'rb'), 'audio/mp3')}
    headers = {
        'api-key': settings.API_KEY,
    }
    r = requests.post(url=settings.SEND_VOICE_SMS_URL,
                      data=data,
                      files=files, headers=headers)
    logger.info(r)
    logger.info(r.json())

    return r.json()
