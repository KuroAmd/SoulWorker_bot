import discord
from discord import Embed
#from nextcord.utils import get
from discord.ext import commands
from replit import db
import aiohttp
import random
import json
#import datetime
from google_trans_new import google_translator

p='sw!'

if 'member_spy' not in db.keys():
  db['member_spy']= None
if 'server_spy' not in db.keys():
  db['server_spy']= None
if 'mylog' not in db.keys():
  db['mylog']= None

# Encouragments
encourage = ['Cheer up!', "You are a great person!", "It's ok","You don't need to worry"]
sad = ['sad', 'depress', 'unhappy', 'miserable', "can't do"]

def update_encouragement(encouraging_msg):
	if "encouragements" in db.keys():
		encouragement = db["encouragements"]
		encouragement.append(encouraging_msg)
		db["encouragements"] = encouragement
	else:
		db["encouragments"] = [encouraging_msg]
    
def del_encouragement(index):
	encouragement = db["encouragements"]
	if len(encouragement) > index:
		del encouragement[index]
		db["encouragements"] = encouragement
if "responding" not in db.keys():
	db["responding"] = True
  
async def get_quote():
	async with aiohttp.ClientSession as sess:
		response = sess.get("https://zenquotes.io/api/random")
		json_data = json.loads(response.text)
		quote = json_data[0]['q'] + "\n-" + json_data[0]['a']
		return quote

#    # cmds on this cog don't work

class spy(commands.Cog):
    def __init__(self, client):
      self.client = client

	#Events

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction)
        print(user)
        #print(reaction.message)
        msg = reaction.message.content
        #print(msg)
        #print(self.client)
        if user==self.client.user:
            print("It's my reaction!")
            return
        if str(reaction.emoji)=="🏳️":
            gt = google_translator()
            tmsg = gt.translate(msg, lang_tgt='en')
            #print(tmsg)
            #print(reaction.message.channel)
            em = Embed(title=msg, description=tmsg, colour=user.colour)
            em.set_footer(text= reaction.message.author.display_name,icon_url=reaction.message.author.display_avatar)
            await reaction.message.channel.send(embed=em)
        #else:
        #    print(reaction)
        #    return
        #    print("dunno the reaction")



    #@commands.Cog.listener()
    #async def on_raw_message_delete(self, msg):
      #  if msg_del_log == True:
      #      try:
      #          em = Embed(description=ctx.discord.RawMessageDeleteEvent)
      #      except:
      #          pass
    #  em = Embed(title='Message deleted.',timestamp=datetime.datetime.utcnow())
    #  print('a msg deleted')
    #  await msg.channel.send(embed=em)

    #  else:
    #    pass

  #  @commands.Cog.listener()
  #  async def on_message_edit(self, ctx, user):
  #      print(ctx.message)
  #      print(user)

  #  @commands.Cog.listener() # did not seem to work
  #  async def on_user_update(self, ctx, before, after):
  #      print(before)
  #      print(after+'user update')
    
    @commands.Cog.listener()
    async def on_member_update(self, before:discord.Member , after:discord.Member):
      if db['member_spy']:
        print(before ,' >Member update> ' ,after)

    # add these in moderating maybe
    @commands.Cog.listener()
    async def on_guild_update(self,before:discord.Guild , after: discord.Guild):
      if db['server_spy']:
        print(before,'\n', after)

      if db['mylog']:
        await db['mylog'].send(embed=Embed(title="Server Update",description={after},colour=discord.Colour.orange()))
        
    #@commands.Cog.listener()
    #async def on_invite_create(self,invite):
    #  print(invite)
    #  ch=discord.utils.get(self.client.get_all_channels(), guild__name='【前代魂戦士】 (Prev. Gen. SoulWarriors)', name='vacuum-lab')
    #  print(ch)
    #  await ch.send(f"An invite link was created\n{invite}")

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before:discord.Emoji , after:discord.Emoji):
      print('Server: ', guild, '\n\n')
      print(before,'\n\nAfter:\n', after)
      if db['mylog']:
        try:
          await db['mylog'].send(embed=Embed(title="server emojis update",description=f"{after}",colour=discord.Colour.orange()))
        except:
          print("Can't send to ", db['mylog'])
          
  #  @commands.Cog.listener()
  #  async def on_voice_state_update(self, member, before, after):
  #    print(after)
  #    print(member)
  #    if db['mylog']:
  #      await db['mylog'].send(embed=Embed(title="voice state", description=f"{member.name} {after}", colour=discord.Colour.orange()))

    ## on_msg
    @commands.Cog.listener()
    async def on_message(self, msg):
      msgc = msg.content
      if msg.author == self.client.user:
        return
      elif self.client.user.mentioned_in(msg):
        Bmsg = await msg.channel.send("My prefix is **`{0}`**".format(p))
        await Bmsg.delete(delay=10)
#      elif msgc.startswith(('Hi', 'Hello', 'Hey', 'hi', 'hello')):
#        await msg.channel.send("Hey there!{0} :wave:".format(mood))
#      elif msg.content.startswith(('Bye', 'bye', 'Goodbye')):
#        await msg.channel.send("Take care!{0}".format(mood))
      elif msg.content == 'Send_Embed':
        myEmbed = discord.Embed(title="current ver", description="v0.3.1", color=0x00ff00) # green
        myEmbed.add_field(name="Catherine 입니다!", value="v.10", inline=False)
        myEmbed.add_field(name="released date", value='2020', inline=True)
        myEmbed.set_footer(text="Thisisthefooter")
        myEmbed.set_author(name="Mysterious Assassin")
        await msg.channel.send(embed=myEmbed)

    #  elif isinstance(msg.content, int):
    #      try:
    #        msg = await msg.fetch_message(msg.content)
    #        await msg.channel.send(msg)
    #        print(msg)
    #      except Exception as e:
    #        print(e)

      elif msgc.startswith("inspire") or msgc.startswith("الهام"):
        q = await get_quote()
        e= Embed(title="inspiration :sparks:",description=q, colour=56550)
        await msg.channel.send(embed=e)

      if db["responding"]:
        options = encourage
        if "encouragements" in db.keys():
          options = options + db["encouragements"]

        if any(word in msgc for word in sad):
          await msg.channel.send(random.choice(encourage))

      if msgc.startswith("SW!new"):
        encouraging_msg = msg.split("SW!new ", 1)[1]
        update_encouragement(encouraging_msg)
        await msg.channel.send("New encouraging message added")

      if msgc.startswith("SW!del"):
        encouragement = []
        if "encouragements" in db.keys():
          index = int(msgc.split("sw!del ", 1)[1])
          del_encouragement(index)
          encouragement = db["encouragements"]
        await msg.channel.send(encouragement)

      if msgc.startswith("SW!enouragements"):
        encouragement = []
        encouragement = db["encouragements"]
        await msg.channel.send(encouragement)

      if msgc.startswith("SW!responding"):
        value = msgc.split("SW!responding ", 1)[1]
        if value.lower() == "true":
          db["responding"] = True
          await msg.channel.send("Responding is on.")
        else:
          db["responding"] = False
          await msg.channel.send("responding is off.")
    #  await self.client.process_commands(msg) # # this will destroy the code! (double response)


async def setup(client):
	await client.add_cog(spy(client))