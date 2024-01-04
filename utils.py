from dotenv import load_dotenv
import requests
from requests.exceptions import RequestException
import os

load_dotenv()

def get_daily_horoscope(sign: str, day: str) -> dict:
    """
    Get daily horoscope for a given zodiac sign and day.

    Args:
        sign (str): Zodiac sign (e.g., 'Aries', 'Taurus', etc.).
        day (str): Day for which the horoscope is requested (e.g., 'today', 'tomorrow', etc.).

    Returns:
        dict: Horoscope information in JSON format.

    Raises:
        RequestException: If there is an issue with the HTTP request.
        ValueError: If the provided URL is missing or invalid.
    """
    try:
        # Retrieve the data URL from the environment variables
        url = os.environ.get('DATA_URL')
        if not url:
            raise ValueError('No URL specified in the environment variables.')

        # Set up the request parameters
        params = {'sign': sign, 'day': day}

        # Make the HTTP request
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Return the JSON response
        return response.json()

    except RequestException as e:
        print(f"RequestException: An unexpected error occurred during the HTTP request: {e}")
        # Log the error or handle it appropriately for your application

    except ValueError as e:
        print(f"ValueError: {e}")
        # Log the error or handle it appropriately for your application

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Log the error or handle it appropriately for your application

    return None

