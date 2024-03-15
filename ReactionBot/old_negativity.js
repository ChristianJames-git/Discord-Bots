const Discord = require('discord.js');
const client = new Discord.Client();
const THUMBS_DOWN_EMOJI = '👎';

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('message', message => {
  // Add reaction to every message that is not from the bot itself
  if (message.author.id !== client.user.id) {
    message.react(THUMBS_DOWN_EMOJI);
  }
});

client.login();