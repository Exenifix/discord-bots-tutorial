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


intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
log = Logger()


@bot.event
async def on_ready():
    log.ok("Bot is ready!")
    await bot.change_presence(activity=disnake.Game("python"))


@bot.command(name="hello", aliases=["hi", "greeting"])
async def hello(ctx: commands.Context):
    log.info("Received hello entry!")
    await ctx.send(f"Hi, {ctx.author.mention}!")


@bot.slash_command(name="hello", description="Greets the user")
async def hello_slash(inter: disnake.ApplicationCommandInteraction):
    log.info("Received hello entry!")
    await inter.send(f"Hi, {inter.author.mention}!")


@bot.slash_command(name="badcommand")
async def trash(inter: disnake.ApplicationCommandInteraction):
    pass


log.info("Starting the bot...")
bot.run(get_token())
