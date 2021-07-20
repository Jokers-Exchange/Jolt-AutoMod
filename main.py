import discord
from discord.ext import commands
#Bot made by Cryptic!
whitelisted_airdrop_users = [USERIDS]
client = commands.Bot(command_prefix = 'PREFIX')


@client.event
async def on_ready():
  print("MESSAGE ON READY!")
@client.event
async def on_message(message):
  if "https://discord" in message.content:
    await message.delete()
    await message.channel.send("discord invites are not allowed!")
  elif "discord.gg" in message.content:
    await message.delete()
    await message.channel.send("discord invites are not allowed!")
  elif "$airdrop" not in message.content:
    if message.author.id not in whitelisted_airdrop_users:
        if message.channel.id == CHANNELID:
          await message.delete()
          await message.channel.send(f"{message.author.mention}, MESSAGE OF YOUR CHOICE")


client.run('BOT TOKEN')
