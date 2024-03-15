Reacts to every new message in allowed channels.

Requires config.py detailed below:
"""
from dataclasses import dataclass

@dataclass()
class ConfigData:
    REACTION_ID= # EX: '\U0001F44E' for Thumbsdown
    BOT_TOKEN=
"""