from time import time
from discord.ext import commands
from discord import Embed
from discord import Color
from python.keys import *
from python.VacLogging import *
from python.Database import Database
from python.PlayerTracker import PlayerTracker
from python.Timer import *
setLogger()
myDatabase = Database()
playerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
bot = commands.Bot(command_prefix='$')

@bot.command()
async def track(ctx, arg):
    if not (playerTracker.checkSteamID(arg)):
        await ctx.send("Error: SteamID is not valid")
        return
    player = playerTracker.getPlayer(arg)
    if (player == None):
        await ctx.send("Error: SteamID is not in steam database, check steamid")
        return
    
    playerBan = playerTracker.getPlayerBan(arg)
    if (playerBan == None):
        await ctx.send("Error: SteamID is not in steam database, check steamid")
        return
    
    
    
    myDatabase.addPlayer(player)
    myDatabase.addPlayerBan(playerBan)

    # embedMessage.add_field(name="SteamID", value=player.getSteamID(), inline=False)
    
    if player.getCommunityVisibilityState() == 2:
        embedMessage = Embed(color=Color.red())
        embedMessage.add_field(name="Community Visibility", value="```diff\n-This player is private-```", inline=False)
        embedMessage.set_author(name=f"{player.getPersonaName()}", url=player.getProfileURL(), icon_url=player.getAvatar())
    else:
        playerLevel = playerTracker.getSteamLevel(arg)
        CSGO_total_played = playerTracker.getTotalTimePlayedCSGO(arg) 
        
        embedMessage = Embed(color=Color.blue()) 
        embedMessage.set_author(name=f"{player.getPersonaName()} (Lvl {playerLevel})", url=player.getProfileURL(), icon_url=player.getAvatar())
        embedMessage.add_field(name="Registration Date ", value=f"{player.getYearsTimeCreated()} years ago ({get_time_from_unix(player.getTimeCreated())})", inline=False)#kayıt olma tarihi
        embedMessage.add_field(name="Community Ban", value=f"{playerBan.getCommunityBannedEmoji()}", inline=False)#ban durumu
        embedMessage.add_field(name="Trade Ban", value=f"{playerBan.getEconomyBanEmoji()}",inline =False)
        if (playerBan.getNumberOfGameBans() == 0):
            embedMessage.add_field(name="Game Bans", value=f":x:", inline=False)
        else:
            embedMessage.add_field(name="Game Bans", value=f"{playerBan.getNumberOfGameBans()}", inline=False)
        if (playerBan.getVACBanned()):
            embedMessage.add_field(name=f"VAC Ban", value=f"{playerBan.getNumberOfVACBans()} ban ({playerBan.getDaysSinceLastBan()} days ago)", inline=False)#vac ban tarihi
        else:
            embedMessage.add_field(name="VAC Ban", value=f"{playerBan.getVacBanEmoji()}", inline=False)#ban durumu
        embedMessage.add_field(name="CS GO Total Play Time", value=f"{CSGO_total_played}", inline=False)#oyun zamanı
    
    embedMessage.set_thumbnail(url=player.getAvatarFull())
    embedMessage.set_footer(text=f"I'm following the situation, I'll let you know if there is a change")
    await ctx.send(embed=embedMessage)

    
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))



bot.run(DISCORD_API_KEY)
