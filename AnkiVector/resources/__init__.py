#MIT License

#https://t.me/CGSUPDATES

import logging

from AnkiVector import API_HASH, API_ID, TOKEN

from pyrogram import Client

from Python_ARQ import ARQ

from aiohttp import ClientSession

from AnkiVector import ARQ_API_KEY

ARQ_API_URL = "https://thearq.tech"

aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

MONGODB_CLI = Bot(mango)
