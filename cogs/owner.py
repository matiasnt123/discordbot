import discord
from discord.ext import commands

class cogs(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot

    @commands.group(hidden=True)
    @commands.is_owner()
    async def cog(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid subcommand passed.')

    @cog.command()
    async def load(self, ctx, cog_name: str):
        try:
            self.bot.load_extension(cog_name)
        except Exception as e:
            await ctx.send('ERROR: Exception caught. {}'.format(e))
        else:
            await ctx.send("Cog {} loaded successfully.".format(cog_name))

    @cog.command()
    async def unload(self, ctx, cog_name: str):
        try:
            self.bot.unload_extension(cog_name)
        except Exception as e:
            await ctx.send('ERROR: Exception caught. {}'.format(e))
        else:
            await ctx.send("Cog {} unloaded successfully.".format(cog_name))
    

    @cog.command()
    async def reload(self, ctx, cog_name: str):
        try:
            self.bot.reload_extension(cog_name)
        except Exception as e:
            await ctx.send('ERROR: Exception caught. {}'.format(e))
        else:
            await ctx.send("Cog {} reloaded successfully.".format(cog_name))

def setup(bot):
    bot.add_cog(cogs(bot))  