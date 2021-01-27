import discord
from discord.ext import commands

class channels(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot

    @commands.command()
    async def delete(self, ctx, messages_quantity:int, flags=""):
        
        silence = lambda flags : "-s" in flags
        force = lambda flags : "-f" in flags

        try:
            messages = await ctx.channel.history(limit=messages_quantity).flatten()
            messages_deleted = len(messages) # used to show total amount of deleted messages
            await ctx.channel.delete_messages(messages)
            if silence:
                pass 
            else:
                await ctx.send("{} messages have been deleted.".format(messages_deleted))
            print("{} messages have been deleted from {} in {}.".format(messages_deleted, ctx.channel, ctx.guild))
        except discord.errors.ClientException:
            await ctx.send("You can't delete more than 100 messages at once.")
        except discord.errors.Forbidden:
            await ctx.send("Bot needs 'manage_messages' permission to do this.")
        except discord.errors.NotFound:
            pass
        except discord.errors.HTTPException:
            if force:
                try:
                    for message in messages:
                        await message.delete()
                except:
                    pass
            else:
                await ctx.send("{} messages have been deleted.".format(messages_deleted))
            print("{} messages have been deleted from {} in {}.".format(messages_deleted, ctx.channel, ctx.guild))    
        except Exception as e:
            await ctx.send("There was an unknown error: {}.".format(str(e)))
            print("Exception caught during delete command: {}".format(str(e)))
    

def setup(bot):
    bot.add_cog(channels(bot))