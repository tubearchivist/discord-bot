"""discord bot for tubearchivist server"""

import os
import time

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

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

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_thread_create(thread):

    time.sleep(3)

    await thread.send(WELCOME_MESSAGE)

@bot.event
async def on_thread_update(before, after):
    if any(tag.name == "solved" for tag in after.applied_tags):
        if not after.name.startswith("[SOLVED]"):
            await after.edit(name="[SOLVED] " + after.name)

        await after.edit(archived=True)

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.Thread) and message.channel.name.startswith("[SOLVED]"):
        solved_tag = discord.utils.get(message.guild.tags, name="solved")
        await message.channel.remove_thread_tags(solved_tag)
        new_name = message.channel.name.replace("[SOLVED] ", "", 1)
        await message.channel.edit(name=new_name)
    await bot.process_commands(message)

if __name__ == "__main__":
    bot_token = os.environ.get("BOT_TOKEN")
    bot.run(bot_token)
