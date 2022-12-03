 import discord
from discord.ext import commands        #bibliothèque discord.py

bot = commands.Bot(command_prefix ="/", description = "bot officielle de ModdedQC le best serveur Minecraft")
#event
@bot.event
async def on_menber_join(menber):
 channel = menber.guild.get_channel(1046361661709242380)
await Channel.send("Accueillons ensemble le nouveau joueur {menber mention}sur moddedQC")

@bot.event
	async def on_ready():
		print("Ready !")
		
		#variable help
		helpCommand ="/salut:pour saluer le bot /n /ip:pour avoir l'ip du serveur Minecraft /n /version pour avoir la version de Minecraft /n /infodiscord: pour avoir les infos sur le serveur discord /n /site: pour avoir l'address du site web de ModdedQC/n /vote pour avoir le site de vote du serveur Minecraft et soutenir le serveur en remportent des récompence /n /invite pour avoir un lien d'invitation vers le serveur Discord à partager /n /infojeu pour avoir les information sur le serveur Minecraft /n /staffbot: pour avoir le nom des personnes à mentionner en cas de probléme avec le bot /n /régle pour avoir les régle du serveur Discord s'aplicant aussi au chat ingame /n /help: pour avoir cette liste /cordialement @Gamer_m et le staff :)"
#command bot
@bot.command()
   @commands.has_permissions(ban_menbers=true)
 async def ban(ctx,user:discord.u
User):
 await ctx.guild.ban(user)
 await ctx.send(f"{user} à été définitivement banni de ce serveur")
@bot.command()
	async def salut(ctx):                  #si tu te sent seule mdr 
		print("coucou")								
		await ctx.send("coucou !")
@bot.command()
	async def ip(ctx):                          #command pour avoir l'ip du serveur
		print("secret")
		await ctx.send("**Cette command est indisponible**")
@bot.command()
	async def version(ctx):						#commande pour avoir la version du serveur
		print("*1.17.1* **Minecraft java edition**")
		await ctx.send("1.17.1 Minecraft java edition")
@bot.command()
	async def infodiscord(ctx):                                   #command pour avoir les infos serveur discord
		print("info serveur")
		serveur = ctx.guild 
		numberOfTextChannels = lent(serveur.text_channels)
		numberChannelVocaux = lent(serveur.voice_channels)
		serveurDescription = serveur.description
		numberUtilisateur = serveur.menber_count
		serveurName = serveur.name
		message = f"le serveur **{serveurName}** contient *{numberUtilisateur}*. /n la description du serveur est {serveurDescription} et possede *{numberChannelVocaux}* channels vocaux et *{numberOfTextChannels}*channels textuel donc."
		await ctx.send(message)
@bot.command()                       #command pour le lien vers le site
	async def site(ctx):
		print(siteWeb)            #site du serveur
		siteWeb = " http://moddedqc.rf.gd/"
		message_site =f"pour vous rendre sur le site web prenner cette addresse {siteWeb} "
  await ctx.send(message_site)
@bot.command()
	async def vote(ctx):        #voter pour le serveur 
		print("vote")
		siteVote = "http://moddedqc.rf.gd/voter"
		await ctx.send("**voter sur http://moddedqc.rf.gd/voter**") 
@bot.command()
	async def invite(ctx):              #ien invitation
		print("invitation")
		await ctx.send("**https://discord.gg/55zRejMr4V**")
@bot.commands()
	async def infojeu(ctx):             #info sur le serveur minecraft
		print("info jeu")
		await ctx.send("Le serveur est acctuellement en *developpement*à la version  version 1.17.1 de Minecraft java /n **Statue:offline**")
@bot.command()
	async def !staffbot(ctx):              #obtenir la liste des develloppeur bot a mentionner
		print("bug")
		Stafflist = "Gamer_m2082"
		staffbot= f"mentionner {Stafflist}" 
		await ctx.send(staffbot)

                #rsauModdedq = f"discord: https://discord.gg/55zRejMr4V" 
@bot.command()                    #command pour les régle
	async def regle(ctx):
		print ("les régle du serveur")
		await ctx.send(regleServeur)

@bot.command()
	async def help(ctx):
		await ctx.send(helpCommand)               #command help
		
regleServeur = "Bonjour tout le monde, ||@here  Version articles des règles :/nRèglement du serveur Discord /n 1 Comportement/n-Restez courtois, poli. Vous pouvez être familier./n-Pas de violence verbale gratuite. Vous pouvez taquiner gentiment sans aller dans l’extrême. Si cela reste dans la bonne humeur et le second degré nous le tolérons. Si le staff ou moi même estimons que cela ne respecte plus la règle, vous risquez un kick ou un ban en fonction du geste et de la tolérance du membre du staff qui vous puni, pas le droit de faire la pub en Message privé , le harcèlement n'est pas autorisé. /nII – Chat écrit/vocal/n-Pas de spam, sous peine de bannissement./n-Pas de Bruit de propos sexuelle en vocal ni de soufflement dans le micro  ,  sous peine d’avertissement puis kick si l’avertissement n’est pas pris en compte./n-Pas de pub sur les différents chats , sous peine avertissement puis ban si l’avertissement n’est pas pris en compte./nIII Profil/Pseudo/n- Ne doit pas être ressemblant/confondu avec celui d’un membre du staff, sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte. /n-les doubles-comptes sont strictement interdis/n- Ne doit pas contenir de propos racistes, homophobes, sexistes sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte./n-Ne doit pas avoir de caractère pornographique, sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte./n- Contacter le staff/n- Si pour une quelconque raison, vous voulez contacter un membre du staff, créez un ticket de support serveur discord dans le salon tickets/n-Si vous voulez entrer dans l’équipe de modération allez dans le salon recrutement/nMerci de ne pas mentioner les administrateur  sous aucuns prétextes sous peine de sanctions . Cordialement le staff "

#bot.run("token")


bot.run("MTA0MTM3MDYyMzM3NDUzMjcwOQ.Gsuc3m.9VMPijpQImHNhyRhwrB6XOkVLp7JA-LpC2u8ME")

