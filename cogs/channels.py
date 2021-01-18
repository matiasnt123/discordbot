import discord
from discord.ext import commands

class channels(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot

    @commands.command()
    async def delete(self, ctx, messages_quantity: int):
        channel = ctx.channel  
        try:
            messages = await channel.history(limit=messages_quantity).flatten()
            messages_deleted = messages
            await channel.delete_messages(messages)
        except discord.errors.ClientException:
            await ctx.send("You can't delete more than 100 messages at once.")
        except discord.errors.Forbidden:
            await ctx.send("Bot needs 'manage_messages' permission to do this.")
        except discord.errors.NotFound:
            pass
        except discord.errors.HTTPException:
            try:
                for message in messages:
                    await message.delete()
            except:
                pass
            await ctx.send("{} messages have been deleted.".format(len(messages_deleted)))
            print("{} messages have been deleted from {} in {}.".format(len(messages_deleted), ctx.channel, ctx.guild))
        except Exception as e:
            await ctx.send("There was an unknown error.")
            print("Exception caught during delete command: {}".format(e))
        else:
            await ctx.send("{} messages have been deleted.".format(len(messages_deleted)))
            print("{} messages have been deleted from {} in {}.".format(len(messages_deleted), ctx.channel, ctx.guild))    

def setup(bot):
    bot.add_cog(channels(bot))