from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive
import discord, sys, os
# import logging
# logging.basicConfig(level=logging.INFO)

initial_extensions = [
    "cogs.misc", "cogs.owner", "cogs.good_morning", "cogs.channels"
]

# load discord token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OWNER_1 = int(os.getenv("OWNER_ID_1"))
OWNER_2 = int(os.getenv("OWNER_ID_2"))

bot = commands.Bot(command_prefix="!", owner_ids=[OWNER_1, OWNER_2])

if __name__ == '__main__':
	sys.path.insert(1, os.getcwd() + "/cogs/")

	for extension in initial_extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
	await bot.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.streaming,
	        name="Mi Sexy Chambelán",
	        url="https://www.youtube.com/watch?v=c2ByEeR9Jbg"))

	print('Logged in as {0.user}.'.format(bot))


keep_alive()
bot.run(DISCORD_TOKEN)
