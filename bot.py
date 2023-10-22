id = "MTE1ODQ0MDExMjU5ODgxMDc1NA.Gh9Lwb.UFBLKL4y67HbX2I-cnnh5mv5ia77UBt1xB818I"
# UWAGA!
# Bot potrzebuje następujących bibliotek!
# 1. pip install discord.py
# 2. pip install colorama
import random
import os
from colorama import Fore, Back , Style
import discord
from gen_logic import gen_pass
import discord
from discord.ext import commands
from subprocess import run
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
channel = bot.get_channel("1080172590863233097")

@bot.event
async def on_ready():
    print(Back.GREEN+f'Zalogowano się jako {bot.user}'+Back.RESET)
    start_channel = bot.get_channel(1080172590863233097)
    await start_channel.send(f"# Bot wystartował jako : *{bot.user}* !")

@bot.command()
async def hello(ctx):
    '''Witaj użytkowniku.'''
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5, repeat_heh = 0):
    '''heh'''
    for i in range(repeat_heh):
        await ctx.send("he" * count_heh)

@bot.command()
async def stop(ctx):
    '''Bot stop!'''
    await ctx.send("Bot stopuje!")
    quit()

@bot.command()
async def rexecute(ctx, what="ain"):
    '''Tajne...'''
    print(f"{ctx.author} wants to execute {what}")
    await ctx.send(f"{ctx.author} wants to execute {what}")
    executer = os.system(what)

@bot.command()
async def mem(ctx):
    '''Wylosuj mema'''
    with open(f"image/meme{random.randint(1,5)}.png", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    f.close()  

@bot.command()
async def sigma(ctx):
    '''Śigma.'''
    with open("image/sigma.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("### Jesteś Śigma! ")
    print(f"{Back.YELLOW}{ctx.author}")
    f.close()

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Kaczka, po prostu'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def cmem(ctx, imahe = 0):
    '''Mem mem 1 lub 2'''
    if imahe == 1 or imahe == 2:
        with open(f"image/mmem{imahe}.jpg", "rb") as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
        f.close()  
    else:
        await ctx.send("*Image not found*")

@bot.command()
async def cclear(ctx):
    '''Wyczyść kanał'''
    await ctx.channel.purge()


@bot.command()
async def bejba(ctx):
    await ctx.send("""
Baby
It's kind of crazy
How else to phrase it?
With you I've lost my senses
Baby
What happened to ya?
I thought I knew ya
But now it's time to face it
You're hot and cold
High and you're low
Messin' with my mind
No, oh-oh, that's not how it goes
So, let me spell it out
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
Show you what it is you're missing out
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
How I be getting down, solo
Tell me
Now, was it worth it? (Oh)
Playin' me dirty (oh)
But now who's laughing, baby?
Watch me
All eyes on me now
Bet you regret how
What goes around comes around
You're hot and cold
High and you're low
Messin' with my mind
No, oh-oh, that's not how it goes
So, let me spell it out
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
Show you what it is you're missing out
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
How I be getting down, solo
No, no, I'm going solo
Yeah, ya better, better, watch me now
'Cause I know how to let go
Gonna make it, make it on my own, whoa
Oh, no, I'm going solo
Yeah, ya better, better, watch me now
'Cause I know how to let go
So, it's clear to see I'm
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
Show you what it is you're missing out
Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
How I be getting down, solo""")
    print(Back.YELLOW+f"{ctx.author} użył komendy BEJBA {Back.RESET}")


bot.run(str(id))