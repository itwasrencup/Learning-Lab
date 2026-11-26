import discord
from discord.ext import commands
import random 
import os
import requests
tips = ["you cant type 'quit' to quit", "eating uranium is an extremely good idea!", "C is superior to C++", "Imagine using windows, cant be me", "Git Gud", "The cake is a lie", 'print("im pretty sure im writing this wrong")', "Im genunely convinced that Artemis 13 is peak", "Domain Expansion: Infinite Random bs", 'helloworld("print") \n \n Syntax Error: Never code again']
intents = discord.Intents.default()
intents.message_content = True
secrets = "ho rimosso la chiave prima di committare"
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def dice(ctx):
    await ctx.send(f"Dal lancio del dato e' uscito: {random.randint(1, 6)}")
@bot.command()
async def quote(ctx):
    await ctx.send(random.choice(tips))
@bot.command()
async def rickroll(ctx):
    await ctx.send("https://boulderbugle.com/breaking-scientists-officially-confirm-aliens-exist-hz5O8f8G")
@bot.command()
async def searchyt(ctx, ytext):
    clean = ytext.replace(" ", "+")
    # print(ytext)
    await ctx.send(f"il link che stai cercando: https://www.youtube.com/results?search_query={clean}")
@bot.command()
async def opendemonlist(ctx, demonlist):
    if demonlist == "Global":
        await ctx.send("https://demonlist.org/classic")
    elif demonlist == "Pointercrate":
        await ctx.send("https://www.pointercrate.com/demonlist/")
    elif demonlist == "Aredl":
        await ctx.send("https://aredl.net/list/149992717")
    else:
        await ctx.send(" https://soggy.cat/ (Nessuna Demonlist trovata, sicuro di averla scritta bene?)")


@bot.command()
async def domath(ctx, num1, operator, num2):
    try:
        num1 = int(num1)
    except:
        await ctx.send("Errore: NaN")
        return 
    try:
        num2 = int(num2)
    except:
        await ctx.send("Errore: NaN")
        return
    
    try:
        if operator == "/":
            await ctx.send(f"il risultato e' {num1/num2}")
            return
        if operator == "x":
            await ctx.send(f"il risultato e' {num1*num2}")
            return
        if operator == "+":
            await ctx.send(f"il risultato e' {num1+num2}")
            return
        if operator == "-":
            await ctx.send(f"il risultato e' {num1-num2}")
            return
        else:
            await ctx.send("Errore: l'operatore non e' valido, usa /, x, +, o -")
            return
    except:
        await ctx.send("Errore: Formato invalido o dato mancante: il formato e': Numero1 + Operatore + Numero2")

@bot.command()
async def rcs(ctx, difficulty, choice):
    try:
        if difficulty == "impossible":
            try:
                if choice == "Rock":
                    await ctx.send("Il Bot ha scelto Carta e tu Roccia, GGs ")
                    return
                elif choice == "Paper":
                    await ctx.send("il Bot ha scelto Forbice e tu Carta, GGs")
                    return
                elif choice == "scissors":
                    await ctx.send("il Bot ha scelto Roccia e tu Forbici, GGs")
                    return
                elif choice == "Thermonuclear Bomb":
                    await ctx.send("Hai evaporizzato il bot con una bomba Termonucleare, GGs")
                    return
                else:
                    await ctx.send(f"Errore: {choice} non e' valido (scegli tra Rock, Paper, Scissors, e Thermonuclear Bomb)")
                    return
            except:
                await ctx.send("Errore: Scelta non inserita")
                return
        elif difficulty == "Normal":
            botchoice = random.choice(["Rock", "Paper", "Scissors"])
            if choice not in ["Rock", "Paper", "Scissors"]:
                await ctx.send(f"Errore: {choice} non e' valido (scegli tra Rock, Paper, e Scissors)")
            elif botchoice == choice:
                await ctx.send(f"Il bot ha scelto {botchoice}, e tu {choice}, quindi e' patta, GGs")
            elif (botchoice == "Rock" and choice == "Paper") or (botchoice == "Paper" and choice == "Scissors") or (botchoice == "Scissors" and choice == "Rock"):
                await ctx.send(f"Il bot ha scelto {botchoice}, e tu {choice}, hai vinto, GGs")
            else:
                await ctx.send(f"Il bot ha scelto {botchoice}, e tu {choice}, hai perso, GGs")
    except:
        await ctx.send("Errore: qualcosa e' andato storto")

@bot.command()
async def mempick(ctx):
    # avaiable_images = ["1.jpg", '2.jpg', '3.jpg', '4.jpg', '5.png']
    dir = 'Discord-Bot/images/'
    all_pictures = os.listdir(dir)
    # print(all_pictures)
    selected_picture = random.choice(all_pictures)
    with open(f'Discord-Bot/images/{selected_picture}', 'rb') as f:
        # Memorizziamo il file della libreria di Discord convertito in questa variabile!
        picture = discord.File(f)
   # Possiamo quindi inviare questo file come parametro!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_cat_image_url():    
    url = 'https://cataas.com/cat?position=center&json=true'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_ultracat_image_url(textt): 
    texttt = textt.replace(' ', '%20')
    url = f'https://cataas.com/cat/says/{texttt}?position=center&json=true&font=Impact&fontSize=50&fontColor=%23fff&fontBackground=none'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('gitcat')
async def gitcat(ctx):
    '''Una volta chiamato il comando gitcat, il programma richiama la funzione get_cat_image_url'''
    image_url = get_cat_image_url()
    await ctx.send(image_url)

@bot.command('catadvanced')
async def catadvanced(ctx, text):
    '''Una volta chiamato il comando gitcat, il programma richiama la funzione get_cat_image_url'''
    image_url = get_ultracat_image_url(text)
    await ctx.send(image_url)

bot.run(secret)