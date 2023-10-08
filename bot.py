id = "MTE1ODQ0MDExMjU5ODgxMDc1NA.GDVAhV.rfGLVqHyrEwOyLDJZHKrA_fQ564TtbizyEh3lM"

import discord
from gen_logic import gen_pass
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
channel = bot.get_channel("1080172590863233097")
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    start_channel = bot.get_channel(1080172590863233097)
    await start_channel.send(f"# Bot wystartował jako : *{bot.user}* !")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5, repeat_heh = 0):
    for i in range(repeat_heh):
        await ctx.send("he" * count_heh)

@bot.command()
async def stop(ctx):
    await ctx.send("Bot stopuje!")
    quit()

bot.run(str(id))