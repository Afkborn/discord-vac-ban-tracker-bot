from discord.ext import commands
from python.keys import *
from python.VacLogging import *
from python.Database import Database
from python.PlayerTracker import PlayerTracker
setLogger()
myDatabase = Database()
playerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
bot = commands.Bot(command_prefix='$')

@bot.command()
async def track(ctx, arg):
    if not (playerTracker.checkSteamID(arg)):
        await ctx.send("Error: SteamID is not valid")
        return
    


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



bot.run(DISCORD_API_KEY)
