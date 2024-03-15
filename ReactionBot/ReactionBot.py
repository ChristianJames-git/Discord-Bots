# TODO Improve customizability - Add discord commands: Select player target(s) or all ; Select channel target(s) or all visible ; Set timeout time ; Choose Reaction
import discord
from config import ConfigData

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    try:
        await message.add_reaction(ConfigData.REACTION_ID)
    except:
        pass

client.run(ConfigData.BOT_TOKEN)
