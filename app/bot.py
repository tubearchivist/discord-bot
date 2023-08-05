"""discord bot for tubearchivist server"""

import os
import time

import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

client = discord.Client(intents=intents)

WELCOME_MESSAGE = """
## Welcome to the Support Channel!
To streamline the support process and expedite solutions, please complete the following checklist before reaching out for assistance:

## Support Checklist:
- **Search for Solutions**: Check our documentation and FAQs for existing answers <https://docs.tubearchivist.com/>.
- **Reproduce the Issue**: Try replicating the problem and note the steps.
- **Review Settings**: Double-check your configurations.
- **Provide Relevant Logs**: Include related logs with your query. Use a site like <https://pastebin.com/> to quickly share large log files.
- **Provide Installation details**: For questions about installing, share your compose file or other relevant info.
- **Describe the Issue**: Clearly explain the problem and prior steps.

## Let's work together to get everything running smoothly! 🚀
"""

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_thread_create(thread):

    time.sleep(3)

    await thread.send(WELCOME_MESSAGE)


if __name__ == "__main__":
    bot_token = os.environ.get("BOT_TOKEN")
    client.run(bot_token)
