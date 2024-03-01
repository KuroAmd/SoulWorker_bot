import discord
#import nextcord.ext
from discord.ext import commands
from discord import Embed, app_commands
#from replit import db
#import datetime
import random
import aiohttp
from aiohttp import request
from bs4 import BeautifulSoup
#import json
import io
#import os
import animec
#mood = db['mood']

#gid= discord.Object(id= 727092352363135077)

somerandapi = "https://some-random-api.com"

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        html = await res.text()
        return html

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    def adminpowa(ctx):
      print(ctx.author)
      return (ctx.author.id==444806806682730496) or (ctx.channel.permissions_for(ctx.author).administrator)

    ##Events

    ##Cmds

    ## from the docs
    def to_upper(argument):
        return argument.upper()
    @commands.command()
    async def scream(ctx, *, content: to_upper):
        await ctx.send(content)

        
    # CERN
    @commands.hybrid_command(aliases=['CERN',"المنظمة","سیرن"])
    @app_commands.guilds()
    async def cernnews(self, ctx):
        await ctx.typing()

        website = "https://home.cern/news?audience=23"
        html_text = await fetch(website)
        soup = BeautifulSoup(html_text, 'html.parser')
        news = soup.find_all('div',class_='views-row')
        
        for n in news:
            try:
                headlines = n.find('h3', class_='preview-list-title').text
            except:
                print(f"error{n}")
                continue
            try:
                description = n.find('div', class_='preview-list-strap').text
                news_date = n.find('div', class_='preview-list-date has-separator').text
                more_info = ("https://home.cern" + n.h3.a['href'])
            except:
                print("something went wrong")
                await ctx.send("err")
            await ctx.send(f'''
            headlines: {headlines.strip()}
            description: {description.strip()}
            date: {news_date.strip()}\n
            look in {more_info}
            ''')
            if(headlines != None):
                break

