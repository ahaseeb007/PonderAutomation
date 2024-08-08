import os
from dotenv import load_dotenv

load_dotenv()

class config:
    app_url = os.getenv("BASE_URL")
    meta_password= os.getenv("PASSWORD")