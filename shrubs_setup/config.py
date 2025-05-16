import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class EnvVariables:
    # email = random_string_generator() + '@gmail.com'
    # print(email)
    WEB_URL: str = os.getenv("WEB_URL")
    CORRECT_EMAIL: str = os.getenv("CORRECT_EMAIL")
    CORRECT_PASSWORD: str = os.getenv("CORRECT_PASSWORD")
    EMAIL: str = os.getenv("EMAIL")
    PASSWORD: str = os.getenv("PASSWORD")
    RESET_PASSWORD: str = os.getenv("RESET_PASSWORD")


config = EnvVariables()
