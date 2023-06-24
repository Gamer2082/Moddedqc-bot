import discord
from discord import app_commands
from discord.ext import commands
import datetime
import time
import calendar

Intents = discord.Intents().all()

bot = commands.Bot(command_prefix="!", intents=Intents)

Intents.message_content = True
Intents.guilds = True
Intents.members= True

moddedID = 1063543942131486780

client = discord.Client(intents=Intents)

tree = app_commands.CommandTree(client)



@bot.event
async def on_ready():
    print(f"{bot.user.name} : Go for hype serveur")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=moddedID))
        print(f"Synced {len(synced)} commands")

    except Exception as e :
        print(e)

def isOwner():
    def predicate(interaction : discord.Interaction):
        for role in interaction.user.roles:
            if role.id == 1116698028888293386:
                return True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        return False

    return app_commands.check(predicate)


@bot.tree.command(guild=discord.Object(id=moddedID), name="test",description="test if bot is enable")
@isOwner()

async def test_slash(interaction : discord.Interaction):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log = current_time + f" : {bot.user.name} PythonLog : {interaction.user.name} use command /test"
    log_channel = interaction.guild.get_channel(1063558928316760205)
    await interaction.response.send_message(f"{bot.user.name} : Go for hype serveur")
    await log_channel.send(log)


@bot.tree.command(guild=discord.Object(id=moddedID), name="help",description="Get command help" )
async def help_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"Command list \n /help : Get command help \n/embed: Create new embed message [ADMIN] \n/annonce: make a brodcast[ADMIN]", ephemeral = False)
    def newHelp(title,text):
        title = str
        text = str
        embed.add_field(name= "Command",value=text)

    embed = discord.Embed(title="Help",description="Liste des commandes")
    newHelp("/help "," Get command help")
    newHelp("/embed", "Create new embed message [ADMIN]")
    newHelp("/annonce", "make a brodcast[ADMIN]")
    embed.timestamp = datetime.datetime.now()

    # await interaction.response.send_message(embed= embed)
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log = current_time + f" : {bot.user.name} PythonLog : {interaction.user.name} use command /help"
    log_channel = interaction.guild.get_channel(1063558928316760205)

    await log_channel.send(log)
@bot.tree.command(guild=discord.Object(id=moddedID),name="embed",description="Create new embed message")
@isOwner()

async def embed_slash(interaction : discord.Integration ,title : str = None ,message: str = None,description :str = None):

    if title == None:
        title = "title"


    if description == None:
        description = "DESCRIPTION"


    if message == None:
        message= "MESSAGE"


    log_channel = interaction.guild.get_channel(1063558928316760205)
    embed = discord.Embed(title=title,description=description, color = 0xffff)
    embed.add_field(name="MESSAGE",value=message)
    embed.timestamp = datetime.datetime.now()
    channel = interaction.guild.get_channel(1090640745569980477)
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log= str(current_time)  + f" : {bot.user.name} PythonLog : {interaction.user.name} use command /embed"

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await channel.send(embed = embed)
    await log_channel.send(log)

@bot.tree.command(guild=discord.Object(id=moddedID), name="annonce",description="make broadcast" )
@isOwner()

async def annonce_slash(interaction : discord.Interaction, message : str):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log = current_time + f" : {bot.user.name} PythonLog : {interaction.user.name} use command /annonce"
    log_channel = interaction.guild.get_channel(1063558928316760205)

    if message == None:
        interaction.response.send_message("Info manquante")

    embed = discord.Embed(title="ANNONCE", description="" , color=0xffff)
    embed.add_field(name="MESSAGE", value=message)
    embed.timestamp = datetime.datetime.now()
    channel = interaction.guild.get_channel(1090640745569980477)

    await interaction.response.send_message(embed=embed, ephemeral=True)
    await channel.send(embed=embed)

    await log_channel.send(log)

@bot.tree.command(guild=discord.Object(id=moddedID), name="login", description="login" )

async def login_slash(interaction:discord.Interaction, verify:bool):
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    log = current_time + f" : {bot.user.name} PythonLog : {interaction.user.name} use command /login"
    log_channel = interaction.guild.get_channel(1063558928316760205)
    await log_channel.send(log)

    if verify == True:
        await interaction.response.send_message("Wait...")
    else:
        await interaction.response.send_message("True no False")


    


































































token = "Token"

bot.run(token)
