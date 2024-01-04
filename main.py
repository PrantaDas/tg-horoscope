#  Internal
from bot import bot

if __name__ == '__main__':
    """
    Main script to start and run the bot.

    This script initializes the bot and starts an infinite polling loop to receive and process updates.

    Usage:
        python main.py

    Raises:
        KeyboardInterrupt: Raised when the user interrupts the script (e.g., by pressing Ctrl+C).
        Exception: Any unexpected exception that might occur during the bot's execution.
    """
    try:
        print('=> Bot started ')
        # Start the bot's infinite polling loop
        bot.infinity_polling()

    except KeyboardInterrupt as e:
        # Handle the KeyboardInterrupt gracefully
        print(f"KeyboardInterrupt: {e}")
    
    except Exception as e:
        # Handle any other unexpected exception
        print(f"Exception: {e}")
