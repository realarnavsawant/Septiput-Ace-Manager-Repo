import discord
from discord.ext import commands
import pymongo
from launcher import db

class notes(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.notes = db["notes"]

    @commands.command(aliases = ["an"])
    async def addnote(self, ctx, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        id = ctx.author.id
        msg = " ".join(args)

        if not msg == "":
            if len(msg) <= 245:

                if not self.notes.count_documents({'_id': id}, limit = 1):
                    self.notes.insert_one({"_id": id}, {"notes": []})
                    self.notes.update_one({"_id": id}, {"$push":{"notes": msg}})
                    await ctx.send(f'added `{" ".join(args)}` to notes')

                else:
                    lenNotes = self.notes.find_one({"_id": id})
                    if len(lenNotes['notes']) < 24:
                        self.notes.update_one({"_id": id}, {"$push":{"notes": msg}})
                        await ctx.send(f'added `{msg}` to notes')
                    else:
                        await ctx.send(f'You can only have a max of 24 notes. You can use ace.notes to see your notes or ace.removenote to remove a note')

            else:
                await ctx.send(f'Your note has exided the max 245 charecters. Add a note with 245 charecters or less please.')
        else:
            await ctx.send(f'You provided no note. Try `ace.addnote "note here"` to add a note.')

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command(aliases = ["rn"])
    async def removenote(self, ctx, index = None):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        id = ctx.author.id
        result = self.notes.find_one({"_id": id})

        if not self.notes.count_documents({'_id': id}, limit = 1):
            await ctx.send("You have no notes. use `ace.addnote [your note]` to add a note.")

        if index == "clear":
            self.notes.delete_one({"_id": id})
            await ctx.send('Cleard all notes')

        elif int(index) >= 1 and int(index) <= 24 and int(index) <= len(result['notes']):
            self.notes.update_one({"_id": id}, {"$pull": {"notes": result['notes'][int(index) - 1]}})

            await ctx.send(f'Removed note `{index}` from notes')

        elif not int(index) <= len(result['notes']):
            await ctx.send(f"You dont have {int(index)} notes you only have {len(result['notes'])}. Enter `ace.removenote {len(result['notes'])}` or less.")

        else:
            await ctx.send('Add the number of the note you wanna remove (<= 24)or clear to clear all notes, example (ace.removenote 1)')

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

    @commands.command(aliases = ["n"])
    async def notes(self, ctx, *args):
        await ctx.message.add_reaction("<a:loadingdots:805521532529016882>")
        id = ctx.author.id

        if not self.notes.count_documents({'_id': id}, limit = 1):
            await ctx.send("You have no notes. use `ace.addnote [your note]` to add a note.")

        else:
            notes_dict = self.notes.find_one({"_id": id})
            note = notes_dict['notes']
            if len(note) > 0:
                embed = discord.Embed(title="Notes", color=0x1b63ad, timestamp=ctx.message.created_at)
                embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
                for index, item in enumerate(note, start=1):
                    embed.add_field(name=f"{index}.", value=f"{item}", inline=False)
                    if index >= 24:
                        embed.set_footer(text="You can only have 24 notes max")
                        break
                await ctx.send(embed=embed)
            else:
                await ctx.send("You have no notes")

        await ctx.message.remove_reaction("<a:loadingdots:805521532529016882>", self.client.user)

def setup(client):
    client.add_cog(notes(client))
