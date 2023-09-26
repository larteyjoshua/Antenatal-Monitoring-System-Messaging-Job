import requests
from app.utils.config import settings
from pathlib import Path
from loguru import logger


def sendVoiceSMSWithMnotify(phone_number: str):
    endPoint = settings.MNOTIFY_VOICE_SMS_URL
    apiKey = settings.MNOTIFY_API_KEY
    voice_file = Path("app/static/voice/announcement.mp3")
    file = {'file': (
            'announcement.mp3', open(voice_file, 'rb'), 'audio/mp3')}
    data = {
        'campaign': 'Antenatal Remainder',
        'recipient[]': [phone_number],
        'is_schedule': False,
        'voice_id': '',
        'schedule_date': ''
    }

    print(data)
    url = endPoint + '?key=' + apiKey
    response = requests.post(
        url=url, data=data, files=file)
    logger.info(response)
    data = response.json()
    logger.info(data)
    return data
