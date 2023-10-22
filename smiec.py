id = ""
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

smieci = {
    "plastik": "żółty",
    "papier": "niebieski",
    "warzywo": "brązowy",
    "szkło": "zielony",
    "mieszane": "szary",
    "puszka": "żółty",
    "gazeta": "niebieski",
    "bio": "brązowy",
    "szklany": "zielony",
    "ceramika": "szary"
}
pojemniki = {
    "zielony":"""W niektórych przypadkach wciąż stosuje się podział na szkło bezbarwne (kolor biały) i kolorowe (zieleń). Do zielonego pojemnika na śmieci możemy wyrzucać szklane opakowania, słoiki oraz szklane butelki po napojach, w tym alkoholowych. Nie można jednak wrzucać zniczy z woskiem, nieopróżnionych do końca opakowań po lekach, olejach czy rozpuszczalnikach oraz żarówek.""",
    "żółty": """W koszu można bez problemu umieszczać zgniecione butelki plastikowe oraz nakrętki (osobno, plastikowe butelki nie mogą być zakręcone), plastikowe opakowania po produktach spożywczych, torebki, worki i różnego rodzaju folie (w tym folia aluminiowa)""",
    "niebieski": """Pojemnik w kolorze niebieskim przeznaczony jest na różnego rodzaju czysty papier, na przykład w formie zrobionych z tego materiału torebek, worków czy folderów. Tu wrzucimy gazety, czasopisma, zeszyty, książki oraz opakowania z papieru i tektury. Pozbędziemy się tu też różnego rodzaju zbędnych katalogów i prospektów, wyrzucimy też papier pakowy.""",
    "brązowy": """Pojemnik na odpady biodegradowalne w założeniu przeznaczony jest na śmieci pochodzące z gospodarstw domowych. Do niego wrzucimy resztki jedzenia, takie jak odpadki warzywne i owocowe, fusy po herbacie i kawie oraz skorupki jaj. Jest to także miejsce na wszelkie zwiędłe rośliny doniczkowe, w tym kwiaty. Możliwe jest również wyrzucanie tu pozostałości z rearanżacji ogródka, takich jak kora drzew, skoszona trawa, gałęzie, trociny i surowe, niezaimpregnowane drewno.""",
    "czarny": """Do odpadów zmieszanych może trafić bardzo wiele ze śmieci, które nie mogły zostać odpowiednio posegregowane lub nie spełniają wymogów poszczególnych pojemników. Do pojemnika na odpady zmieszane można wrzucać na przykład resztki mięsa i kości zwierząt, silnie zabrudzone worki papierowe czy zużyte artykuły higieniczne. To także miejsce na żwirek z kuwet i klatek, potłuczone szkło oraz tekstylia.""",
    "inne": """Jeśli dana kategoria przedmiotów nie mogła zostać umieszczona w koszach na odpady segregowane i w pojemniku na odpady zmieszane, należy poszukać odpowiedniego sposobu pozbycia się wchodzących w jej skład śmieci."""
}
@bot.event
async def on_ready():
    print(Back.GREEN+f'Zalogowano się jako {bot.user}'+Back.RESET)
    start_channel = bot.get_channel(1080172590863233097)
    await start_channel.send(f"# Bot wystartował jako : *{bot.user}* !")

@bot.command()
async def pomoc(ctx):
    await ctx.send("# Cześć!")
    await ctx.send("## Hej kolego!")
    await ctx.send("""### Pomogę ci posegregować twoje śmieci!
Spróbuj wpisać to:
!smiec - wpisz z czego jest zrobiony twój śmieć i bot ci pomoże
!pojemnik - pisze co można wrzucić do danego pojemnika
!obrazek - wysyła losowy obrazek związany z recyklingiem
!stop - stop bota""")
    
@bot.command()
async def smiec(ctx, smiec = "bejba"):
    if smiec.lower() in smieci.keys():
        await ctx.send("Znaleziono przedmiot")
        await ctx.send(f"Wrzuć ten przedmiot do {smieci[smiec.lower()]} pojemnik")
    else:
        listaaa = []
        for i in smieci.keys():
            listaaa.append(i)
        await ctx.send(listaaa)
        await ctx.send("Następnym razem wybierz jedno z tych na górze!")

@bot.command()
async def pojemnik(ctx, pojemnik = "bejba"):
    if pojemnik.lower() in pojemniki.keys():
        await ctx.send("Znaleziono pojemnik")
        await ctx.send(pojemniki[pojemnik.lower()])
    else:
        pojemnikilist = []
        await ctx.send("Nie znaleziono pojemnika")
        for e in pojemniki.keys():
            pojemnikilist.append(e)
        await ctx.send(pojemnikilist)
        await ctx.send("Następnym razem wybierz jeden z tych pojemników na górze!")

@bot.command()
async def obrazek(ctx):
    with open(f"image/smiec{random.randint(1,3)}.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    f.close()

@bot.command()
async def stop(ctx):
    await ctx.send("Pa pa! Brumbrummmmm")
    print("!WYJŚCIE!")
    quit()





bot.run("")