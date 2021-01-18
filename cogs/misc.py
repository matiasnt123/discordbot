import discord, aiohttp
from datetime import datetime
from dadjokes import Dadjoke
from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        self.latency = self.bot.latency
        await ctx.send("Pong.\n" + str(self.latency))
    
    @commands.command()
    async def insult(self, ctx, lang="es"):
      async with aiohttp.ClientSession() as session:
        url = "https://evilinsult.com/generate_insult.php?lang=" + lang + "&type=json"
        async with session.get(url) as json_response:
          if json_response.status == 200:
            insult = await json_response.json()
            await ctx.send(insult['insult'])
    
    @commands.command()
    async def time(self, ctx):
      current_time = datetime.now()
      await ctx.send("Current time: {}".format(current_time))

    @commands.command()
    async def joke(self, ctx):
      dadjoke = Dadjoke()
      await ctx.send(dadjoke.joke)
    
    @commands.command()
    async def kanye(self, ctx, lang="es"):
      async with aiohttp.ClientSession() as session:
        async with session.get("https://api.kanye.rest/") as json_response:
          if json_response.status == 200:
            quote = await json_response.json()
            await ctx.send(quote['quote'])
      

def setup(bot):
    bot.add_cog(misc(bot))