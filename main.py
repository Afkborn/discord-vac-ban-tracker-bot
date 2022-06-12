from time import mktime, time
from discord.ext import commands
from discord import Embed, Color, Game

from python.globalVariables import *
from python.VacLogging import *
from python.Database import Database
from python.PlayerTracker import PlayerTracker
from python.Timer import *
from python.Model.DiscordUser import DiscordUser
from python.GetCountryDetail import *
setLogger()

myDatabase = Database()
playerTracker = PlayerTracker(STEAM_API_KEY=STEAM_API_KEY)
bot = commands.Bot(command_prefix='$')

@bot.command()
async def track(message, arg):
    if not (playerTracker.checkSteamID(arg)):
        await message.send("Error: SteamID is not valid")
        return
    
    player = playerTracker.getPlayer(arg)
    if (player == None):
        await message.send("Error: SteamID is not in steam database, check steamid")
        return
    
    playerBan = playerTracker.getPlayerBan(arg)
    if (playerBan == None):
        await message.send("Error: SteamID is not in steam database, check steamid")
        return
    
    myDatabase.addPlayer(player)
    myDatabase.addPlayerBan(playerBan)

    if player.getCommunityVisibilityState() == 2:
        embedMessage = Embed(color=Color.red())
        embedMessage.add_field(name="Community Visibility", value="```diff\n-This player is private-```", inline=False)
        embedMessage.set_author(name=f"{player.getPersonaName()}", url=player.getProfileURL(), icon_url=player.getAvatar())
    elif player.getCommunityVisibilityState() == 3:
        playerLevel = playerTracker.getSteamLevel(arg)
        CSGO_total_played = playerTracker.getTotalTimePlayedCSGO(arg) 
        embedMessage = Embed(color=Color.blue()) 
        embedMessage.set_author(name=f"{player.getPersonaName()} (Lvl {playerLevel})", url=player.getProfileURL(), icon_url=player.getAvatar())
        embedMessage.add_field(name="Registration Date ", value=f"{player.getYearsTimeCreated()} years ago ({get_time_from_unix(player.getTimeCreated())})", inline=False)
        embedMessage.add_field(name="Status", value=f"{player.getPersonaStateText()}", inline=False)
        
        embedMessage.add_field(name="Community Ban", value=f"{playerBan.getCommunityBannedEmoji()}", inline=False)
        embedMessage.add_field(name="Trade Ban", value=f"{playerBan.getEconomyBanEmoji()}",inline =False)
        if (playerBan.getNumberOfGameBans() == 0):
            embedMessage.add_field(name="Game Bans", value=f":x:", inline=False)
        else:
            embedMessage.add_field(name="Game Bans", value=f"{playerBan.getNumberOfGameBans()}", inline=False)
        if (playerBan.getVACBanned()):
            embedMessage.add_field(name=f"VAC Ban", value=f"{playerBan.getNumberOfVACBans()} ban ({playerBan.getDaysSinceLastBan()} days ago)", inline=False)
        else:
            embedMessage.add_field(name="VAC Ban", value=f"{playerBan.getVacBanEmoji()}", inline=False)  
            
        if (player.getRealName() != None):
            embedMessage.add_field(name="Real Name", value=f"{player.getRealName()}", inline=False)
        if (player.getLocCountryCode() != None):
            countryName, countryStateName, countryStateCityName = getCountryDetail(player.getLocCountryCode(), player.getLocStateCode(), player.getLocCityID())
            fullText = ""
            if countryStateCityName != None:
                fullText += f"{countryStateCityName}, "
            if countryStateName != None:
                fullText += f"{countryStateName}, "
            if countryName != None:
                fullText += f"{countryName}"
            embedMessage.add_field(name="Location", value=f"{fullText} :flag_{player.getLocCountryCode().lower()}:", inline=False)
        if (CSGO_total_played != None):
            embedMessage.add_field(name="CS GO Total Play Time", value=f"{CSGO_total_played}", inline=False) 
        
    else:
        embedMessage = Embed(color=Color.red())
        embedMessage.add_field(name="Community Visibility", value="```diff\n-This player is private-```", inline=False)
        embedMessage.set_author(name=f"{player.getPersonaName()}", url=player.getProfileURL(), icon_url=player.getAvatar())
        
    embedMessage.set_thumbnail(url=player.getAvatarFull())
    embedMessage.set_footer(text=f"I'm following the situation, I'll let you know if there is a change")
    await message.send(embed=embedMessage)


@bot.command()
async def config(message):
    if (message.author.id == ADMIN_DISCORD_ID):
        await message.send(f"PRINT CONFIG")

# @bot.event
# async def on_command_error(message, error):
#     print(error)
#     await message.send(f"An error occured: {str(error)} {error.__class__}")

@bot.event
async def on_ready():
    print(f" Logged in as  : {bot.user.name}")
    print(f" Bot ID        : {bot.user.id}")
    await bot.change_presence(activity=Game(name=""))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    authorObj = DiscordUser(discordID=message.author.id,
                            name=message.author.name,
                            avatar_url=message.author.avatar_url,
                            joined_at=time(),
                            created_at=mktime(message.author.created_at.timetuple()))
    myDatabase.addDiscordUser(authorObj)
    
    if len(message.content) < 256:
        print(f" {get_time_command()},{message.guild.name}| {message.author.name} = {message.content}")
    else:
        print(f" {get_time_command()},{message.guild.name}| {message.author.name} = Too long message")

    await bot.process_commands(message)


bot.run(DISCORD_API_KEY)
