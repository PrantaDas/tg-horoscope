import os
from telebot import TeleBot
from dotenv import load_dotenv

# Internal
from utils import get_daily_horoscope

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN must be provided in the environment variables.')

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello', 'hi'])
def greet(message):
    """
    Responds with a greeting message when the user sends a start, hello, or hi command.

    Args:
        message (obj): The message object from the user.

    Returns:
        None
    """
    bot.reply_to(message, 'Hey, how are you doing?')


@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    """
    Handles the /horoscope command by asking the user for their zodiac sign.

    Args:
        message (obj): The message object from the user.

    Returns:
        None
    """
    text = ("What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, "
            "*Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*.")
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


def day_handler(message):
    """
    Handles the user's response to the zodiac sign prompt and asks for the desired day.

    Args:
        message (obj): The message object from the user.

    Returns:
        None
    """
    sign = message.text
    text = ("What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in "
            "format YYYY-MM-DD.")
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign.capitalize())


def fetch_horoscope(message, sign):
    """
    Fetches the horoscope for the specified zodiac sign and day and sends the result to the user.

    Args:
        message (obj): The message object from the user.
        sign (str): The zodiac sign.

    Returns:
        None
    """
    day = message.text
    horoscope = get_daily_horoscope(sign, day)
    
    if horoscope:
        data = horoscope.get("data", {})
        horoscope_message = f'*Horoscope:* {data.get("horoscope_data", "Not available")}\n' \
                            f'*Sign:* {sign}\n*Day:* {data.get("date", "Not available")}'
        bot.send_message(message.chat.id, "Here's your horoscope!")
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Failed to retrieve the horoscope. Please try again later.")
