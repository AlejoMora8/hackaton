import discord
import os
import random
import requests
from discord.ext import commands
from botlogic import generador
from botlogic import gira_una_moneda
from botlogic import gen_emoji
from botlogic import dados
from botlogic import ayudas
from botlogic import chistes
from botlogic import get_duck_image_url
from botlogic import get_dog_image_url
from botlogic import get_fox_image_url
API_CLIMA_URL = "https://wttr.in/{city}?format=%C+%t&lang=es"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def gen(ctx):
    await ctx.send(f"Tu contraseña generada es: {generador(10)}")


@bot.command()
async def moneda(ctx):
    await ctx.send(f"La moneda callo y dio: {gira_una_moneda()}")


@bot.command()
async def emogi(ctx):
    await ctx.send(f" {gen_emoji()}")


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def dado(ctx):
    await ctx.send(f"El dado paro de girar y dio: {dados()}")


@bot.command()
async def ayuda(ctx):
    await ctx.send(f" {ayudas()}")


@bot.command()
async def chiste(ctx):
    await ctx.send(f" {(chistes)}")


@bot.command()
async def meme(ctx):
    momazos = os .listdir("images")
    azar = random.choice(momazos)
    with open(f'images/{azar}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck,
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command('dog')
async def dog(ctx):
    '''Una vez que llamamos al comando duck,
    el programa llama a la función get_duck_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


@bot.command('fox')
async def fox(ctx):
    '''Una vez que llamamos al comando duck,
    el programa llama a la función get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)


def obtener_clima(ciudad: str) -> str:
    """
    Devuelve el clima actual de una ciudad usando la API wttr.in.
    """
    url = API_CLIMA_URL.format(city=ciudad)
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.text.strip()
    return "Error: no se pudo obtener la información del clima."


bot.run("TOKEN")
