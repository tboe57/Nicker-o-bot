import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "n!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='type n!help'))
    
@client.command(pass_context=True)
async def TurnOff(ctx):
    if ctx.message.author.id == "217328624829726720":  # thats ur id
        await client.say("Going offline")
        await client.logout()
    else:
        await client.say("sorry, my maker is a crackhead and won't let you execute this command.... \n#rekt")
        
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context = True)
async def inrole(ctx, *name):
    name = ' '.join(name)
    message = ctx.message
    users = [x.name for x in message.server.members if name in [z.name for z in x.roles]]

    if len(users) > 50: seperator = ', '
    else: seperator = '\n'
    
    embed = discord.Embed(title = "User with the %s role (%s)"%(name, str(len(users))), description = seperator.join(users), color = 0xFFFFF)
    await client.delete_message(message)
    return await client.say(embed = embed)

'''#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)'''

#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
     
client.run("Token")


