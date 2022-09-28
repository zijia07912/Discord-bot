import discord
from discord.ext import commands
from apikey import *  # import token

intents = discord.Intents.default()
intents.members = True
prefix = ('.', '+', '|')
emote = ["<:Pepega:641810460756410396>", "<:Pepega:864401154754478090>", "<:Sadga:864813104688398376>", "<:PepegaSmart:866314452205568031>"]
helloString = ["hello", "hi", "hey", "h3llo", "hell0", "helo"]

client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
client.remove_command("help")

# startup
@client.event
async def on_ready():
    await client.change_presence()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# join channel
@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Pepega coming in " + emote[0])
    else:
        await ctx.send("You're not in the voice channel u " + emote[0])


# leave channel
@client.command(pass_context=True)
async def bye(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await ctx.send("Adios " + emote[2])
    else:
        await ctx.send("I'm not in the voice channel " + emote[2])


# trigger respond if certain string typed
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    for x in emote:
        if x in message.content:
            await message.channel.send('Did someone called me? <a:PepegaAim:849148853391458304>'.format(message))

    for s in helloString:
        if message.content.lower().startswith(s):
            await message.channel.send(
                'Hello {0.author.mention}, I\'m Pepega <a:PepegaAim:849148853391458304> '.format(message))

    if message.content.lower().startswith('biskut'):
        await message.channel.send(file=discord.File('biskut.png'))
        
    await client.process_commands(message)


@client.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title='Help', description='detail info of all commands ' + emote[3])
    embed.add_field(name="Voice_related", value="join, bye")
    embed.add_field(name="Message_related", value=(str(helloString)+", <:Pepega:641810460756410396>"))

    await ctx.send(embed=embed)


@help.command()
async def join(ctx):
    embed = discord.Embed(title="join", description="<:Pepega:641810460756410396> will join the channel")
    embed.add_field(name="***Syntax***", value=".join / +join / |join")
    await ctx.send(embed=embed)
# run the codes
client.run(TOKEN)
