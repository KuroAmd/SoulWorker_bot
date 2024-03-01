import discord
from discord.ext import commands
import datetime
from discord import Embed
#import asyncio
#import os
#from replit import db

def wel_ch(m):
  channel = m.guild.system_channel
  print()
  if channel==None:
    try:
      channel = discord.utils.get(m.guild.channels, name='general')
    except:
      pass
  return channel

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client._last_member = None
    
    #Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
      mood = db['mood']
      welcomer= db['welcomer']
      print(f"{member.name}\njoined at {datetime.datetime.utcnow()}")
      if isinstance(welcomer, discord.TextChannel):
        channel = welcomer
      else:
        channel=wel_ch(member)
      if welcomer:
        if channel:
          await channel.send('Welcome {0.mention}!{1}'.format(member,mood))

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(member.name+"\nleft at")
        channel=wel_ch(member)
        print(f'{member} has left a server')
        if channel is not None:
            await channel.send(f"{member} has left the server...")

   # @commands.Cog.listener()
   # async def on_reaction_add(self, reaction, user):
   #     fl=('')
   #     if reaction in fl:
   #         await reaction.Message.add_reaction()

    #Cmds

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Welcomer(self,ctx,v):
        "toggle the welcome response message"
        if not isinstance(v, discord.TextChannel):
          v1= discord.utils.get(ctx.guild.channels,id=v)
        if not isinstance(v1, discord.TextChannel):
          v1= discord.utils.get(ctx.guild.channels,name=v)
        if v1:
          welcomer = v1
        else:
          welcomer = v
        print(welcomer)
        print(db["welcomer"])
        bmsg=await ctx.send("Welcomer is set to {0}".format(welcomer))
        await bmsg.delete(delay=5)
        db["welcomer"] = welcomer

    @commands.command(aliases=["مرحبا"])
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello""" # _last_member is not defined #2023-6: fixed
        member = member or ctx.author
        if self.client._last_member is None or self.client._last_member.id != member.id:
            await ctx.send('Hello {0.name}{1}'.format(member, db['mood']))
        else:
            await ctx.send('Hello {0.name}... Haven\'t we met recently?'.format(member))
        self.client._last_member = member
    
    @commands.command()
    async def Weltest(self,ctx,*, ch:discord.TextChannel=None):
        member= ctx.author
        if ch:
          channel=ch
        else:
          channel=wel_ch(member)
        if channel is not None:
          await channel.send('Welcome {0.mention}!{1}'.format(member,db['mood']))
        else:
          await ctx.send("Which channel was it?")


    @commands.command(aliases=["لینک"],hidden= True)
    async def B_inv(self, ctx,perm=0):
        if perm==1:## generate general link (bad gateway)
            lnk = discord.utils.oauth_url(client_id=self.client.user.id, permissions=discord.Permissions)
        elif perm==0:## no perm link
          lnk = "https://discord.com/api/oauth2/authorize?client_id=752123777571094638&scope=bot"
        else:## admin perm link
            lnk = "https://discord.com/api/oauth2/authorize?client_id=752123777571094638&permissions=8&scope=bot"
        await ctx.message.delete()
        print(lnk)
        em= Embed(title="Invite me to a server~",description=lnk, url=lnk, colour=16777215)
        await ctx.send(embed=em)



async def setup(client):
    await client.add_cog(Greetings(client))