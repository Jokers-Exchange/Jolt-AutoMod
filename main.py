import discord
from discord.ext import commands
import time
from ping import keep_alive
whitelisted_airdrop_users = [867136262704201768, 867136262704201768, 617037497574359050]
whitelisted_invite_users = []
client = commands.Bot(command_prefix = '*')


@client.event
async def on_ready():
  print("Im Awake!")
@client.event
async def on_message(message):
  if "https://discord" in message.content:
    if message.channel.id != 861766094641823784:
      time.sleep(0.3)
      await message.delete()
      await message.channel.send("discord invites are not allowed!")
  elif "discord.gg" in message.content:
    time.sleep(0.3)
    await message.delete()
    await message.channel.send("discord invites are not allowed!")
  elif "$airdrop" not in message.content:
    if message.author.id not in whitelisted_airdrop_users:
        if message.channel.id == 853318242584231936:
          time.sleep(0.3)
          await message.delete()
          await message.channel.send(f"{message.author.mention}, You can only airdrop in this channel! if you keep repeating this offense you will be muted or banned!")

  await client.process_commands(message)

keep_alive()
client.run('BOTTOKEN')
