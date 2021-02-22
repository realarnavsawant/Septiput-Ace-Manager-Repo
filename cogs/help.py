import discord
from discord.ext import commands
from discord import Embed

class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["h"])
    async def help(self, ctx, category=None):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        embed=discord.Embed(title="Help", color=0x1b63ad)
        embed.set_author(name="Ace Manager", icon_url="https://cdn.discordapp.com/attachments/361589481847128074/802895352352342016/8584_verified_blue.gif")
        if category is None:
            embed.add_field(name="How to use help:", value='Use `ace.help [category name]` for help on the categories commands and appropriate usage\n [Support Server](https://discord.gg/7evgPefh2h) | [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=799201224384577547&permissions=289856&scope=bot)', inline=False)
            embed.add_field(name="Categories:", value="```\n📔 notes\n➕ math\n📰 summarizer\n🔎 search\n🌎 translator\n🌧️ Weather\n📨 invite``` ", inline=False)

        elif category.lower() == 'notes':
            embed.add_field(name="📔 Notes:", value='Notes are used to stor your notes or set reminders, the bot will stor up to 24 of your notes. Use the commands highlighted below to manipulate your notes', inline=False)
            embed.add_field(name="📔 Note Commands:", value="\n\n ```\nnotes\n```**See all your notes**\nUsage: `ace.notes`\n \n ```\naddnote\n```**Add a note**\nUsage: `ace.addnote [text]`\n \n ```\nremovenote```**Remove a specific note or all notes** \nUsage: `ace.removenote [number]` to remove a specific note and `ace.removenote clear`  to remove all notes", inline=False)

        elif category.lower() == 'math':
            embed.add_field(name="➕ Math:", value='Math is used to solve math equasions like addition (+), subtraction (-), multiplication (*) and devision (/)', inline=False)
            embed.add_field(name="➕ Math Commands:", value="\n\n ```\nmath\n```**Calculate a math equation**\nUsage: `ace.math [equation]`, ex: `ace.math x + 20 = 30`", inline=False)

        elif category.lower() == 'summarizer':
            embed.add_field(name="📰 Summarizer:", value='Summarizer is made ro summarize online news articles', inline=False)
            embed.add_field(name="📰 Summarizer Commands:", value="\n\n ```summarize\n```**Summarize news articles**\nUsage: `ace.summarize [URL]` use the command follwed by a article URL, ex: `ace.summarize https://www.bbc.com/news/technology-55853565`\n", inline=False)

        elif category.lower() == 'search':
            embed.add_field(name="🔎 Search:", value='The search commands can be used to browse the internet', inline=False)
            embed.add_field(name="🔎 Search Commands:", value="\n\n ```\nsearch\n```**Search anything on google**\nUsage: `ace.search [text]`, ex: `ace.search tech with tim`\n \n ```\nwikisearch\n```**Search anything directly from the Wikipedia website**\nUsage: `ace.wikisearch [text]`, ex: `ace.wikisearch python`", inline=False)

        elif category.lower() == 'translator':
            embed.add_field(name="🌎 Translator:", value='Translate text to over 100 languages, Also Let the bot automatically translate any word from any language that is not english.', inline=False)
            embed.add_field(name="🌎 Translator Commands:", value="\n \n ```\ntranslate\n```**Translate messages**\nUsage: `ace.activetranslate -en- hola` to sepcifie the language use '-language-' line -en- for english translation\n \n ```\nactivetranslate on\n```**Enable automatic message traslating to english**\nUsage: `ace.activetranslate on`\n \n ```\nactivetranslate off\n```**Disable automatic message traslating**\nUsage: `ace.activetranslate off`\n ", inline=False)

        elif category.lower() == 'weather':
            embed.add_field(name="🌧️ Weather:", value='Find out what the weather is in a specific location.', inline=False)
            embed.add_field(name="🌧️ Weather Commands:", value="\n \n ```weather\n```**Weather in location**\nUsage: `ace.weather London` sepcifie the location after the command\n ", inline=False)

        elif category.lower() == 'invite':
            embed.add_field(name="📨 Invite:", value='More about Ace Manager\n [Support Server](https://discord.gg/7evgPefh2h) | [Invite Bot](https://discord.com/api/oauth2/authorize?client_id=799201224384577547&permissions=289856&scope=bot)', inline=False)
            embed.add_field(name="📨 Invite Commands:", value="\n\n ```\ninvite\n```**Invite this bot to other servers**\nUsage: `ace.invite`\n \n ```\ndiscord\n```**Join the official Ace discord server**\nUsage: `ace.discord`\n ", inline=False)

        else:
            embed.add_field(name="Invalid category:", value='Use: `ace.help` to see all valid categories', inline=False)

        embed.set_image(url="https://cdn.discordapp.com/attachments/361589481847128074/805440698001129502/ezgif.com-gif-maker_4.gif")
        embed.set_footer(text="Bot made by Septiput and Uap")
        await ctx.send(embed=embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(help(client))
