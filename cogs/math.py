import discord
from discord.ext import commands
import wolframalpha

class math(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.wolfram = wolframalpha.Client('')

    @commands.command(aliases = ["m"])
    async def math(self, ctx, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        try:
            query = self.wolfram.query(" ".join(args))

            embed = discord.Embed(color=0x1b63ad)
            embed.add_field(name="Input", value=f'```{" ".join(args)}```', inline=False)
            embed.add_field(name="Result", value=f'```{next(query.results).text}```', inline=False)

            try:
                embed.set_image(url=f"{next(query.results)['subpod']['img']['@src']}")
            except:
                try:
                    embed.set_image(url=f"{next(query.results)['subpod'][0]['img']['@src']}")
                except:
                    pass

            await ctx.send(embed=embed)
        except:
            await ctx.send("Sorry, ran into a problem.")

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(math(client))
