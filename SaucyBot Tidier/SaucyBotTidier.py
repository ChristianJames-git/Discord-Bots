import discord
import re
import asyncio
from config import ConfigData

# This regex matches typical URL structures
url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

intents = discord.Intents.default()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        # Check if the message is from SaucyBot
        if message.author.name == 'SaucyBot':
            # Check the history of the channel where the message was sent
            messages = [msg async for msg in message.channel.history(limit=2)]

            # Ensure there are at least two messages (SaucyBot's and the previous one)
            if len(messages) == 2:
                prev_message = messages[1]  # Get the message before SaucyBot's message

                # Check if the previous message contains a link
                if url_regex.search(prev_message.content):
                    try:
                        def check(m):
                            return m.author.name == 'SaucyBot' and m.embeds

                        await self.wait_for('message', timeout=30.0, check=check)
                        await prev_message.delete()  # Delete the previous message
                        print("Deleted a message containing a link.")
                    except discord.Forbidden:
                        print("Do not have permission to delete the message.")
                    except discord.HTTPException as e:
                        print(f"Failed to delete message: {e}")
                    except asyncio.TimeoutError:
                        print("Timed out waiting for SaucyBot to post an embedded link.")
                else:
                    print("The previous message does not contain a link.")
            else:
                print("SaucyBot's message is not following any user messages or there is not enough history.")
        # Ignore messages sent by the bot itself to avoid self-deletion or responding to its own commands
        elif message.author == self.user:
            return


client = MyClient(intents=intents)
client.run(ConfigData.BOT_TOKEN)
