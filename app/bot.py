"""discord bot for tubearchivist server"""

import os

import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

client = discord.Client(intents=intents)

WELCOME_MESSAGE = """Welcome to the forum!
Thanks for starting a new thread.
"""

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_thread_create(thread):

    await thread.send(WELCOME_MESSAGE)


if __name__ == "__main__":
    bot_token = os.environ.get("BOT_TOKEN")
    client.run(bot_token)
