from time import mktime, time
from discord.ext import commands
from discord import Embed, Color, Game
from threading import Thread


from python.TextFunction import splitTextByLength
from python.globalVariables import *
from python.VacLogging import *
from python.BotDatabase import Database
from python.SteamAPI_Service import SteamAPI_Service
from python.Timer import *
from python.Model.DiscordUser import DiscordUser
from python.Model.Track import Track
from python.SteamCountries import *
from python.SteamGames import *
from python.Tracker import Tracker

setLogger()

myDatabase = Database()
steamAPI_service = SteamAPI_Service()
myTracker = Tracker()
bot = commands.Bot(command_prefix='$')



@bot.command()
async def track(message, arg):
    if not (steamAPI_service.checkSteamID(arg)):
        await message.send("Error: SteamID is not valid")
        return
    
    player = steamAPI_service.getPlayer(arg)
    if (player == None):
        await message.send("Error: SteamID is not in steam database, check steamid")
        return
    
    playerBan = steamAPI_service.getPlayerBan(arg)
    if (playerBan == None):
        await message.send("Error: SteamID is not in steam database, check steamid")
        return
    
    myDatabase.addPlayer(player)
    myDatabase.addPlayerBan(playerBan)

    if player.getCommunityVisibilityState() == 2:
        embedMessage = Embed(color=Color.red())
        embedMessage.add_field(name="Community Visibility", value="```diff\n-This player is private-```", inline=False)
        embedMessage.add_field(name="STATUS",value="I CANT SEE THIS PLAYER", inline=False)
        embedMessage.set_author(name=f"{player.getPersonaName()}", url=player.getProfileURL(), icon_url=player.getAvatar())
    elif player.getCommunityVisibilityState() == 3:
        playerLevel = steamAPI_service.getSteamLevel(arg)
        CSGO_total_played = steamAPI_service.getTotalTimePlayedCSGO(arg) 
        embedMessage = Embed(color=Color.blue()) 
        embedMessage.set_author(name=f"{player.getPersonaName()} (Lvl {playerLevel})", url=player.getProfileURL(), icon_url=player.getAvatar())
        date, type = player.getYearsTimeCreated()
        embedMessage.add_field(name="Registration Date ", value=f"{date} {type}  ago ({get_time_from_unix(player.getTimeCreated())})", inline=False)
            
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
            
            if countryStateCityName != None and countryStateCityName != countryStateName:
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
    
    trackObj = Track(ownerDiscordID=message.author.id, steamID=player.getSteamID(), time=time(), channel_id=message.channel.id)
    result = myDatabase.addTrack(trackObj)

    embedMessage.set_thumbnail(url=player.getAvatarFull())
    embedMessage.set_footer(text=f"I'm following the situation, I'll let you know if there is a change")
    await message.send(embed=embedMessage)
    if (result == False):
        await message.send("Error: This account is already tracked, please use $untrack <STEAM_ID, Vanity_URL, STEAM2_ID> to untrack it")
    

@bot.command()
async def game(message,arg):
    try:
        gameID = int(arg)
        result = steamAPI_service.getGameWithID(gameID)
        if (len(result) > 2000):
            splitedText = splitTextByLength(result, 2000)
            for text in splitedText:
                await message.send(text)
        else:
            await message.send(f"{result}") 
        
    except:
        await message.send("Error: GameID is not valid")

@bot.command()
async def find_game(message,*args):
    arg = " ".join(args)
    resultList = myDatabase.getGameWithName(arg)
    text = f"I found {len(resultList)} results for {arg}\n"
    for index ,game in enumerate(resultList,start=1):
        text += f"{index}. {game.getName()} (ID:{game.getAppID()})\n"
    text += "If you want to see more information about a game, use $game <gameID>"
    if (len(text) > 2000):
        splitedText = splitTextByLength(text,2000)
        for text in splitedText:
            await message.send(text)
    else:
        await message.send(text)
    

@bot.command()
async def config(message):
    if (message.author.id == ADMIN_DISCORD_ID):
        await message.send(f"""TRACK_SLEEP_TIME: {myTracker.getTrackSleepTime()}
TRACK_CHECK_TIME: {myTracker.getTrackCheckTime()}
Change the values by using $setconfig <config_name> <value>""")
    else:
        await message.send("You are not authorized to use this command")

@bot.command()
async def setconfig(message,config_name,value):
    if (message.author.id == ADMIN_DISCORD_ID):
        if (config_name == "TRACK_SLEEP_TIME"):
            myTracker.setTrackSleepTime(int(value))
            await message.send(f"TRACK_SLEEP_TIME: {myTracker.getTrackSleepTime()}")
        elif (config_name == "TRACK_CHECK_TIME"):
            myTracker.setTrackCheckTime(int(value))
            await message.send(f"Set Track Check Time to {myTracker.getTrackCheckTime()}")
                
    else:
        await message.send("Error: You are not authorized to change the config")


# @bot.event
# async def on_command_error(message, error):
#     print(error)
#     await message.send(f"An error occured: {str(error)}")

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


tracker = Thread(target=myTracker.setTracker)
tracker.start()

bot.run(DISCORD_API_KEY)
