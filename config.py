from pyrogram import filters
import os

class Config:
    API_ID = "23378380"
    API_HASH = "5ddcf1df1360fe446b06dd94bd3ad0c6"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://jarvisxd45:rajnish68mishra85@atlascluster.xkizs7c.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/2397df5c916a1933957d4.jpg"
    SUDOERS = filters.user(["6539801772"])
