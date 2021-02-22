import discord
from discord.ext import commands
import requests
import json

class weather(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.weather = ''

    @commands.command(aliases = ["w", "temp", "temperature"])
    async def weather(self, ctx, location = None):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        try:
            if location is not None:
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location.lower()}&appid={self.weather}&units=metric'
                data = json.loads(requests.get(url).content)

            embed=discord.Embed(title=f"Weather in {data['name']}", color=0x1b63ad)
            embed.add_field(name="Temperature:", value=f"{data['main']['temp']} °C", inline=False)
            embed.add_field(name="Feels Like:", value=f"{data['main']['feels_like']} °C", inline=False)
            embed.add_field(name="Minimum Temperature:", value=f"{data['main']['temp_min']} °C", inline=False)
            embed.add_field(name="Maximum Temperature:", value=f"{data['main']['temp_max']} °C", inline=False)
            await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Error", description=f"There was an error retriving weather data for {location}.", color=0x1b63ad)
            await ctx.send(embed=embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(weather(client))
