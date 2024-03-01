## Notes to do next:- rewrite cleaner code!
# Shards [if too many servers]
# replit db has limit 50MB
# ArHelp cmd in Arabic
# changable prefix for servers
# more game with AI
# Search-able yt and music (not only link)
# premium other servers
# sub cmds!
# slash cmds! *IMPORTANT*
## PS: using nextcord instead of discordpy # turns out not really a good idea
# instead of `avatar_url`, uses `display_avatar` (which returns *Asset* type)

import os
import discord
from discord import Embed, Colour, app_commands
from discord.ext import commands, tasks
#import json
#from replit import db ## Use MongoDB

#import aiohttp
#import random
#from keep import keep_alive
from datetime import datetime
from itertools import cycle
import asyncio
from inspect import getsource
import re
import typing

from cogs.cog1 import Greetings
from cogs.cog2 import Moderating
from cogs.cog3 import Games
from cogs.cog4 import spy
from cogs.cog5 import SoulWorker
from cogs.cog8 import Fun
from cogs.cog9 import Music
# need to find a better way


h_cmd = commands.MinimalHelpCommand(no_category="Others")
p = ('sw!','بیب ','بيب ')
intents = discord.Intents.all()
gid= discord.Object(id= 727092352363135077)

class Mybot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.all()
    super().__init__(command_prefix= p, intents= intents,help_command = h_cmd)
  async def setup_hook(self):
    await self.tree.sync()
    print(f"Synced slash cmds for {self.user}.")

Kat = Mybot()
#tree= app_commands.CommandTree
#Kat = Mybot(command_prefix=p,intents=intents, help_command= h_cmd)

@Kat.event
async def on_ready():
#	await self.wait_until_ready()
		#if not self.synced:
		#	await self.tree.sync(guild= discord.Object(id= 727092352363135077))
		#	self.synced = True
		change_status.start()
		print("Catherine is on!")


@Kat.hybrid_command(with_app_command= True)
@app_commands.guilds(gid)
async def slash(ctx: commands.Context):
  #await ctx.defer(ephermal= True)
  await Kat.tree.sync(guild= gid)
  print(f"Attempted to sync slash cmds for {Kat.user} in {ctx.guild}")
  await ctx.reply("Yoho!")

#class Bot(commands.AutoShardedBot):
  	#async def startup(self):
    		#await self.wait_until_ready()
    		#await tree.sync()

#kat = Bot(intents = intents)
#tree = app_commands.CommandTree(kat)

#shard_id = (guild_id >> 22) % num_shards
# # guild_id? num_shards?

#menu = DefaultMenu('◀️', '▶️', '❌')
#Kat.help_command = PrettyHelp(navigation=menu, colour=discord.Colour.blue())
# # nah forget pretty help, use paginator + Default/MinimalHelpCommand

mood = ""
db["mood"]= mood

status = cycle(["Working the soul","Soulworker","how to defeat souldregs","to become the best Soulworker!"])
extentions = ['cog1', 'cog2', 'cog3', 'cog4', 'cog5', 'cog8', 'cog9']


def mee(ctx):
	return ctx.message.author.id == 444806806682730496


@tasks.loop(minutes=20)
async def change_status():
	await Kat.change_presence(activity= discord.Game(next(status)))

# Events

@Kat.event
async def on_command_error(ctx, error):
	print(error)
	#await ctx.send("something's wrong!")
	await ctx.send(embed=Embed(title='Error', description= error, colour=16711680, timestamp= datetime.utcnow()))

@Kat.hybrid_command()
@app_commands.guilds(gid)
async def shards(ctx):
  await ctx.send(Kat.shards)
  await ctx.send(Kat.shards[0].id)
  await ctx.send(Kat.shard_count)

## None
#  await ctx.send(Kat.shard_id)
#  await ctx.send(Kat.shard_ids)

@Kat.hybrid_command(aliases=["بنج"])
@app_commands.guilds(gid)
async def ping(ctx):
	await ctx.send(f"pong!~ {int(Kat.latency*1000)}ms")

@Kat.command(hidden=True)
@commands.check(mee)
async def Load(ctx, extention):
	try:
		await Kat.load_extension('cogs.{0}'.format(extention))
		print('Loaded {0}'.format(extention))
		await ctx.message.delete()
		await ctx.send(f"{extention} added")
	except Exception as e:
		print('{0} error [{1}]'.format(extention, e))
		em= Embed(title="Error", description= e, colour= Colour.red()).set_footer(text= 'Loading exception')
		await ctx.send(embed=em)

@Kat.command(hidden=True)
@commands.check(mee)
async def Unload(ctx, extention):
	try:
		await Kat.unload_extension(f'cogs.{extention}')
		print('unloaded {0}'.format(extention))
		await ctx.message.delete()
		await ctx.send(f"Removed {extention}")
	except Exception as e:
		print('Error: [{0}]'.format(e))
		ctx.message.delete()
		em= Embed(title="Error",description=e, colour= Colour.red())
		em.set_footer(text='Unload exception')
		await ctx.send(embed= em)

