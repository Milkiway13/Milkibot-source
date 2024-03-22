import discord
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

print(os.listdir('images'))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def delete(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def divide(ctx, left: int, right: int):
    await ctx.send(left / right)

@bot.command()
async def multiply(ctx, left: int, right: int):
    await ctx.send(left * right)
    
@bot.command(pass_context=True)
@commands.has_permissions(change_nickname=True)
async def hnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def yazanyata(ctx):
    await ctx.send('отстаньте!!!')
    
bot.run('token')
