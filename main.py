import editdistance
from random import choice
from logic import BOT_CONFIG as BOTCON
# from ai import ask_gpt
from telebot import telebot
from mistralai import Mistral
import dotenv
import os
dotenv.load_dotenv()

def ask_gpt(content):
    # client = Mistral(api_key='9R7ejYU6QoycCOTilZFyCgJbe6c09MVs')
    client = Mistral(api_key=os.getenv('MISTRAL_API_KEY'))

    chat_response = client.chat.complete(
        model = "mistral-large-latest",
        messages = [
            {
                "role": "user",
                "content": content,
            },
        ]
    )
    return chat_response.choices[0].message.content




def clean(text):
    output_text = ''
    for i in text.lower():
        if i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя abcdefghijklmnopqrstuvwxyz/':
            output_text += i
    return output_text


def get_intent(text):
    for intent in BOTCON['intents'].keys():
        for example in BOTCON['intents'][intent]['examples']:
            text1 = clean(example)
            text2 = clean(text)
            if editdistance.eval(text1, text2) / max(len(text1), len(text2)) < 0.4:
                return intent
    return 'Не удалось определить тему'

def bot(text):
    intent = get_intent(text)
    if intent != 'Не удалось определить тему':
        return choice(BOTCON['intents'][intent]['responces'])
    else:
        return 'Извините, но я ничего не понял. Напишите /help для получения списка команд.'
token = api_key=os.getenv('TG_TOKEN')
# token = '8106236659:AAGREaGAI0fblHs_d4N3a9VtC2DP6tPmI6Y'
client = telebot.TeleBot(token)
@client.message_handler(content_types=['text'])
def lalala(message):
    if message.text[0:4] == '@gpt':
        a = message.text.replace('@gpt', '')
        client.send_message(message.chat.id, ask_gpt(a))
    else:
        client.send_message(message.chat.id, bot(message.text))
if __name__ == '__main__':
    client.infinity_polling()