import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('start'):
        await message.channel.send("Commands:!mem MRX Hallo Привет Bye Пока Случайное число")
    elif message.content.startswith(('MRX', 'Hallo', 'Привет')):
        await message.channel.send("Hello, how can I help?")
    elif message.content.startswith(('Bye', 'Пока')):
        await message.channel.send("Goodbye, master")
    elif message.content.startswith('Случайное число'):
        rand = random.randint(1, 1000000)
        await message.channel.send(f"Random number: {rand}")
    else:
        await bot.process_commands(message)

@bot.command()
async def mem(ctx):
    images_path = 'imag'
    files = [file for file in os.listdir(images_path) if file.endswith('.jpg')]
    random_image = random.choice(files)
    
    with open(os.path.join(images_path, random_image), 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)

bot.run("MTE4ODQzNzcyMjYwMDMxNjk5OA.G6rMsO._vX8vlCrWRBtoYr4twqBYSukIJcDK4-deJEmxQ")
