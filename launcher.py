import discord
from discord.ext import commands
import os
from pymongo import MongoClient

prifix = ['ace.', 'Ace.', 'a.', 'A.']

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = commands.when_mentioned_or(*prifix), guild_subscriptions = True, intents = intents)
client.remove_command("help")

token = ''

cluster = MongoClient("")
db = cluster["Ace-Manager"]

@client.command()
async def load(ctx, extension = None):
    if ctx.guild is not None:
        if ctx.author.guild_permissions.administrator and ctx.guild.id == 805442964809711656:
            if extension is not None:
                client.load_extension(f'cogs.{extension}')
                await ctx.send(str(extension) + " has been loaded")
            else:
                embed=discord.Embed(title="Error", description=f"Missing a required argument.", color=0x1b63ad)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
        await ctx.send(embed = embed)

@client.command()
async def unload(ctx, extension = None):
    if ctx.guild is not None:
        if ctx.author.guild_permissions.administrator and ctx.guild.id == 805442964809711656:
            if extension is not None:
                client.unload_extension(f'cogs.{extension}')
                await ctx.send(str(extension) + " has been unloaded")
            else:
                embed=discord.Embed(title="Error", description=f"Missing a required argument.", color=0x1b63ad)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
        await ctx.send(embed = embed)

@client.command()
async def reload(ctx, extension = None):
    if ctx.guild is not None:
        if ctx.author.guild_permissions.administrator and ctx.guild.id == 805442964809711656:
            if extension is not None:
                client.unload_extension(f'cogs.{extension}')
                client.load_extension(f'cogs.{extension}')
                await ctx.send(str(extension) + " has been reloaded")
            else:
                embed=discord.Embed(title="Error", description=f"Missing a required argument.", color=0x1b63ad)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
            await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command.", color = 0x1b63ad)
        await ctx.send(embed = embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith("_"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
