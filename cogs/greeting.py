import discord
from discord.ext import commands
from launcher import db
import random

class greeting(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.activegreeting = db["activegreeting"]

    @commands.command(aliases = ["ag"])
    async def activegreeting(self, ctx, status = ""):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        if ctx.guild is not None:
            if ctx.author.guild_permissions.administrator:
                id = ctx.guild.id

                if status.lower() == "on":
                    if not self.activegreeting.count_documents({'_id': id}, limit = 1):
                        self.activegreeting.insert_one({"_id": id})
                        await ctx.send("active greeting on")
                    else:
                        await ctx.send("active greeting is already on")

                elif status.lower() == "off":
                    if self.activegreeting.count_documents({'_id': id}, limit = 1):
                        self.activegreeting.delete_one({"_id": id})
                        await ctx.send("active greeting off")
                    else:
                        await ctx.send("active greeting is already off")

                else:
                    await ctx.send("Add on or off after the command to enable or disable the featur. (ex. `ace.activegreeting on`)")

            else:
                embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command. Only administartors can use this command.", color = 0x1b63ad)
                await ctx.send(embed = embed)

        else:
            embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command. You can only use this command on a server.", color = 0x1b63ad)
            await ctx.send(embed = embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.guild is not None:
                id = message.guild.id
                if self.activegreeting.count_documents({'_id': id}, limit = 1):
                    try:
                        content = {"hello", "hi"}
                        if message.content.lower() in content:
                            greeting = ["Hello", "Hello There", "Hi", "Hi There"]
                            await message.channel.send(random.choice(greeting))
                    except:
                        pass
            else:
                try:
                    content = {"hello", "hi"}
                    if message.content.lower() in content:
                        greeting = ["Hello", "Hello There", "Hi", "Hi There"]
                        await message.channel.send(random.choice(greeting))
                except:
                    pass

def setup(client):
    client.add_cog(greeting(client))
