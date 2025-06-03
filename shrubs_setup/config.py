import os
from dotenv import load_dotenv
load_dotenv()

class EnvVariables:
    WEB_URL = os.getenv("WEB_URL")
    CORRECT_EMAIL = os.getenv("CORRECT_EMAIL")
    CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
    PASSWORD = os.getenv("PASSWORD")
    RESET_PASSWORD = os.getenv("RESET_PASSWORD")
    CONFIRM_PASSWORD = os.getenv("CONFIRM_PASSWORD")

config = EnvVariables()
