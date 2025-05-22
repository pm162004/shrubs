import os
from dotenv import load_dotenv
load_dotenv()


class EnvVariables:
    WEB_URL:str = os.getenv("WEB_URL")
    CORRECT_EMAIL: str = os.getenv("CORRECT_EMAIL")
    CORRECT_PASSWORD: str = os.getenv("CORRECT_PASSWORD")
    EMAIL: str = os.getenv("EMAIL")
    NEW_PASSWORD: str = os.getenv("NEW_PASSWORD")
    CONFIRM_PASSWORD: str = os.getenv("CONFIRM_PASSWORD")
config = EnvVariables()
