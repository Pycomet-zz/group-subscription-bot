import logging
import os
import re
import csv
import stripe
import pyshorteners
from flask import Flask, request

# from flask_apscheduler import APScheduler
from telethon.sessions import StringSession
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import DeleteChatUserRequest
from datetime import date
import telegram
import time
import telebot
import asyncio
from telethon import TelegramClient
from telebot import types
import requests
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")  # Input your api_id here
api_hash = os.getenv("API_HASH")  # Input your api_hash here

from models import User

user = User
LANGUAGE = user.language

# # Language setup
# os.environ["LANGUAGE"] = "en"
# LANGUAGE = os.getenv("LANGUAGE")

## Setup logs file for debugging
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
logging.basicConfig(
    filename="extract.log",
    format="%(levelname)s: %(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S",
)

TOKEN = os.getenv("TOKEN")

DEBUG = False
SERVER_URL = os.getenv("SERVER_URL")

GROUP = os.getenv("GROUP")
SESSION = os.getenv("SESSION")

## Connection of all the integrated APIs
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
client = TelegramClient(
    StringSession(SESSION), api_id=api_id, api_hash=api_hash, loop=loop
)
client.start()  # Starting Telegram Bot API
print(client.session.save())

fieldnames = ["First Name", "Last Name", "Username", "User Id", "Joined Days Count"]


class Config:
    SCHEDULER_API_ENABLED = True


# scheduler = APScheduler()


stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


shortener = pyshorteners.Shortener()

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
app.config.from_object(Config())
# scheduler.init_app(app)
# scheduler.start()
