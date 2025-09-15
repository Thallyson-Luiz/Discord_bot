from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

# Carrega as variáveis de ambiente
load_dotenv()

bot = commands.Bot(command_prefix='.', intents=discord.Intents.default())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}') # type: ignore


bot.run(os.getenv('BOT_TOKEN') or 'CHANGE-ME')
