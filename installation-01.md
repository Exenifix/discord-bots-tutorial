# Lesson 1 | Installation
## Lesson Subject
Learn how to install everything for bots development.

## Recommended Software
As said in introduction, we can recommend Visual Studio Code and PyCharm.

If you are a fan of browser IDEs like replit, we have to disappoint you — most of them have ephemeral file system, which means all the files created during program execution will be destroyed as soon as the application is killed, and there's a probability of getting another issue — shared IP. It means that all the requests your app and other apps are sent from the same IP address. Many people might also run their bots. Discord API has a ratelimit of **50 requests per second** for each IP. Read more about it [here](https://discord.com/developers/docs/topics/rate-limits).

You will also need a Python Interpreter with version not lower than 3.8, as it is the minimum version required by the library. We recommend installing the latest version available!

## Modules Installation
### Visual Studio Code
1. Proceed to your project directory or create one
2. Open a terminal and run the following command
```sh
$ py -m venv venv
```
This should create a virtual environment we will need for easier modules management.
3. Press CTRL + SHIFT + P and pick "Select Python Interpreter", then select one with "venv"
4. Open another terminal. The command string should have `(venv)` at the beginning. 
5. Run `pip install -U pip` to update the pip
6. Run `pip install disnake` to install the library for making discord bots.
> In this tutorial we are going to use disnake - a fork of discord.py that is easy to understand compared to some others. You may also use `nextcord` which is very similar to disnake or the original library — `discord.py`, however its implementation of slash commands is different and is not liked by many.
#### Troubleshooting
1. You may get "py is not recognised as a command, executable, ..." error. It might happen because you didn't add Python to PATH on installation. The solution to this is first to try to replace `py` with `python` and `python3`, if these both fail, then reinstall Python or add it to PATH [manually](https://datatofish.com/add-python-to-windows-path/). 
2. You may get "scripts execution is prohibited in this system". To resolve this issue, run Windows PowerShell with administrator permissions and execute the following command:
```sh
Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy Unrestricted
```
### PyCharm
PyCharm setup is a bit easier because it handles the exceptions we may face automatically and also manages venv by itself. We will only need to
1. Create a new project
2. Open terminal and run these commands
```sh
pip install -U pip
pip install disnake
```

There you go, you may start the development now!
