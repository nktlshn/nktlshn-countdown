from datetime import datetime
from telegram.ext import Updater
import random
import emojis_list
from cfg import TG_TOKEN, GROUP_ID, DAY_X

TODAY = datetime.now()


def get_time_delta():
    day_x = datetime.strptime(DAY_X, '%d%m%Y')
    delta_days = TODAY - day_x

    return abs(delta_days.days)


def not_weekend():
    if TODAY.weekday() not in (5, 6):
        return True
    else:
        return False


days_left = get_time_delta()


def send_message_to_tg():
    random_emoji = random.choice(emojis_list.emoji_list)

    updater = Updater(TG_TOKEN)
    updater.bot.send_message(chat_id=GROUP_ID,
                             text=f'Days left to day X: {days_left} {random_emoji}')
    print('sending...')


if __name__ == '__main__' and not_weekend():
    send_message_to_tg()
