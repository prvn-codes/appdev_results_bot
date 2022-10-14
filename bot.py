import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="Only For App Dev"))
 
async def load_cogs_func():
  print("--- Loading Cogs ---")
  for _, _, files in os.walk('./cogs/'):
        for file in files:
            file_name, ext = os.path.splitext(file)
            print(f"{file_name}")
            await bot.load_extension(f'cogs.{file_name}')
        break
  print("---Cogs Loaded---")   


if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(load_cogs_func())
  bot.run(os.environ["BOT_TOKEN"])
  loop.close()