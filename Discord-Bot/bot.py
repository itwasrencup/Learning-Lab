import discord
from discord.ext import commands
import random 
tips = ["you cant type 'quit' to quit", "eating uranium is an extremely good idea!", "C is superior to C++", "Imagine using windows, cant be me", "Git Gud", "The cake is a lie", 'print("im pretty sure im writing this wrong")', "Im genunely convinced that Artemis 13 is peak", "Domain Expansion: Infinite Random bs", 'helloworld("print") \n \n Syntax Error: Never code again']
intents = discord.Intents.default()
intents.message_content = True
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

bot.run(secret)