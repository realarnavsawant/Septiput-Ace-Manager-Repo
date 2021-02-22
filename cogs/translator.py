import discord
from discord.ext import commands
import json
from googletrans import Translator
import similar
from launcher import db

class translator(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.autotranslate = db["autotranslate"]
        self.translator = Translator()

    @commands.command(aliases = ["at"])
    async def activetranslate(self, ctx, status = ""):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        if ctx.guild is not None:
            if ctx.author.guild_permissions.administrator:
                id = ctx.guild.id

                if status.lower() == "on":
                    if not self.autotranslate.count_documents({'_id': id}, limit = 1):
                        self.autotranslate.insert_one({"_id": id})
                        await ctx.send("activetranslate on")
                    else:
                        await ctx.send("activetranslate is already on")

                elif status.lower() == "off":
                    if self.autotranslate.count_documents({'_id': id}, limit = 1):
                        self.autotranslate.delete_one({"_id": id})
                        await ctx.send("activetranslate off")
                    else:
                        await ctx.send("activetranslate is already off")

                else:
                    await ctx.send("Add on or off after the command to enable or disable the featur. (ex. `ace.activetranslate on`)")

            else:
                embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command. Only administartors can use this command.", color = 0x1b63ad)
                await ctx.send(embed = embed)

        else:
            embed = discord.Embed(title ="Permission Denied.", description = "You don't have permission to use this command. You can only use this command on a server.", color = 0x1b63ad)
            await ctx.send(embed = embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and message.guild is not None:
            id = message.guild.id
            if self.autotranslate.count_documents({'_id': id}, limit = 1):
                if self.translator.detect(message.content).lang != 'en':
                    await message.channel.send(f'**Detected Language: {self.translator.detect(message.content).lang}** \n{self.translator.translate(message.content, dest="en").text}')

    @commands.command(aliases = ["t"])
    async def translate(self, ctx, lang = None, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")

        prifix = {'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'}

        language_to_prifix = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese': 'zh-cn', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

        try:
            if lang is not None:
                if (lang[0] != '-') and (lang[-1] != '-'):
                    embed=discord.Embed(title="You have to specifie the language", description='You have to specifie the language you wanna use like "en", "es"... and add "-" befor and after the language, ex (`ace.translate -en- hola`)', color=0x1b63ad)
                    await ctx.send(embed=embed)

                elif lang.lower()[1:-1] in prifix:
                    await ctx.send(f'{self.translator.translate(" ".join(args), dest=lang.lower()[1:-1]).text}')

                elif lang.lower()[1:-1] in language_to_prifix:
                    await ctx.send(f'{self.translator.translate(" ".join(args), dest=language_to_prifix[lang.lower()[1:-1]]).text}')

                else:
                    invalid_lang = lang.lower()[1:-1]
                    match = similar.best_match(invalid_lang, language_to_prifix)
                    embed=discord.Embed(title="Invalid Language", description=f'`{invalid_lang}` is a invalid language did you mean `{match}`? Make shure to specifie the language you wanna use like "en", "es"... and add "-" befor and after the language, ex (`ace.translate -en- hola`)', color=0x1b63ad)
                    await ctx.send(embed=embed)

            else:
                embed=discord.Embed(title="Invalid Language", description='Make shure to specifie the language you wanna use like "en", "es"... and add "-" befor and after the language, ex (`ace.translate -en- hola`)', color=0x1b63ad)
                await ctx.send(embed=embed)

        except:
            embed=discord.Embed(title="sorry somthing went wrong", description='Make shure to specifie the language you wanna use like "en", "es"... and add "-" befor and after the language, ex (`ace.translate -en- hola`)', color=0x1b63ad)
            await ctx.send(embed=embed)

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(translator(client))
