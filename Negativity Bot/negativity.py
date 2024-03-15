import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    try:
        await message.add_reaction('\U0001F44E')
    except:
        pass

client.run()




