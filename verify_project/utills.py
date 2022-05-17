import os
from twilio.rest import Client
from decouple import config

account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message =  client.messages.create(
        body=f'Hi!, You user and verification code id {user_code}',
        from_='+19403604974', 
        to= "+"+phone_number,
    )
    print(message.sid)