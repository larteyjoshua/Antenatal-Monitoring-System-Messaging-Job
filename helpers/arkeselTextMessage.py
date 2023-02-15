import requests
from utils.config import settings
import json

def sendSMS(sender: str, message: str, phone_numbers):
        data = {
        'sender':sender,
        'message': message,
        'recipients': phone_numbers
        }
    
        headers = {
        'api-key':settings.API_KEY,
        "Content-Type": "application/json"
        } 
        params = json.dumps(data)
        print('data', params)
        messageResponse = requests.post(
           url = settings.SEND_SMS_URL, 
            data = params,
            headers = headers)
        return messageResponse.json()
        
   