import discord
from discord.ext import commands

class inviter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["i"])
    async def invite(self, ctx):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        embed=discord.Embed(title="Invite Bot", description="[Invite Link](https://discord.com/api/oauth2/authorize?client_id=799201224384577547&permissions=289856&scope=bot)", color=0x1b63ad)
        await ctx.send(embed=embed)       
        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command(aliases = ["d"])
    async def discord(self, ctx):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        embed=discord.Embed(title="Official Support Server", description="[Support Server Invite Link](https://discord.gg/7evgPefh2h)", color=0x1b63ad)
        await ctx.send(embed=embed)
        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(inviter(client))
