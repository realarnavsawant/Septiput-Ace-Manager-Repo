import discord
from discord.ext import commands
import similar

class error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd = ctx.invoked_with
            cmds = [cmd.name for cmd in self.client.commands]
            match = similar.best_match(cmd, cmds)
            embed=discord.Embed(title="Error", description=f'Command `{cmd}` not found, maybe you meant `{match}`?, use `ace.help` to see all valid commands', color=0x1b63ad)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.DisabledCommand):
            embed=discord.Embed(title="Error", description=f"`{ctx.command}` has been disabled.", color=0x1b63ad)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):
            embed=discord.Embed(title="Error", description=f"`{ctx.command}` is currently on cooldown.", color=0x1b63ad)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title="Error", description=f"Missing a required argument, use `ace.help [category name]` to see all arguments nessery.", color=0x1b63ad)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(title="Error", description=f"Invalid argument, use `ace.help [category name]` to see all the valid arguments.", color=0x1b63ad)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                embed=discord.Embed(title="Error", description=f"`{ctx.command}` can not be used in Private Messages, Try use `{ctx.command}` in a guild.", color=0x1b63ad)
                await ctx.send(embed=embed)

            except discord.HTTPException:
                pass

        else:
            print(str(error))

def setup(client):
    client.add_cog(error(client))
