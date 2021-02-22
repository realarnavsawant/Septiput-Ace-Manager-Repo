import discord
from discord.ext import commands
import nltk
from textblob import TextBlob
from newspaper import Article

class summarizer(commands.Cog):

    def __init__(self, client):
        self.client = client
        nltk.download('punkt')

    @commands.command(aliases = ["s", "summary", "summarizer"])
    async def summarize(self, ctx, url = None):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        try:
            if url is not None:
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()
                analysis = TextBlob(article.text)

                embed=discord.Embed(title="Summarizer", color=0x1b63ad)
                embed.add_field(name="Title:", value=f"```\n{article.title}\n```", inline=False)
                if len(article.authors) >= 1:
                    embed.add_field(name="Authors:", value=f"```\n{', '.join(article.authors)}\n```", inline=False)
                if article.publish_date is not None:
                    embed.add_field(name="Publication Date:", value=f"```\n{article.publish_date}\n```", inline=False)
                embed.add_field(name="Summary:", value=f"```\n{article.summary}\n```", inline=False)
                embed.add_field(name="Sentiment:", value=f"```\n{'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}\n```", inline=False)
                await ctx.send(embed=embed)

            else:
                await ctx.send("You have to add a url after the command")

        except:
            await ctx.send("Sorry ran into a problem. Make shure the url is of a article.")

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(summarizer(client))
