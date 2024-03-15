import discord
import asyncio
from datetime import datetime
from config import ConfigData

intents = discord.Intents.default()
intents.members = True

# Set up the client
client = discord.Client(intents=intents)

# Set the channel ID and message to send
CHANNEL_ID = ConfigData.CHANNEL_ID # Replace with the ID of the channel you want to send messages to
MESSAGE = f"<@{ConfigData.PING_TARGET}> {ConfigData.MESSAGE}"
MESSAGE_TIME = ConfigData.MESSAGE_TIME

# Function to send the message
async def send_message():
    print(MESSAGE)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(MESSAGE)

# Function to check if it's time to send the message
async def check_time():
    while True:
        now = datetime.now().replace(second=0).replace(microsecond=0).time()
        print(now)
        print(now == MESSAGE_TIME)
        if now == MESSAGE_TIME:
            print(now == MESSAGE_TIME)
            await send_message()
        await asyncio.sleep(60) # Check every minute

# Log in the bot and start the loop
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(check_time())

client.run(ConfigData.BOT_TOKEN) # Replace with your Discord bot token
