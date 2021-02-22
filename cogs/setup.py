import discord
from discord.ext import commands
import datetime

class setUp(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.UpTime = datetime.datetime.now()

    @commands.Cog.listener()
    async def on_ready(self):
        print("logged in as")
        print(self.client.user.name)
        print("---------------")
        print("bot is ready!")
        dev = await self.client.fetch_user()
        await dev.send("Bot is ready")
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='ace.help | ace.invite'))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        server_logs_channel = self.client.get_channel()
        embed=discord.Embed(description=f"<:in:813121065110863902> Joined **{guild}**", color=0x1b63ad)
        await server_logs_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            server_logs_channel = self.client.get_channel()
            embed=discord.Embed(description=f"<:out:813121051830517762> Left **{guild}**", color=0x1b63ad)
            await server_logs_channel.send(embed=embed)
        except:
            pass
    @commands.command(aliases = ["p"])
    async def ping(self, ctx):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        embed=discord.Embed(color=0x1b63ad)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms', inline=True)
        await ctx.send(embed=embed)
        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command(aliases = ["gc", "sc","servercount"])
    async def guildcount(self, ctx):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        embed=discord.Embed(color=0x1b63ad)
        embed.add_field(name='Guild count:', value=f'{len(self.client.guilds)} servers', inline=True)
        await ctx.send(embed=embed)
        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command(aliases = ["ut"])
    async def uptime(self, ctx):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        embed=discord.Embed(title="Bots Up Time", description=f"{str(datetime.datetime.now() - self.UpTime)[:-7]}", color=0x1b63ad)
        await ctx.send(embed=embed)
        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)



def setup(client):
    client.add_cog(setUp(client))
