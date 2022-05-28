# Lesson 1 | Basic Bot
## Lesson Subject
Learn how to create application on Discord Developer portal and build a very basic bot.

## Creating Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to application page and select `Bot` tab
4. Click `Add Bot` button
5. Notice the `Reset Token` button - you may press it and copy the token right now or come back to it later
6. Invite the bot to your server from `OAuth2` -> `URL Generator`. Add `bot` and `applications.commands` scopes and required permissions, then copy link and follow it

## Token Storage
### .env file
Usually the developers use `.env` config files to store the token securely. We are going to show you how to use them in code.
1. Run this command to install the module for working with `.env` files
```sh
$ pip install python-dotenv
```
2. Create a new file named `.env` with the following contents:
```
TOKEN=
```
3. Put your token **without any additional symbols or spaces** right after `TOKEN=`. It should look like this:
```
TOKEN=OTc5MzU0NTM0NTEyMDUwMTk2.G9Ft4q.kcb5BIKqqJnDtwviIz_VMiaunVLLci8U6Oxlgc
```
4. Now in your main script you can get it like this:
```py
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")
assert TOKEN is not None, "TOKEN was not found"  # we need this to make sure that token is filled in correctly.
```

### Fernet Encryption
You may also *encrypt* your token so it is visible only if you have the key to decrypt it. We will need `cryptography` module to done this:
```sh
$ pip install cryptography
```
#### Encryption Script
```py
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
with open("key.key", "wb") as key_file, open("token", "wb") as token_file:
    key_file.write(key)
    token = input("Insert the token here: ").encode()
    token_file.write(fernet.encrypt(token))
```
#### Decryption Script
```py
from cryptography.fernet import Fernet

with open("key.key", "rb") as key_file, open("token", "rb") as token_file:
    fernet = Fernet(key_file.read())
    TOKEN = fernet.decrypt(token_file.read()).decode()
```
In your `token` file the encrypted token is stored, and in the `key.key` the key required to decrypt the token is stored. You may put the key into some safe place and use it when needed.

## Basic Bot
Now let's build a bot! 
> To display logs in this sample we are going to use `exencolorlogs` module which can be installed with pip. You may use simple `print()` statements or setup logging by yourself if you don't like this module's implementation.
```py
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


bot = commands.Bot( command_prefix="!")  # create a bot object, it is the object everything will be based on
log = Logger()


@bot.event
async def on_ready():
    log.ok("Bot is ready!")


log.info("Starting the bot...")
bot.run(get_token())
```
> Please notice that any code after `bot.run()` will not be executed until the bot is shutted down.

If everything went fine, you will receive "Bot is ready!" message in the console and your bot will come online! You may also change its activity by adding this into `on_ready`:
```py
await bot.change_presence(activity=disnake.Game("python"))
```

## Asynchronous App
The bot we just made is *an asynchronous app* which uses `async` and `await` keywords. All API calls must be awaited. It is recommended to know principles of asynchronous programming for this tutorial although it is a good entrypoint to asynchronous programming overall.
