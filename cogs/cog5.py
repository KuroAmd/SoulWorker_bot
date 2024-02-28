#import discord
#from discord import Embed
from discord.ext import commands
#import random
#import datetime


class SoulWorker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.hybrid_command()
    async def story(self,ctx,character= "Catherine"):
        if (character == 'Catherine') or (character=='catherine'):
          await ctx.send("I always aimed to be a strong Soul-- and eventually a strong Soulworker! I would surpass all other soulworkers\n")
        elif (character == 'Erwin') or (character=='erwin') or (character=='Arclight'):
          await ctx.send("What Erwin is to me?")
          await ctx.send("First time I saw him, he inspired me!\nHe always does his best and doesn't give up! And he's always been nice to me... So I kind of, love Erwin!\nI gave Erwin a wire ring that I made, maybe it's not very well-made, but he always wears it!\nIt's a sign for our promise that in 5 years I'd be the most beautiful woman he ever saw and Erwin's bride!\n\nthe promise cannot be fulfilled, but he aims to create a better future with that image later")
        elif (character == 'Jin') or (character=='jin') or (character=='Seipatsu'):
          await ctx.send("What do I think of Jin?")

        elif character.lower() in ('haru','estia'):
          await ctx.send("What I think of Haru?")

        elif character.lower() in ('chii','aruel'):
          await ctx.send("Chii")
        elif character.lower() in ('lily','bloom-'):
          await ctx.send("What about lily?")
        elif character.lower() in ('ephnel'):
          await ctx.send("money")
        elif (character==None):
          await ctx.send("Ara ara~")

        elif (character==''):
          await ctx.send("uh")
              
        else:
          await ctx.send("Who?")


async def setup(client):
    await client.add_cog(SoulWorker(client))