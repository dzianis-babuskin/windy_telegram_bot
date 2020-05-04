import requests
from pprint import pprint
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, KeyboardButton, InlineKeyboardMarkup
import telegram


#todo: delete all sensitive data before pushing into repository
BOT_TOKEN = 'YOUR TOKEN'
UNITS = 'metric'
API_KEY = 'YOUR API KEY'


def get_current_weather_by_name(city_name:str):
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()

def get_current_weather_by_geo(lat:int, lon:int):
    api_call = f'https://api.openweathermap.org/data/2.5/forecast/weather?lat={lat}&lon={lon}&appid={API_KEY}&units={UNITS}'
    return requests.get(api_call).json()

def start(update, context):
    some_strings = ["col1", "col2", "row2"]
    button_list = [[KeyboardButton(s)] for s in some_strings]
    # context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()