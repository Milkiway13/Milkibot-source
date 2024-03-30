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
    await ctx.send('/radiation (language(lu/en/ge/pl/jp)) - bot says about radiation')
    await ctx.send('/radiation (language(lu/en/jp)) - bot says about fire')

@bot.command()
async def radiation(ctx, lang_rad: str):
    if lang_rad == 'lu':
        await ctx.send('Stralung ass Stralung a Form vu Partikelen oder Wellen, déi verschidden Originen hunn: natierlech (kosmesch Stralung, radioaktiv Elementer an der Natur) oder kënschtlech (Atomexplosiounen, Atomreaktoren, medizinesch Prozeduren, asw.). Ioniséierend Stralung kann mat liewegen Organismen interagéieren, wat verschidde Konsequenzen verursaacht, vu Stralungskrankheet bis DNA Mutatiounen. Et ass wichteg Virsiichtsmoossnamen a Sécherheetsnormen ze verfollegen wann Dir mat Stralung schafft.')
    if lang_rad == 'en':
        await ctx.send('Radiation is radiation in the form of particles or waves, which can have different origins: natural (cosmic radiation, radioactive elements in nature) or artificial (nuclear explosions, nuclear reactors, medical procedures, etc.). Ionizing radiation can interact with living organisms, causing various consequences, from radiation sickness to DNA mutations. It is important to follow precautions and safety standards when working with radiation.')
    if lang_rad == 'pl':
        await ctx.send('Promieniowanie to promieniowanie w postaci cząstek lub fal, które może mieć różne pochodzenie: naturalne (promieniowanie kosmiczne, pierwiastki promieniotwórcze w przyrodzie) lub sztuczne (wybuchy jądrowe, reaktory jądrowe, procedury medyczne itp.). Promieniowanie jonizujące może oddziaływać z organizmami żywymi, powodując różne konsekwencje, od choroby popromiennej po mutacje DNA. Podczas pracy z promieniowaniem ważne jest przestrzeganie środków ostrożności i norm bezpieczeństwa.')
    if lang_rad == 'ge':
        await ctx.send('Strahlung ist Strahlung in Form von Teilchen oder Wellen, die unterschiedlichen Ursprungs sein kann: natürlich (kosmische Strahlung, radioaktive Elemente in der Natur) oder künstlich (nukleare Explosionen, Kernreaktoren, medizinische Eingriffe usw.). Ionisierende Strahlung kann mit lebenden Organismen interagieren und verschiedene Folgen haben, von Strahlenkrankheit bis hin zu DNA-Mutationen. Bei der Arbeit mit Strahlung ist es wichtig, Vorsichtsmaßnahmen und Sicherheitsstandards zu beachten.')
    if lang_rad == 'jp':
        await ctx.send('放射線は粒子または波の形をした放射線であり、その起源はさまざまです。自然（宇宙​​放射線、自然界の放射性元素）または人工（核爆発、原子炉、医療処置など）です。 電離放射線は生物と相互作用し、放射線障害から DNA 突然変異まで、さまざまな影響を引き起こす可能性があります。 放射線を取り扱う場合は、予防措置と安全基準に従うことが重要です。')

@bot.command()
async def fire(ctx, lang_fire: str):
    if lang_fire == 'lu':
        await ctx.send('Bränn sinn eng sérieux Bedrohung, dofir ass et wichteg präventiv Moossnamen ze huelen fir Bränn ze verhënneren. E puer Weeër fir Feier ze vermeiden: 1. Installéiert Rauch- an Hëtztdetektoren dobannen. 2. Erhalen elektresch wiring an elektresch Apparater. 3. Loosst net ageschalt elektresch Apparater ouni Iwwerwaachung. 4. Fëmmt net op verbuedenen Plazen a geheien Zigarettestécker a spezielle Behälter. 5. Brandbar Substanzen a Materialien richteg späicheren. 6. Maacht periodesch Inspektioun a Botzen vu Kamäiner a Belëftungssystemer. No dëse Moossnamen hëlleft dWahrscheinlechkeet vun engem Feier ze reduzéieren an dSécherheet ze garantéieren.')
    if lang_fire == 'en':
        await ctx.send('Fires are a serious threat, so it is important to take preventive measures to prevent fires. Some ways to avoid fires: 1. Install smoke and heat detectors indoors. 2. Maintain electrical wiring and electrical appliances. 3. Do not leave switched on electrical appliances unattended. 4. Do not smoke in prohibited places and throw cigarette butts into special containers. 5. Properly store flammable substances and materials. 6. Carry out periodic inspection and cleaning of chimneys and ventilation systems. Following these measures will help reduce the likelihood of a fire and ensure safety.')
    if lang_fire == 'jp':
        await ctx.send('火災は深刻な脅威であるため、火災を防ぐための予防措置を講じることが重要です。 火災を避けるいくつかの方法: 1. 屋内に煙感知器と熱感知器を設置します。2. 電気配線と電気器具を保守します。3. 電気製品のスイッチを入れたまま放置しないでください。4. 禁止された場所では喫煙せず、吸い殻は専用の容器に捨ててください。5. 可燃性の物質や材料は適切に保管してください。6. 煙突と換気システムの定期的な点検と清掃を実施してください。これらの措置を講じることは、火災の可能性を減らし、安全を確保するのに役立ちます。')



bot.run('token')
