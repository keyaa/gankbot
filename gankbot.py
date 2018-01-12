# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import feedparser

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665, adapted for use by 'plz enjoy game#6067'.", command_prefix=">", pm_help = True)
f=open("../botkey.txt")
for l in f:
    l=l.strip()
client_token=l	# this is to keep the token private

weebcounter = 0	# these counters are for the reddit feeds
haikucounter = 0
keebcounter = 0
mecounter = 0
videocounter = 0
codecounter = 0

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('Created by Habchy#1665')
	print("Adapted for use by 'plz enjoy game#6067'")

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.event
async def on_message(message):
	if message.content.startswith(">help"):	# help dialogue
		await client.send_message(message.author, "**------ Commands ------**\n\
Prefix all commands with > character.\n\
# character is optional, specifies number to repeat.\n\
ping: 		Generic response test for robot.\n\
stop: 		Stop current audio and leave voice channel.\n\
play 'link': 		Starts playing Youtube link _(must be in voice channel)_.\n\
oof #: 		Roblox death sound _(must be in voice channel, limit 10)_.\n\
OOF #: 		Loud Roblox death sound _(must be in voice channel, limit 3)_.\n\
thot #:		Begone, thot! _(must be in voice channel, limit 3)_.\n\
THOT #: 		***BEGONE, THOT!*** _(must be in voice channel, limit 1)_.\n\
quack #:		Duck noise _(must be in voice channel, limit 10)_.\n\
git #:		git text-to-speech _(must be in voice channel, limit 10)_.\n\
woop #: 		Unknown noise _(must be in voice channel, limit 10)_.\n\
weeb #: 		Fetches most recent post on r/awwnime _(limit 3)_.\n\
keeb #: 		Fetches most recent post on r/mechanicalkeyboards _(limit 3)_.\n\
haiku #: 		Fetches most recent post on r/youtubehaiku _(limit 3)_.\n\
me #: 		Fetches most recent post on r/me\_irl _(limit 3)_.\n\
code #: 		Fetches most recent post on r/programmerhumor _(limit 3)_.\n\
video #: 		Fetches most recent post on r/videos _(limit 3)_.")
	elif message.content.startswith(">stop"):	# stop command for audio
		for voice in client.voice_clients:	# loops through all connections
			if voice.server == message.channel.server:	# if server matches the currently connected server
				await voice.disconnect()	# disconnect the voice client
	elif message.content.startswith(">play"):	# play youtube link
		channel = client.get_channel(message.author.voice.voice_channel.id)	# get the author's voice channel
		voice = await client.join_voice_channel(channel)
		link = message.content[6:]	# fetch link from author's message
		player = await voice.create_ytdl_player(link)	# play the youtube link
		player.start()
		while not player.is_done():
			await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">oof"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		msg = await client.send_message(message.channel, ":weary: ***oof***")	# oof message
		repetitions = message.content[5:]	# repetitions specifies how many times to loop
		if repetitions == "":	# if none specified, do command 1 time
			repetitions = 1
		if int(repetitions) > 10:	# limit of 10 max
			repetitions = 10
		for i in range(0, int(repetitions)):	# loop through all repetitions
			player = voice.create_ffmpeg_player("assets/quietoof.mp3")	# play audio
			player.start()
			while not player.is_done():	# wait for player to finish before starting again
				await asyncio.sleep(.01)
		await voice.disconnect()	# disconnect when done
	elif message.content.startswith(">ping"):
		msg = await client.send_message(message.channel, ":ping_pong: Pong! :ping_pong:")
	elif message.content.startswith(">OOF"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		msg = await client.send_file(message.channel, "assets/oof.png")
		repetitions = message.content[5:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/loudoof.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">git"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		msg = await client.send_file(message.channel, "assets/git.png")
		repetitions = message.content[5:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 10:
			repetitions = 10
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/git.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">thot"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		repetitions = message.content[6:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/quietthot.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">THOT"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		repetitions = message.content[6:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 1:
			repetitions = 1
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/loudthot.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">quack"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		repetitions = message.content[7:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 10:
			repetitions = 10
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/quack.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">woop"):
		channel = client.get_channel(message.author.voice.voice_channel.id)
		voice = await client.join_voice_channel(channel)
		repetitions = message.content[6:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 10:
			repetitions = 10
		for i in range(0, int(repetitions)):
			player = voice.create_ffmpeg_player("assets/woop.mp3")
			player.start()
			while not player.is_done():
				await asyncio.sleep(.01)
		await voice.disconnect()
	elif message.content.startswith(">weeb"):
		global weebcounter	# uses global counter to keep track of how many posts were already gone through
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=awwnime")	# fetch data
		repetitions = message.content[6:]	# see how many repetitions user wants
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):	# display post
			msg = await client.send_message(message.channel, " " + d['entries'][weebcounter]['title'] + ":\n" + d['entries'][weebcounter]['link'])
			weebcounter += 1	# increment counter to next post
	elif message.content.startswith(">haiku"):
		global haikucounter
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=youtubehaiku")
		repetitions = message.content[7:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			msg = await client.send_message(message.channel, " " + d['entries'][haikucounter]['title'] + ":\n" + d['entries'][haikucounter]['link'])
			haikucounter += 1
	elif message.content.startswith(">keeb"):
		global keebcounter
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=mechanicalkeyboards")
		repetitions = message.content[6:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			msg = await client.send_message(message.channel, " " + d['entries'][keebcounter]['title'] + ":\n" + d['entries'][keebcounter]['link'])
			keebcounter += 1
	elif message.content.startswith(">me"):
		global mecounter
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=me_irl")
		repetitions = message.content[4:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			msg = await client.send_message(message.channel, " " + d['entries'][mecounter]['title'] + ":\n" + d['entries'][mecounter]['link'])
			mecounter += 1
	elif message.content.startswith(">video"):
		global videocounter
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=videos")
		repetitions = message.content[7:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			msg = await client.send_message(message.channel, " " + d['entries'][videocounter]['title'] + ":\n" + d['entries'][videocounter]['link'])
			videocounter += 1
	elif message.content.startswith(">code"):
		global codecounter
		d = feedparser.parse("http://inline-reddit.com/feed/?subreddit=programmerhumor")
		repetitions = message.content[6:]
		if repetitions == "":
			repetitions = 1
		if int(repetitions) > 3:
			repetitions = 3
		for i in range(0, int(repetitions)):
			msg = await client.send_message(message.channel, " " + d['entries'][codecounter]['title'] + ":\n" + d['entries'][codecounter]['link'])
			codecounter += 1

# After you have modified the code, feel free to delete the line above (line 33) so it does not keep popping up everytime you initiate the ping commmand.
	
client.run(client_token)

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 9.