import os
import discord
import json
import asyncio
import sys
import random
from discord.ext import commands
from discord.ext.commands import Bot


with open("configMe.json") as json_cfg:
    cfg = json.load(json_cfg)
# Load configuration file items
secret_token = cfg['secret_token']

# Loading of nonsense-files
allFiles = [x["filename"] for x in cfg['allFiles']]
httpString = cfg['site_address']
allowedNonsenseChannels = [x["channel"] for x in cfg['allowed_nonsense_channels']]
# Load Fate-Config
fate = [x["emote"] for x in cfg['fate_dice']]


def roller(n):
    return random.randint(0,n)
def rollHandler(x):
	rolls = [0] * x
	for x, item in enumerate(rolls):
	    rolls[x] = roller(2)
	rolls.sort()
	return rolls


client = commands.Bot(command_prefix='!')

@client.command()
async def roll(ctx, arg="FfffX"):
    x = "F"
    # we need to set these args to garbage to make sure an assignment was made.
    try: 
        x = int(arg) #if this fails, they haven't given us a proper int. I should write a catch statement to reduce the impact on logs, right now every time it's 8 lines or more per failure.
    except:
        await ctx.channel.send("That's not a valid. Try `roll x` for x dice.")
    sendString = "" #init the string
    fateNum = rollHandler(x);
 #these values hardcoded for now, maybe offload to config later?
    for index, elt in enumerate(fateNum):
        sendString += fate[fateNum[index]]   #Append the roll to the message
        #Remember here, we roll 0-2 instead of 1-3 because of this! 
    await ctx.channel.send(sendString) # send the finished string
    
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user) #once every few hours per user
async def nonsense(ctx):
    choice = random.choice(allFiles)
    if str(ctx.channel.id) in allowedNonsenseChannels: #does it match any of our channels?
    	await ctx.channel.send(f'{httpString}{choice}')
    return


@client.event
async def on_ready():
    print(f"Initializing...")
    print('Logged on as', client.user) #Identify current nickname to console
    print(f"Bot is ready.")
    print(f"There are {len(allFiles)} nonsense files ready to be dispensed.") 
    print(f"FATE roller is active.")

client.run(secret_token)
