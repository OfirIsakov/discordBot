import discord
from discord.ext import commands
import time
from time import gmtime, strftime
import random
import youtube_dl
import asyncio
from itertools import cycle
import numpy
import myToken

### PLAYERS IDS ###
ofido = '283625847460462593'
yigdan = '266593092205805568'
rrass = '272719228170403840'
rrass2 = '426713009356931072'
daiva = '285056543479562240'
hatif = '330721023563399169'
koko = '325264338149703680'

### LOBBY IDS ###
afk = '476770345945268225'
console = '500414709351317509'

### LIST FOR MUSIC PLAYER ###
players = {}  # Don't touch please

### ANIMATED MOTD ###
status = ['KQLYHACKS.WORDPRESS.COM','NEVER VAC AND YOU KNOW!']

### MISC ###
prefix = '#'
line = '-----------------'

### PREFIX ###
bot = commands.Bot(command_prefix=prefix)

### REMOVED COMMANDS ###
bot.remove_command('help')  # Don't touch please



### STATUSES ###
async def change_status():
    await bot.wait_until_ready()
    msgs = cycle(status)
    
    while not bot.is_closed:
        current_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(6.5)
        

### PRINTS TO CONSOLE WHEN GOING ONLINE ###
@bot.event
async def on_ready():
    await bot.send_message(discord.Object(id=console),'Time:' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
    await bot.send_message(discord.Object(id=console),"I am: " + bot.user.name)
    await bot.send_message(discord.Object(id=console),"My ID is: " + bot.user.id)
    await bot.send_message(discord.Object(id=console),str(line))


### CLOSE BOT ###
@bot.command(pass_context=True)
async def close(ctx):
    if ctx.message.author.id == ofido:
        await bot.send_message(discord.Object(id=console),'logging out')
        await bot.logout()
        

### HELP FUNCTION ###
@bot.command(pass_context=True)
async def help(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        embed = discord.Embed(title="Dont worry {}".format(author.name), description="I will help ya!", color=0x00F0A9)
        embed.add_field(name="Prefix:", value="#")
        embed.add_field(name="HELP:", value="I will show this window.")
        embed.add_field(name="ping:", value="I will pong you back.")
        embed.add_field(name="info @[user name]:", value="I will show info about the mentioned user.")
        embed.add_field(name="serverinfo:", value="I will show the info about the server.")
        embed.add_field(name="join:", value="I will join the lobby your in.")
        embed.add_field(name="leave:", value="I will leave the lobby im currently in.")
        embed.add_field(name="stop:", value="I will stop the song im currently playing.")
        embed.add_field(name="leave:", value="I will leave the lobby im currently in.")
        embed.add_field(name="leave:", value="I will leave the lobby im currently in.")
        embed.add_field(name="leave:", value="I will leave the lobby im currently in.")
        embed.add_field(name="spam:", value="I will join and leave the lobby your in(I will chase you....)")
        embed.add_field(name="playing WIP(Work In Progress):", value="Shows the 3 most played games in all the servers im in.")
        embed.add_field(name="roll:", value="Chooses a random person frtom all the servers im in.")
        embed.add_field(name="kick(Disabled because security purposes.):", value="Kicks the mentioned user.")
        await bot.say(embed=embed)
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),"Help:")
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### PING FUNCTION ###
@bot.command(pass_context=True)
async def ping(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        await bot.say("Pong! :ping_pong:")
        ### PRINT TO CONSOLE ### 
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### USER INFO ### 
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        embed = discord.Embed(title="{}'s Info.".format(user.name), description="So... I Found This:", color=0x00ff00)
        embed.add_field(name="Name:", value=user.name, inline=True)
        embed.add_field(name="ID:", value=user.id, inline=True)
        embed.add_field(name="Status:", value=user.status, inline=True)
        embed.add_field(name="Highest Role:", value=user.top_role)
        embed.add_field(name="Joined At:", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.say(embed=embed)
        ### PRINT TO CONSOLE ### 
        await bot.send_message(discord.Object(id=console),user.name + '\'s - Info.')
        await bot.send_message(discord.Object(id=console),'-ID.' + user.id)
        await bot.send_message(discord.Object(id=console),'-Status.' + user.status)
        await bot.send_message(discord.Object(id=console),'-Highest Role.' + user.top_role)
        await bot.send_message(discord.Object(id=console),'-Joined At.' + user.joined_at)
        await bot.send_message(discord.Object(id=console),'-Image URL.' + user.avatar_url)
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### SERVER INFO ###
@bot.command(pass_context=True)
async def serverinfo(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        embed = discord.Embed(title="{}'s Info.".format(ctx.message.server.name), description="So... I Found This:", color=0xff0000)
        embed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Roles:", value=str(len(ctx.message.server.roles)) + '(With Bot Roles.)', inline=True)
        embed.add_field(name="Members:", value=str(len(ctx.message.server.members)))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        await bot.say(embed=embed)
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),ctx.message.server.name + '\'s - ServerInfo.')
        await bot.send_message(discord.Object(id=console),'-ID.' + ctx.message.server.id)
        await bot.send_message(discord.Object(id=console),'-Roles.' + len(ctx.message.server.roles))
        await bot.send_message(discord.Object(id=console),'-Members.' + len(ctx.message.server.members))
        await bot.send_message(discord.Object(id=console),'-Image URL.' + ctx.message.server.icon_url)
        await bot.send_message(discord.Object(id=console),'Resumed playing')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### JOIN CHANNEL ###
@bot.command(pass_context=True)
async def join(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        channel = author.voice.voice_channel
        await bot.join_voice_channel(channel)
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Joined: ' + str(channel))
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### PLAY MUSIC ###
@bot.command(pass_context=True)
async def play(ctx, url):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        try:
            channel = author.voice.voice_channel
            await bot.join_voice_channel(channel)
        except:
            print('All ready was connected!')
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Joined: ' + 'Played: ' + str(url) + 'at: ' + str(channel))
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        await bot.say('Playing: ' + str(url) + ' because ' + str(author.mention) + ' asked.')
        server = ctx.message.server
        voice_client = bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()
    
    
### PAUSE MUSIC ###
@bot.command(pass_context=True)
async def pause(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        await bot.say('Paused, it\'s  not my fault! It\'s %s fault!' % str(author.mention))
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Paused playing')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        id = ctx.message.server.id
        players[id].pause()
    
    
    
### RESUME MUSIC ###
@bot.command(pass_context=True)
async def resume(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        await bot.say('Resumed playing, it\'s not my fault! It\'s %s fault!' % str(author.mention))
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Resumed playing')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        id = ctx.message.server.id
        players[id].resume()
    
    
### STOP MUSIC ###
@bot.command(pass_context=True)
async def stop(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        await bot.say('Stoped playing, it\'s not my fault! It\'s %s fault!' % str(author.mention))
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Stoped playing')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        id = ctx.message.server.id
        players[id].stop()
        server = ctx.message.server
        voice_client = bot.voice_client_in(server)
        await voice_client.disconnect()
    
    
### QUEUE A SONG ###
###### work in progress ######


### LEAVE CHANNEL ###
@bot.command(pass_context=True)
async def leave(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        server = ctx.message.server
        voice_client = bot.voice_client_in(server)
        await voice_client.disconnect()
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Left Channel')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### PLAY MUSIC ###
@bot.command(pass_context=True)
async def ah(ctx):
    if not ctx.message.author.id == daiva:
    
        url = 'https://www.youtube.com/watch?v=ZntwTAreDSc'
        author = ctx.message.author
        try:
            channel = author.voice.voice_channel
            await bot.join_voice_channel(channel)
        except:
            await bot.send_message(discord.Object(id=console),'All ready was connected!')
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Ah meshihma va mala')
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        await bot.say('Everything for ah yakar ' + str(author.mention) + ' :eggplant:')
        server = ctx.message.server
        voice_client = bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()


### SPAM JOIN CHANNEL ###
@bot.command(pass_context=True)
async def spam(ctx):
    if not ctx.message.author.id == daiva:
        global l
        l = True
        author = ctx.message.author
        channel = author.voice_channel
        chanelserver = author.voice_channel.server
        voice_channel = bot.voice_client_in(chanelserver)
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),'Spamed: ' + str(chanelserver))
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))
        while l:
            try:
                await bot.join_voice_channel(channel)
            except:
                await voice_channel.disconnect()


### STOP THE LOOP ###
@bot.command(pass_context=True)
async def stop_move(ctx):
    global breaking
    breaking = True


### VOICE CHANNEL ###
@bot.command(pass_context=True)
async def move(ctx, victim, numbers):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        if author.id == ofido or author.id == yigdan:
            global breaking
            breaking = False
            for i in range(abs(int(numbers))):
                victim_member = ctx.message.mentions[0]
                channel = bot.get_channel(afk)
                await bot.move_member(victim_member, channel)
                await asyncio.sleep(0.75)

                if breaking:
                    break
        else:
            await bot.say('NO!')


### CHECKS FOR THE TOP 3 GAME USERS ARE PLYING ###
@bot.command(pass_context=True)
async def playing(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        lista = []
        none = []
        for member in bot.get_all_members():
            if ctx.message.author.bot:
                pass
            if str(member.game) == 'None':
                none.append('None')
            else:
                lista.append(str(member) + ' ' + str(member.game))

        lista = set(lista)
        final = "\n".join(lista)
        if len(final) < 2000:
            await bot.say(final)
        elif 4000 > len(final) > 2000:
            listb = numpy.array_split(lista, 2)
            final2 = "\n".join(listb)
            await bot.say(final2)
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),str(len(none)) + 'users are not doing anything.')
        await bot.send_message(discord.Object(id=console),final)
        await bot.send_message(discord.Object(id=console),"Playing:")
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### CHOOSES A RANDOM PERSON ###
@bot.command(pass_context=True)
async def roll(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        serverid = ctx.message.server.id
        members = []
        for member in bot.get_all_members():
            if member == bot:
                return
            else:
                members.append(member)
        memberCount = len(members)
        randomNumber = random.randint(0, (memberCount - 1))
        await bot.say(members[randomNumber].name + " I choose you!")
        ### PRINT TO CONSOLE ###
        await bot.send_message(discord.Object(id=console),"roll: ")
        await bot.send_message(discord.Object(id=console),"rolled: " + str(members[randomNumber].name))
        await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
        await bot.send_message(discord.Object(id=console),'By: ' + str(author))
        await bot.send_message(discord.Object(id=console),str(line))


### LOVE ME ###
@bot.command(pass_context=True)
async def loveme(ctx):
    if not ctx.message.author.id == daiva:
        if ctx.message.author.id == ofido:
            await bot.say(":heart_eyes:")
        else:
            await bot.say("{}, m8... I ONLY LOVE OFIDO!:rage:".format(ctx.message.author.mention))


### KICKS A USER FROM VOICE CHANNEL ###
@bot.command(pass_context=True)
async def kick(ctx):
    if not ctx.message.author.id == daiva:
        author = ctx.message.author
        if ctx.message.author.id == ofido or ctx.message.author.id == yigdan:
            victim = ctx.message.mentions[0]
            kick_channel = await bot.create_channel(ctx.message.server, "kick", type=discord.ChannelType.voice)
            await bot.move_member(victim, kick_channel)
            await bot.delete_channel(kick_channel)
        elif ctx.message.mentions[0] == ofido:
            await bot.say('FORK YOU! YOU DARE TO TRY AND KICK THE MASTER?!?! EAT A BOOT IN YOUR FACE :boot:')
            victim = ctx.message.author
            kick_channel = await bot.create_channel(ctx.message.server, "kick", type=discord.ChannelType.voice)
            await bot.move_member(victim, kick_channel)
            await bot.delete_channel(kick_channel) 
            ### PRINT TO CONSOLE ###
            await bot.send_message(discord.Object(id=console),'Some 1 tried to kick you:')
            await bot.send_message(discord.Object(id=console),'At: ' + str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
            await bot.send_message(discord.Object(id=console),'By: ' + str(author))
            await bot.send_message(discord.Object(id=console),str(line))

### KICK FROM SERVER ###
# @bot.command(pass_context=True)
# async def kick(ctx, user: discord.Member):
#
#     if user.id == "283625847460462593":
#         await bot.say("HELL NO!")
#     if ctx.message.author.id == "283625847460462593":
#         await bot.say(":boot: Cya {}. Ya loser!".format(user.name))
#         await bot.kick(user)
#         print('Kicked: ', user)
#         print('At: ', str(strftime("%d-%m-%Y %H:%M:%S", gmtime())))
#         print('By: ', ctx.message.author)
#         print(line)


### EMBED OPTIONS ###
# @bot.command(pass_context=True)
# async def embed(ctx):
#     embed = discord.Embed(title="test", description="THE KQLY IS TESTING")
#     embed.set_footer(text="footer")
#     embed.set_author(name="cool name!")
#     embed.add_field(name="field", value="but is it?", inline=True)
#     await bot.say(embed=embed)



### OLD FORMAT ###
# @bot.event
#
# async def on_message(message):
#     msg = message.content.upper()
#     userid = message.author.id
#     ofido = "283625847460462593"
#     yigdan = "266593092205805568"
#     mention = message.author.mention
#     if msg.startswith('KQLY'):
#         if userid == ofido or userid == yigdan:
#             await bot.send_message(message.channel, "Yes master?")
#             counter = 0
#             counter += 1
#             if counter == 1:
#                 return
#             else:
#                 await bot.send_message(message.channel, "%s DONT SAY THE NAME OF KQLY!!" % mention)
#                 await bot.delete_message(message)
#
#     if msg.startswith("HOW ARE YOU?"):
#         if userid == ofido or userid == yigdan:
#             await bot.send_message(message.channel, "Im fine! %s" % mention)
#             await bot.send_message(message.channel, "You?")
#
#     if msg.startswith("FINE THX"):
#         if userid == ofido or userid == yigdan:
#             await bot.send_message(message.channel, ":smile:")


bot.loop.create_task(change_status())
bot.run(myToken.token())

