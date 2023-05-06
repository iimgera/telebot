import requests


TOKEN = '5923286722:AAE_VLnyQiWstGS17Gdd7zmRYMe4fbDBbt8'
CHAT_ID = '-1001801986206'


def send_message(message, chat_id):
    bot_token = TOKEN
    chat_id = CHAT_ID
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    response = requests.post(api_url, json={'chat_id': chat_id, 'text': message})
