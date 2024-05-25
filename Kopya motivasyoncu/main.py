import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='<', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Tavsiye(ctx):
    await ctx.send(f'Başarının anahtarı Her zaman içindedir, Fakat önemli olan bunu farkedebilmektedir {ctx.message.author}.')

@bot.command()
async def Selam (ctx):
    await ctx.send(f'Selam!{ctx.message.author}, İyimisin iyi değilsen sana Motivasyon konuşması yapabilirim!')

bot.run("DCBot Key")

