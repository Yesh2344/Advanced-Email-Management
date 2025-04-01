# config.py
import os
from dotenv import load_dotenv

# Optionally load variables from a .env file if you have one.
load_dotenv()

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'imap.gmail.com')
EMAIL_USER = os.environ.get('EMAIL_USER', 'y@gmail.com')
EMAIL_PASS = os.environ.get('EMAIL_PASS', 'your_app_specific_password')
IMAP_PORT = 993
