import os
import discord
import asyncio
from datetime import datetime, time

intents = discord.Intents.default()
intents.members = True

# Set up the client
client = discord.Client(intents=intents)

# Set the channel ID and message to send
CHANNEL_ID =  # Replace with the ID of the channel you want to send messages to
MESSAGE = "@ RETURN AT ONCE!" # Replace with the message you want to send

# Function to send the message
async def send_message():
    print(MESSAGE)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(MESSAGE)

# Function to check if it's time to send the message
async def check_time():
    while True:
        now = datetime.now().time()
        if now == time(15, 51):  # Replace with the time you want the message to be sent
            print(datetime.now().time())
            await send_message()
        await asyncio.sleep(60) # Check every minute

# Log in the bot and start the loop
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    client.loop.create_task(check_time())

client.run()
