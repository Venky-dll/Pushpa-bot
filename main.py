import discord
from discord.ext import commands
from quadratic_eq import roots
from weather import weather

intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Import commands 
bot.add_command(roots)
bot.add_command(weather)
    

bot.run('bot_token')
