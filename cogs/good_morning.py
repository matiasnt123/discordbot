import discord, os, re, random, asyncio
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class good_morning(commands.Cog):
    def __init__(self, bot):  # This allows the cog to access the bot, and its functions
        self.bot = bot
        self.channel_id = int(os.getenv("GOOD_MORNING_CHANNEL_ID"))
        self.first_img_path = "resources/good_morning_images/first.jpg"
        self.jokes_path = "resources/good_morning_images/jokes.txt"
        self.days = {
            0: "resources/good_morning_images/monday", # monday
            1: "resources/good_morning_images/tuesday", #tuesday
            2: "resources/good_morning_images/wednesday", #wednesday
            3: "resources/good_morning_images/thursday", #thursday
            4: "resources/good_morning_images/friday", # friday
            5: "resources/good_morning_images/saturday", # saturday
            6: "resources/good_morning_images/sunday" #sunday
            }
        self.good_morning.start()
    
    @tasks.loop(hours=1)
    async def good_morning(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        pattern = "12:..:.."  # 9 AM
        is_time = re.match(pattern, current_time)
        channel = self.bot.get_channel(self.channel_id)
        
        if is_time:
            path = self.days.get(datetime.today().weekday())
            file_to_send = random.choice(os.listdir(path))
            full_path = path + "/" + file_to_send
            
            with open(self.first_img_path, 'rb') as fp:
                await channel.send(file=discord.File(fp, 'preparense.jpg'))
            print("Sending {} to channel {}.".format(self.first_img_path, channel))

            await asyncio.sleep(300)  # 5 minutes

            with open(full_path, 'rb') as fp:
                await channel.send(file=discord.File(fp, 'muy buenas.jpg'))
            print("Sending {} to channel {}.".format(file_to_send, channel))  
            
            joke = random.choice(open(self.jokes_path, encoding="utf8").read().splitlines())
            await channel.send("{} \n\n #humor... :thinking:".format(joke))
            print("Sending joke '{}' to channel {}.".format(joke, channel)) 
    
    @good_morning.before_loop
    async def before_good_morning(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(good_morning(bot))