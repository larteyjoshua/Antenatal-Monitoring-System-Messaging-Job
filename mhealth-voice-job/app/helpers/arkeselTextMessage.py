import requests
from app.utils.config import settings
import json
from requests_toolbelt import MultipartEncoder
from pathlib import Path
from loguru import logger


def sendVoiceSMS(phone_number: str):
    voice_file = Path("app/static/voice/announcement.mp3")

    data = MultipartEncoder(
        fields={
            'recipients[]': (None, phone_number),
            'voice_file': ('announcement.mp3', open(voice_file, 'rb'), 'audio/mp3')
        }
    )
    headers = {
        'Content-Type': data.content_type,
        'api-key': settings.API_KEY
    }
    messageResponse = requests.post(
        url=settings.SEND_VOICE_SMS_URL,
        data=data,
        headers=headers,)
    logger.info(messageResponse.json())
    return messageResponse.json()
