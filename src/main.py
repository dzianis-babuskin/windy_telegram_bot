import datetime

from telegram.ext import Updater, CommandHandler

from src.const import BOT_TOKEN
from src.open_weather import get_hourly_weather_by_name


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send '/wind' to bot to know the wind speed for upcoming hours")

def wind(update, context, city_name='Minsk'):
    weather_json = get_hourly_weather_by_name(city_name)
    weather_string = 'Remind you that Mavic mini max wind resistance is 8 m/s\n'
    for weather in weather_json:
        weather_string += f'Wind speed at {time(get_timestamp_from_json(weather))} - {get_wind_speed_from_json(weather):.1f} m/s'
        weather_string += '\n'
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather_string)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('wind', wind))
    updater.start_polling()
    updater.idle()

def get_wind_speed_from_json(weather:dict) -> float:
    return weather['wind_speed']

def get_timestamp_from_json(weather:dict) -> int:
    return weather['dt'] + 3600 * 3 #Local timezone is +3

def time(timestamp:int):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%H:%M')


if __name__ == '__main__':
    main()