@Kat.command(hidden=True)
@commands.check(mee)
async def Reload(ctx, extention):
	try:
		await Kat.unload_extension('cogs.{0}'.format(extention))
		await Kat.load_extension('cogs.{0}'.format(extention))
		print('Reloaded {0}'.format(extention))
		await ctx.message.delete()
		await ctx.send("Reloaded")
	except Exception as e:
		print(e)
		await ctx.message.delete()
		em= Embed(title="Error", description=e, colour=Colour.red())
		em.set_footer(text='Reloading exception')
		await ctx.send(embed=em)


if __name__ == '__main__':
	for ex in extentions:
		try:
      #commands.Cog.cog_load('cogs.{0}'.format(ex))
      #print("yes")
			asyncio.run(Kat.load_extension('cogs.{0}'.format(ex)))
			print(f"{ex} loaded")
		except Exception as error:
			print('{0} cannot be loaded [{1}]'.format(ex, error))


# cmds
@Kat.hybrid_command(aliases=["الساعة","ساعة","الوقت"])
async def clock(ctx):
	a = datetime.utcnow()
	em= Embed(title="Right now", description="It's {0}:{1} GMT{2}".format(a.hour, a.minute, mood), timestamp=a,colour=Colour.green())
	await ctx.send(embed=em)

        
@Kat.hybrid_command(aliases=["مساعده","مساعدة"], hidden= True)
async def halp(ctx):
  await ctx.send_help()


@Kat.command(aliases= ['shc'], hidden= True)
async def showcode(ctx, args):
        '''Shows code of a command;
        (Prints: 1st- exact cmd name, KeyError: gets cmd by alias + prints cmd name, Modules: searches for non-cmd parts''' #, cogs: Searches other cogs, classes)
        await ctx.typing()
        print(args)
        try:
            print("1st") # works when exact cmd name is given
            code = getsource(typing.cast(typing.Callable, globals()[args].callback))
        except:
            print("KeyError")
            cmd = Kat.get_command(args)
            print(cmd) # works when an alias of a cmd is given
            if cmd:
                #await ctx.send(dir(cmd.callback))
                code = getsource(typing.cast(typing.Callable, cmd.callback))
            else:
                try: # should return a module and/or other parts that are not a cmd
                    print("Modules")
                    code = getsource(globals()[args])
                except:
                    print("Not Found\n")
                    await ctx.send(embed=Embed(title="E 404",description= "Command not found!", colour= discord.Colour.red()))
                    return
        code = re.sub(r"\`", "\\`", code)
        lines = code.splitlines(keepends = True)
        codelines = ""
        line_nr = 0
        spaces = len(str(len(lines))) - 1
        print(spaces)

        for line in lines:
            if len(codelines) < 1500:
                codelines += f"{line_nr}.{' ' * (spaces - len(str(line_nr)) + 1)}|{line}"
            else:
                await ctx.send(f"```python\n{codelines}```")
                codelines = f"{line_nr}.{' ' * (spaces - len(str(line_nr)) + 1)}|{line}"
            line_nr += 1
        else:
            await ctx.send(f"```python\n{codelines}```")


#@Kat.command()
#@commands.has_role("Guild Leader")
#async def Prefix(ctx,pr='sw!'):
#    global p
#    if pr == p :
#        ctx.send(f"prefix hasn't changed{mood}")
#    p = f"{pr}"
#    await ctx.channel.send("New prefix is `{}`".format(p))
# # The actual prefix can't change like that!


@Kat.command(hidden=True)
async def mode(ctx, value:int):
    global mood
    if value == 0:
      mood = ''
    if value == 1:
      mood='~'
      pass
    elif value == 2:
      mood = " nya"
    await ctx.send("Okay{0}".format(mood))
    db["mood"] = mood

#special response from me (or flamegorl)
@Kat.command()
async def flamegorl(ctx):
    mood = db['mood']
    if ctx.author.id == 444806806682730496:
      await ctx.channel.send("That's Aurumiel-sama{0}!".format(mood))
    elif ctx.author.id == 146828906069098496:
      await ctx.send("Yes, You!{0}".format(mood))
    else:
      await ctx.send("Don't bully Aurumiel-sama!")

@Kat.command(hidden=True)
async def db_keys(ctx,*,v:str =None):
    if ctx.author.id == 444806806682730496:
      if v:
        s=db[v]
      else:
        v = db.keys()
        #print(v)
        s=[]
        for i in v:
          print(i)
          s.append(i)
          
      await ctx.send(s if s else 'None') ## if/else statement in a single line! (don't put colons)

@Kat.command(hidden=True)
async def die(ctx):
	if ctx.author.id == 444806806682730496:
		await ctx.send("Okay")
		await Kat.close()
	else:
		await ctx.send("Nope!{0}".format(mood))

@Kat.command(hidden=True)
async def Shutdown(ctx):
	await die(ctx)


keep_alive()
Kat.run(os.getenv("TOKEN"))