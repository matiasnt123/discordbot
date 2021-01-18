import discord, asyncio, random
from discord.ext import commands

class voice_channel(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot
        self.ffmpeg_path = "resources/ffmpeg"

    @commands.command()
    async def play(self, ctx):
        try:
            channel = ctx.author.voice.channel
            vc = await channel.connect()
            print('Bot connected to voice chat "{}" on server "{}".'.format(vc.channel, vc.guild))
        except AttributeError:
            await ctx.send("{} is not in a channel.".format(ctx.author))

    @commands.group()
    @commands.is_owner()
    async def vc(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid subcommand passed.')

    @vc.command()
    async def join(self, ctx, voice_channel_id: int):
        try:
            channel = self.bot.get_channel(voice_channel_id)
            vc = await channel.connect()
        except:
            await ctx.send('Channel "{}" does not exist.'.format(voice_channel_id))
        else:
            print('Bot connected to "{}" on server "{}".'.format(vc.channel, vc.guild))
            await ctx.send('Bot connected to "{}" on server "{}".'.format(vc.channel, vc.guild))
        
    @vc.command()
    async def leave(self, ctx):
        try:
            vc = ctx.voice_client
            await vc.disconnect()
            print("Bot disconnected from {}.".format(vc.channel))
            await ctx.send("Bot disconnected from {}.".format(vc.channel))
        except:
            await ctx.send("Bot was not connected to that channel.")

    @vc.command()
    async def play_track(self, ctx, track_name):
        try:
            vc = ctx.voice_client
            track = "resources/tracks/" + track_name
            open(track)
        except IOError as e:
            await ctx.send("That file does not exist.")
            print("Exception caught: {}".format(e))
        except:
            await ctx.send("Bot is not connected to that channel.")
        else:
            await ctx.send("Bot is now playing {} on {}.".format(track_name, vc.guild))
            print("Bot is now playing {} on {}.".format(track_name, vc.guild))
            while vc.is_connected():
                vc.play(discord.FFmpegPCMAudio(executable=self.ffmpeg_path, source=track))
                await asyncio.sleep(random.randint(10, 30))
            
        
def setup(bot):
    bot.add_cog(voice_channel(bot))