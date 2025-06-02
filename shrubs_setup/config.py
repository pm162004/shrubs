import os
from dotenv import load_dotenv
load_dotenv()

class EnvVariables:
    WEB_URL:str = os.getenv("WEB_URL")
    CORRECT_EMAIL: str = os.getenv("CORRECT_EMAIL")
    CORRECT_PASSWORD: str = os.getenv("CORRECT_PASSWORD")
    PASSWORD: str = os.getenv("PASSWORD")
    RESET_PASSWORD: str = os.getenv("RESET_PASSWORD")
    CONFIRM_PASSWORD: str = os.getenv("CONFIRM_PASSWORD")

config = EnvVariables()
