import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='<', intents=intents)

Motivasyons = ['Kendinize inandığın sürece, her şey mümkündür', 
               'Başarısızlık, başarıya giden yolda bir basamaktır',
                 'Her yeni gün, yeni bir başlangıçtır bunu unutma',
                   'Hayallerinin peşinden gitmekten asla vazgeçme',
                     'Zorluklar, seni daha güçlü kılar', 
                     'Küçük adımların, Büyük başarıların habercisi olduğunu unutma',
                       'Azmin ve kararlılığının, zaferin anahtarı olduğunu unutma',
                         'Başarının, cesaretinin ve sabrının sonucudur', 
                         'Bugün, geleceğinin ilk günü bugün',
                           'Hedeflerine ulaşmak için asla pes etme', 
                           'Senin için her engel, bir fırsatı gizler',
                             'Kendi yolunu çiz ve ona sadık kalmayı hedefle', 
                             'Başarın, hayal etmekle başlar', 
                             'Her günün, daha iyi bir sen olamk için fırsattır', 
                             'Kendine güven ve adım atmaktan korkma', 
                             'Hayat, cesaretini ödüllendirir merak etme', 
                             'Düşmek, kalkman içindir', 
                             'Senin için her zorluk, birşey öğrenmen için fırsatır', 
                             'İçindeki gücü keşfet ve dünyaya göster']


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def motivasyon_ver(ctx):
    await ctx.send(f' {random.choice(Motivasyons)} {ctx.message.author}.')

@bot.command()
async def yardım(ctx):
    await ctx.send(f'Benim bütün komutlarımda küçük harf kullanırım bunu unutmasan iyi olur {ctx.message.author}.')

@bot.command()
async def selam(ctx):
    await ctx.send(f'Selam!{ctx.message.author}, İyimisin iyi değilsen sana Motivasyon konuşması yapabilirim. Sadece şu komutu gir <motivasyon_ver')

bot.run("Discord Bot Key")

