import os
import sys

import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from exencolorlogs import Logger


def get_token() -> str:
    """Fill in this function based on the method you used for storing token. This one uses .env file."""
    load_dotenv()
    token = os.getenv("TOKEN")
    if token is None:
        log.critical("Token is not filled in.")
        sys.exit(1)

    return token


bot = commands.Bot(
    command_prefix="!"
)  # create a bot object, it is the object everything will be based on
log = Logger()


@bot.event
async def on_ready():
    log.ok("Bot is ready!")
    await bot.change_presence(activity=disnake.Game("python"))


log.info("Starting the bot...")
bot.run(get_token())
