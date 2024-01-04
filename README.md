# Daily Horoscope Bot

Welcome to the Daily Horoscope Bot (Built for fun purpose)! This Telegram bot provides daily horoscope readings based on your zodiac sign and the desired day.

## Features

- Greet users with a friendly message when they start or send a greeting command (/start, /hello, /hi).
- Allow users to request their daily horoscope using the /horoscope command.
- Prompt users to select their zodiac sign and the desired day for the horoscope reading.
- Fetch and display the horoscope information for the specified zodiac sign and day.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/PrantaDas/tg-horoscope.git
    cd tg-horoscope
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Telegram bot and obtain the BOT_TOKEN.

4. Create a `.env` file in the project root and add your BOT_TOKEN:

    ```ini
    BOT_TOKEN = your_bot_token_here
    DATA_URL = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    ```

5. Run the bot:

    ```bash
    python main.py
    ```

## Usage

1. Start a chat with the bot on Telegram.
2. Send a greeting command (/start, /hello, /hi) to receive a friendly response.
3. Use the /horoscope command to request your daily horoscope.
4. Follow the prompts to select your zodiac sign and the desired day.
5. Receive your personalized horoscope reading from the bot!

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request.


Happy horoscope reading!
