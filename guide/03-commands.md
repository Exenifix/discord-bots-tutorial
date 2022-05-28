# Lesson 3 | Commands
## Lesson Subject
In this lesson we are going to learn how to
- create text and slash commands
- send responses to commands
- add arguments to commands

## Adding a Command
Let's look into this piece of code which is supposed to add a simple text command to a bot
```py
@bot.command(
    name="hello",
    aliases=["hi", "greeting"]
)
async def hello(ctx: commands.Context):
    log.info("Received hello entry!")
    await ctx.send(f"Hi, {ctx.author.mention}!")
```
1. First of all, we have a `@bot.command` decorator which registers the decorated function as a command callback. You can parse several parameters to it, explore them in the [documentation](https://docs.disnake.dev/en/latest/ext/commands/api.html#disnake.ext.commands.Command). All the parameters are *optional*
2. Next, we have a function itself. First argument is the *invokation context* and it contains many stuff we will need. Check out its attributes [here](https://docs.disnake.dev/en/latest/ext/commands/api.html#disnake.ext.commands.Context). The `: commands.Context` is a typehint which basically allows you to get code suggestions in this case
3. In the body of function we have a log entry and a [statement for sending the message](https://docs.disnake.dev/en/latest/api.html#disnake.abc.Messageable.send)
4. The f-string which is a python feature newcomers might not know about. It allows pretty easy and good-looking string formatting. Read more about it [here](https://peps.python.org/pep-0498/)

You can now put this command **before `bot.run()`**, as none of statements after it will be executed until bot is stopped. In fact, all the commands we make in single script bots should lay between bot declaration and run statement.
> **WARNING!**<br>
> Later, we will learn how to organize bot's commands better with usage of extensions and cogs. In fact, writing all commands in a single script is discouraged and will cause issues with huge projects. So, please don't rush into making a bot with 200 commands and putting them all into one file. You will *definitely regret*.

## Introduction into Intents
Have you tested your brand new command already? If you did, you are probably confused - the command did not work. There was nothing in the console neither bot sent anything in response. Why did that happen?<br>
Well, let us explain one thing. The communication between your bot and the Discord API includes **websocket events** which are sent from server to the app and the **API calls** that are sent from the app to the server. When a message is sent in a guild that bot is a member of, the Discord sends an event to the app. App catches it and checks if a message is a command. If it is, then the app invokes the command callback and bot does what it is supposed to do. But there's a small nuance - Discord won't send us events until we *request* them. For that, the **intents** are used. They basically tell Discord what events to send to us. <br>

So how do we enable intents? First, you need to go to the [Discord Developer Portal](https://discord.com/developers/applications), then to your application page and then to "Bot" tab. Scroll down, and you will see these things<br>
<img src="https://github.com/Exenifix/discord-bots-tutorial/blob/master/images/intents.jpg">
We will need the **Message Content** and **Server Members**. Then we can enable the intents in our code. For that, we need to create an instance of `disnake.Intents` and parse it to `intents` kwarg of the Bot constructor.
```py
intents = disnake.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
```
Test the bot now! Everything should work fine.

## Slash Commands
As for disnake, the slash commands implementation is very similar to the text commands ones, although we gotta tell you about some nuances of slash commands. First, let's look into slash version of our `hello` command:
```py
@bot.slash_command(name="hello", description="Greets the user")
async def hello_slash(inter: disnake.ApplicationCommandInteraction):
    log.info("Received hello entry!")
    await inter.send(f"Hi, {inter.author.mention}!")
```
It does have some small differences with the text commands
1. There's a different decorator for slash commands - `@bot.slash_command`
2. It is highly encouraged to provide description to a slash command because if you don't, it will look unnice
<img src="https://github.com/Exenifix/discord-bots-tutorial/blob/master/images/no-desc-command.jpg">

3. Slash commands **do not support aliasing**. If you really want to implement it (although nobody does that), you may decorate the function with several decorators but with different `name` param values
4. Instead of `ctx: commands.Context` we use `inter: disnake.ApplicationCommandInteraction`. We name the argument differently because its type is different as well. The `ApplicationCommandInteraction` is very similar to `Context` although they do have some differences
5. The message is sent through *interaction* and is not a common message. Read about the send method [here](https://docs.disnake.dev/en/latest/api.html#disnake.Interaction.send)
6. Slash commands do not need message content intent to function properly
> Notice that we named the function for slash command not the same with the text command function. It is made to avoid names overwriting. **You should never name 2 functions the same!**
