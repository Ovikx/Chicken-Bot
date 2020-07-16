# clientID = 672134264124473345
inviteLink = 'https://discordapp.com/api/oauth2/authorize?client_id=672134264124473345&scope=bot&permissions=262208'

# IMPORT STUFF
import discord
from discord.ext import commands

# READ TOKEN FROM FILE
with open('chickenToken.txt', 'r') as tokenF: # make sure the .txt file that contains the token is called 'chickenToken.txt'
    token = tokenF.read()

# CREATE BOT OBJECT
bot = commands.Bot(command_prefix='!', case_insensitive=True) # change the prefix if you want ig

# READY THE BOT
@bot.event
async def on_ready():
    game = discord.Game('C L U C K') # the string can be changed to your liking
    print(f"Client logged in as {bot.user} in {len(bot.guilds)} servers") # this string can also be changed to your liking
    await bot.change_presence(status=discord.Status.online, activity=game)

# ADD THE 🐔!!!
@bot.event
async def on_message(msg):
    await msg.add_reaction(emoji='🐔')

# RUN THE BOT
bot.run(token)