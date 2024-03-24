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

@bot.command()
async def milkihelp(ctx):
    await ctx.send('/hello - bot says her tag')
    await ctx.send('/heh (count) - bot becomes crazy')
    await ctx.send('/repeat (count) (message) - bot sends the message as many times as you wrote')
    await ctx.send('/cool (user mention) - says is guy cool or not')
    await ctx.send('/add (number) (number) - bot adds numbers')
    await ctx.send('/delete (number) (number) - bot subtracts from the number, the second number')
    await ctx.send('/multiply (number) (number) - bot multiplies numbers')
    await ctx.send('/divide (number) (number) - bot divides numbers')
    await ctx.send('/hnick (member mention) (nickname) - changes user nickname(needs administrator and place bots role upper then all roles)')
    await ctx.send('/mem - sends random image from folder, named "images"')
    await ctx.send('/duck - sends random gif/image with duck')
    await ctx.send('/yazanyata - idk what is this')
    await ctx.send('/radiation (language(ru/en/ge/pl/jp)) - bot says about radiation')

@bot.command()
async def radiation(ctx, lang_rad: str):
    if lang_rad == 'ru':
        await ctx.send('Радиация – это излучение в форме частиц или волн, которое может иметь различное происхождение: естественное (космическая радиация, радиоактивные элементы в природе) или искусственное (ядерные взрывы, ядерные реакторы, медицинские процедуры и пр.). Ионизирующая радиация способна взаимодействовать с живыми организмами, вызывая различные последствия, от лучевой болезни до мутаций ДНК. Важно соблюдать меры предосторожности и нормы безопасности при работе с радиацией.')
    if lang_rad == 'en':
        await ctx.send('Radiation is radiation in the form of particles or waves, which can have different origins: natural (cosmic radiation, radioactive elements in nature) or artificial (nuclear explosions, nuclear reactors, medical procedures, etc.). Ionizing radiation can interact with living organisms, causing various consequences, from radiation sickness to DNA mutations. It is important to follow precautions and safety standards when working with radiation.')
    if lang_rad == 'pl':
        await ctx.send('Promieniowanie to promieniowanie w postaci cząstek lub fal, które może mieć różne pochodzenie: naturalne (promieniowanie kosmiczne, pierwiastki promieniotwórcze w przyrodzie) lub sztuczne (wybuchy jądrowe, reaktory jądrowe, procedury medyczne itp.). Promieniowanie jonizujące może oddziaływać z organizmami żywymi, powodując różne konsekwencje, od choroby popromiennej po mutacje DNA. Podczas pracy z promieniowaniem ważne jest przestrzeganie środków ostrożności i norm bezpieczeństwa.')
    if lang_rad == 'ge':
        await ctx.send('Strahlung ist Strahlung in Form von Teilchen oder Wellen, die unterschiedlichen Ursprungs sein kann: natürlich (kosmische Strahlung, radioaktive Elemente in der Natur) oder künstlich (nukleare Explosionen, Kernreaktoren, medizinische Eingriffe usw.). Ionisierende Strahlung kann mit lebenden Organismen interagieren und verschiedene Folgen haben, von Strahlenkrankheit bis hin zu DNA-Mutationen. Bei der Arbeit mit Strahlung ist es wichtig, Vorsichtsmaßnahmen und Sicherheitsstandards zu beachten.')
    if lang_rad == 'jp':
        await ctx.send('放射線は粒子または波の形をした放射線であり、その起源はさまざまです。自然（宇宙​​放射線、自然界の放射性元素）または人工（核爆発、原子炉、医療処置など）です。 電離放射線は生物と相互作用し、放射線障害から DNA 突然変異まで、さまざまな影響を引き起こす可能性があります。 放射線を取り扱う場合は、予防措置と安全基準に従うことが重要です。')


bot.run('token')
