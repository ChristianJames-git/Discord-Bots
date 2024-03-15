Schedules a message ping with customizable message, scheduled time, ping target, and discord channel.

Requires config.py detailed below:
"""
from datetime import datetime
from dataclasses import dataclass

@dataclass()
class ConfigData:
    CHANNEL_ID=
    PING_TARGET=
    MESSAGE_TIME= # datetime format rounded to nearest minute, set to datetime.now().replace(second=0).replace(microsecond=0).time() for instant ping
    MESSAGE=
    BOT_TOKEN=
"""