#just embed it later


    @commands.hybrid_command(aliases=['numbersfact'], description= "facts on any number! about **trivia / math / date / year**")
    @app_commands.guilds()
    async def facts(self, ctx, num='random', typ='trivia'):
      if typ=='maths':
        typ='math'
      res= await fetch(f'http://numbersapi.com/{num}/{typ}')
      await ctx.send(res)


    @commands.hybrid_command(aliases=["انتهی","بوري"])
    @app_commands.guilds()
    async def wasted(self, ctx, u: discord.Member=None):
        if not u:
            u = ctx.author
        
        wastedsession = aiohttp.ClientSession()
        async with wastedsession.get(somerandapi + f"/canvas/wasted?avatar={u.avatar.url}") as img:
            if img.status != 200:
                print(img.status)
                await ctx.send("Unable to get image")
                await wastedsession.close()      
            else:
                data = io.BytesIO(await img.read())
                await ctx.send(file=discord.File(data, 'wasted.png'))
                await wastedsession.close()


    @commands.hybrid_command(aliases=['animalfact','afact','حیوانات'], description="about different animals (but specify which ^_^)")
    @app_commands.guilds()
    async def animal(self,ctx, animal: str):
        """read a funfact with a random cute picture about an animal! (the pic is not related to the funfact)"""
        animals=("dog","cat","panda","fox","bird","koala","kangaroo")
        if animal.lower() not in animals:
          await ctx.send(embed=Embed(title="please choose from:",description=f"{animals}"))
        elif animal.lower() in animals:
            fact_URL= somerandapi + f"/facts/{animal.lower()}"
            img_URL= somerandapi + f"/img/{animal.lower()}"

            async with request("GET",img_URL,headers={}) as response:
                if response.status==200:
                    data= await response.json()
                    img_link=data["link"]

            async with request("GET",fact_URL,headers={}) as response:
                if response.status == 200:
                    data = await response.json()

                    em=Embed(title=f"{animal.title()} fact",
                                description=data["fact"],
                                colour = ctx.author.colour)
                    em.set_image(url=img_link)
                    await ctx.send(embed=em)
                else:
                    await ctx.send(f"API returned: {response.status}")
        else:
            await ctx.send(f"Nothing found for {animal.lower()}")


    @commands.hybrid_command(aliases=['غمز'])
    @app_commands.guilds()
    async def wink(self,ctx):
        async with request("GET",somerandapi + "/animu/wink",headers={}) as response:
            if response.status==200:
                data= await response.json()
                ImgLink=data["link"]
                em = Embed(title=f"{ctx.author} winks")
                em.set_image(url=ImgLink)
                em.set_footer(text="-",icon_url=ctx.author.display_avatar)
                await ctx.send(embed=em)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=['تربيت'])
    async def pat(self,ctx,u:discord.Member=None):
        async with request("GET",somerandapi + "/animu/pat",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["link"]
                if (u==None):
                    em=Embed(title=f"pats {ctx.author.display_name}")
                    em.set_image(url=ImgLink)
                else:
                    em=Embed(title=f"{ctx.author.display_name} pats {u.display_name}")
                    em.set_image(url=ImgLink)
                await ctx.send(embed=em)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=["ضم"])
    async def hug(self,ctx,u:discord.Member=None):
        async with request("GET",somerandapi + "/animu/hug",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["link"]
                if (u==None):
                    em=Embed(title=f"hugs {ctx.author.display_name}")
                    em.set_image(url=ImgLink)
                else:
                    em=Embed(title=f"{ctx.author.display_name} hugs {u.display_name}")
                    em.set_image(url=ImgLink)
                await ctx.send(embed=em)
            else:
                await ctx.send("API returned: {0.status}".format(response))

    @commands.command(aliases=["میم"],brief="LOL",description="You don't need help for this one :P")
    async def meme(self,ctx):
        await ctx.typing()
        async with request("GET",somerandapi + "/meme",headers={}) as response:
            if response.status==200:
                data=await response.json()
                ImgLink=data["image"]
                Cap=data["caption"]
                Categ=data["category"]
                em=Embed(title=f"{Cap}",description=f"{Categ}")
                em.set_image(url=ImgLink)
                em.set_footer(text="-",icon_url=ctx.author.display_avatar)
                await ctx.send(embed=em)
            else:
                await ctx.send("API returned: {0.status}".format(response))



    @commands.command(aliases=['say','repeat','RepeatAfterMe',"قل"],
    brief="Tell me what to say", description="I will 'repeat after you'")
    async def Say(self,ctx, *, msg):
        if isinstance(ctx.channel,discord.DMChannel):
          msg= msg.split()
          i= msg.pop(0)
          msg= ' '.join(msg)
          print(i)
          for g in self.client.guilds:
            ch= discord.utils.get(g.channels, id=int(i))
            if ch:
              print(ch)
              break
        else:
          ch = ctx.channel
        print(ch)
        await ch.send(str(msg))

    @commands.command(hidden=True)
    @commands.check(adminpowa)
    async def Sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(f"{msg} {db['mood']}")

    @commands.command(aliases=["اختر","اختیار"])
    async def choose(self,ctx,*, msg):
        choices = msg.split(' or ')
        print(choices)
        await ctx.send("{1} choices {0}".format(len(choices), " or ".join(choices)))
        await ctx.send(f"Hmm?~\n{random.choice(choices)} of course!{db['mood']}")


    @commands.command(aliases=['8ball','question','q',"سوال"],description="Ask and I shall answer!~ (please ask a yes/no question)")
    async def eightball(self,ctx,* ,question):
      responses= ["Yes!", "Of course!", "Why not?", "Sure!", "Certainly",
      "100 Percent! \n~~unless my calculations are wrong... which is likely~~", "I'd say... Definitely!", "There's no doubt about it!", "Possible...", "Maybe~", "Don't lose hope~!", 
      "Uhh... I'm not sure", "I DON'T KNOW! >_<", "I wonder... maybe?", "Very doubtful","I don't think so", "And my answer will be... no", "Of course not!", "No way", "Nah", "Nuh-uh!", "And no", "N O",
      "ahhh My head hurts x_x", "Need to think about that... Ask again"]
      
      #await ctx.send
      print(f"Q asked: {question}?")

      await ctx.reply(f"{random.choice(responses)} {db['mood']}")

# # Animec api
    @commands.command(aliases=["انيمي","انیمه"])
    async def anime(self,ctx,*,query):
      try:
        anime = animec.Anime(query)
      except:
        await ctx.send(embed= Embed(description=f"No corresponding anime is found for \"{query}\"", colour=discord.Colour.red()))
        return
      em= Embed(title=anime.title_english, url= anime.url, description= anime.description[:200], colour=56550)
      em.add_field(name="Episodes", value= str(anime.episodes))
      em.add_field(name="Rating", value= str(anime.rating))
      em.add_field(name="Broadcast", value= str(anime.broadcast))
      em.add_field(name="Status", value= str(anime.status))
      em.add_field(name="Type", value= str(anime.type))
      em.set_thumbnail(url= anime.poster)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['Nyan','nyan','neko',"مياو"])
    async def Neko(self,ctx):
      a= animec.Waifu.neko()
      em= Embed(title=f"{ctx.author.name} meows~",colour=ctx.author.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=['happy',"سعيد","سعید"])
    async def Happy(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.happy()
      em= Embed(title=f"{u.name} is happy! yay{db['mood']}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["احو"])
    async def awoo(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.awoo()
      em= Embed(title=f"{u.name} awoos~",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    
    @commands.command(aliases=['grin',"تکشير"])
    async def smug(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.smug()
      em= Embed(title=f"{u.name} smugs",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["يبتسم","ابتسم","ابتسام"])
    async def smile(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.smile()
      em= Embed(title=f"{u.name} smiles",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["صفع"])
    async def slap(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.slap()
      em= Embed(title="slap! Ouch",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["رقص"])
    async def dance(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.dance()
      em= Embed(title=f"{u.name} dances",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["غمزة"])
    async def wink2(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.wink()
      em= Embed(title=f"winks for {u.name}< ~",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)
    
    @commands.command(aliases=["تنمر"])
    async def bully(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.bully()
      em= Embed(title=f"bully {u.name}! boo~",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['nuzzle',"شبق"])
    async def cuddle(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.cuddle()
      em= Embed(title=f"cuddles {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=["بکاء","يبکي"])
    async def cry(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.cry()
      em= Embed(title=f"{u.name} cries... what's wrong?",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['cringe',"کرینج"])
    async def cringy(self,ctx):
      a= animec.Waifu.cringe()
      em= Embed(title="Oh nO cRiNgE!",colour=ctx.author.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=["sss"])
    async def blush(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.blush()
      em= Embed(title=f"{u.name} blushes~",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['a',"عض"])
    async def bite(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.bite()
      em= Embed(title=f"{ctx.author.display_name} bites {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['eat',"عم","اکل"])
    async def nom(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.nom()
      em= Embed(title=f"{u.name} noms",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=["هز"])
    async def poke(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.poke()
      em= Embed(title=f"pokes {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=["ششش"])
    async def pat2(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.pat()
      em= Embed(title=f"here here {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['slurp',"لعق"])
    async def lick(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.lick()
      em= Embed(title=f"licks {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['hi5',"احسنت"])
    async def highfive(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.highfive()
      em= Embed(title=f"High Five! {u.name}",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['reee',"رييييي","رييي","رییی"])
    async def yeet(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.yeet()
      em= Embed(title=f"{u.name} got YEETED!",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['kill',"قتل"])
    async def KILL(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.kill()
      em= Embed(title=f"{ctx.author.display_name} kills {u.name} :drop_of_blood: ",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['smooch',"بوس"])
    async def kiss(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.kiss()
      em= Embed(title=f"kisses {u.name}:kiss: ",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['handhold','hands',"امسک يدي"])
    async def holdhand(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.handhold()
      em= Embed(title=f"{ctx.author.display_name} holds {u.name}\' hand~",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['gtfo',"اطلع","برا"])
    async def kicking(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.kick()
      em= Embed(title=f"get out {u.name}! ||Just kidding~||",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)

    @commands.command(aliases=['supersad',"حزن"])
    async def glomp(self,ctx,u:discord.Member=None):
      if not u:
        u= ctx.author
      a= animec.Waifu.glomp()
      em= Embed(title=f"Come here~, HUGS {u.name}!",colour=u.colour)
      em.set_image(url=a)
      em.set_footer(text= "-", icon_url= ctx.author.display_avatar)
      await ctx.send(embed=em)


async def setup(client):
    await client.add_cog(Fun(client))