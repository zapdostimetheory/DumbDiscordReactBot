import os
import discord
import requests
import random

client = discord.Client()
#this calls to the Discord server and activates the bot

sony_words = ["Playstation", "Sony", "PlayStation 5", "ps5"]
#These are the trigger words that you can configure. This is operating under the assumption the server is owned by someone who loves Xbox

sony_bad = [
    "Xbox > Playstation",
    "599 US DOLLARS",
    "Riiiiiiiiiidge racer",
    "So there's this giant enemy crab... you attack its weak point for massive damage",
]
#This is what the bot will say in return, it randomly chooses out of this array, defined later.

xbox_words = ["Xbox",]

xbox_good = [
    "Xbox Fun Fact: Xbox invented gaming on November 15th, 2001 with the release of Halo: Combat Evolved.",
    "Xbox Fun Fact: Halo invented jumping in video games.",
    "Xbox Fun Fact: Shrek was a launch title for the original Xbox, making Shrek among the first video games ever released.",
]
#more fun facts

@client.event
async def on_ready():
    print('Server side -- We are in as {0.user}'.format(client))
#This is to check on the server side, as indicated, the handshake is complete and the bot is now active in the Discord server.

@client.event
#This is how the bot can start communicating with Discord's client, so other users can see.
async def on_message(message):
    if message.author == client.user:
        return
    #no spam filter from the bot itself

    msg = message.content
    #to make the next code block readable, lol

    if any(word in msg for word in sony_words):
        await message.channel.send(random.choice(sony_bad))
    #This is the function that makes a random choice from the array above.

    if any(word in msg for word in xbox_words):
        await message.channel.send(random.choice(xbox_good))
    #As above, so below

    if msg == 'Xbox is good':
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
    #This was to test if the bot could send emojis as a message to server and also react to the original poster's message

    if msg == 'Sony is good':
        emoji = '\N{THUMBS DOWN SIGN}'
        await message.add_reaction(emoji)

    if msg.startswith('Sup '):
        await message.channel.send('Sup back')
    #Startswith method test

    if message.author.id == 0000000000000000: #userid found in the developer menu of Discord client
        await message.channel.send('How are you, USER?')
    #If someone specifically in the channel messages the server, the bot can react.

    if msg == ':howitfeelstochew5gum:':
        emoji = '<:salute:954204579577339964'
        await message.add_reaction(emoji)
    #A Test to see if custom emojis added to the server could be allowed. The custom emoji ids are shown in the developer console on Discord.

client.run('')
#insert your bot code API key above in the quotes.
