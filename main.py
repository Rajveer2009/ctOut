from discord.ext import commands
from time import sleep
import discord
import random
import os


client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.command()
async def ping(ctx):
    pingms = float(format(round(client.latency, 1)))
    ping = 0
    if pingms < 1:
        ping = (f"{round(pingms*1000)}μs")
    else:
        ping = (f"{pingms}ms")
    embedVar = discord.Embed(description=(f"Pong! ( Took `{ping}` )"), color=0x5865F2)
    await ctx.send(embed=embedVar)

@client.command()
async def say(ctx, *args):
    arguments = ' '.join(args)
    await ctx.send(arguments)

@client.command()
async def whoami(ctx):
    await ctx.send(ctx.author.display_name)

@client.command()
async def roll(ctx):
    number = random.randint(1, 6)
    index = ["dice-one-1024.png", "dice-two-1024.png", "dice-three-1024.png", "dice-four-1024.png", "dice-five-1024.png", "dice-six-1024.png"]
    picture = (index[(number - 1)])
    await ctx.send(file = discord.File(picture))

@client.command()
async def count(ctx, arg1, arg2):
    agr3 = int(arg1)
    for agr3 in range(agr3):
        await ctx.send(agr3 + 1)
        sleep((int(arg2))/1000)

client.run(DISCORD_TOKEN)