from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__)) 

load_dotenv(os.path.join(BASE_DIR, ".env"))

BOT_TOKEN = os.environ.get("BOT_TOKEN")