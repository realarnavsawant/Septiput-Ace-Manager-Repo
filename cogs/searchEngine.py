import discord
from discord.ext import commands
from googlesearch import search
import wikipedia

class searchEngine(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def search(self, ctx, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        embed = discord.Embed(color=0x1b63ad, timestamp=ctx.message.created_at)
        embed.add_field(name="Top 5 Search Results", value='\n'.join(search(' '.join(args), num_results=5)), inline=False)
        await ctx.send(embed=embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command()
    async def wikisearch(self, ctx, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        embed = discord.Embed(color=0x1b63ad, timestamp=ctx.message.created_at)
        embed.add_field(name=f"Summary of {' '.join(args)} wikipedias page", value=f"```\n{self.wiki_search(' '.join(args))}\n```", inline=False)
        await ctx.send(embed=embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    def wiki_search(self, query):
        try:
            return wikipedia.summary(query, sentences=2)
        except Exception:
            for new_query in wikipedia.search(query):
                try:
                    return wikipedia.summary(new_query, sentences=2)
                except Exception:
                    pass
        return f"I don't know about {search}"

def setup(client):
    client.add_cog(searchEngine(client))
