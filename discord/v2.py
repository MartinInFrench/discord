# -*- coding: ISO-8859-1 -*-
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def fuke(ctx):
    await ctx.send('fuke you {message.author.mention}')
@bot.event
async def on_ready():
    print("Trop ready mec !")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith('salut'):
        # On répond en utilisant l'@mention de l'utilisateur
        await message.channel.send(f"Salut {message.author.mention}!")



bot.run('MTA5MzQ0MTMzNDA0NTU4NTQ4OA.GGmHDD.0IEmsu1BynI5OnsWShpI6uWr3NZgQFd71ekqvc')