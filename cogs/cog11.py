import discord
from discord import Embed
from discord.ext import commands
#import random
import aiohttp
import datetime
#import asyncio
#import io
#import os
import google_trans_new
import wikipedia
from worldmeter.coronavirus import CovidMeter
from worldmeter.population import PopulationMeter

Cov = CovidMeter()
pop = PopulationMeter()


def what_is(query, session_id="general"):
    try:
    #if False:
        print(wikipedia.search(query))
        return wikipedia.summary(query)
    except Exception:
    #else:
        for new_query in wikipedia.search(query):
            try:
                print('new: '+new_query)
                page = wikipedia.page(new_query)
                page = page.title
                sum_ = wikipedia.summary(new_query)
                return sum_, page
            except Exception:
                pass
    return "I don't know about "+query
    print("no result on"+ query)

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print("Status:", res.status)
            print("Content-type:", res.headers['content-type'])
            html = await res.text()
            print(html)
            

class Informations(commands.Cog):

    @commands.command()
    async def wiki(self, ctx,*, search):
        sm, titl = what_is(search)
        print(sm)
        await ctx.send(embed= Embed(title=titl, description=sm, timestamp=datetime.datetime.utcnow(), colour= discord.Colour.green()))

    @commands.command(aliases=['cur','convert_currency'])
    async def currency(self, ctx, fr, to = None):
        try:
            url = f"https://v6.exchangerate-api.com/v6/4d0dd59b0a26d65003cb5582/latest/{fr}"
        except:
            url = "https://v6.exchangerate-api.com/v6/4d0dd59b0a26d65003cb5582/latest/USD"

        se= aiohttp.ClientSession()
        res = se.get(url)
        data = res.json()

        #print(data)
        print(data['conversion_rates'])
        if not to:
            await ctx.send(data['conversion_rates']['AED'])
            await ctx.send(data['conversion_rates']['JPY'])
        else:
            await ctx.send(data['conversion_rates'][to])

    # needa embed this


    @commands.command()
    async def Spelling(self, ctx, s:str):


        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/spelling/SpellCheck"

        querystring = {"text": s }

        headers = {
            'x-rapidapi-key': "b083b6b7e3msh2491693f4c81f47p16c8d9jsn5bdabe35ae9d",
            'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
            }

        se= aiohttp.ClientSession()
        response = se.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        await ctx.send(response.text)

    @commands.command(aliases=['Tran','tran','t'])
    async def Translate(self,ctx,*, msg):
        gt = google_trans_new.google_translator()
        print(msg)
        tmsg = gt.translate(msg, lang_tgt='en')
        print(tmsg)
        await ctx.send(embed=discord.Embed(title="translation", description=tmsg, colour=ctx.author.colour))
        #print(bmsg)


    @commands.command()
    async def corona(self, ctx, country=None):
        if not country:
            data = Cov.global_data()  # # This is currently BROKEN
            titl = "Covid_19 News"
        else:
          try:
            titl = "Covid_19 in "+ str(country)
            data = Cov.get_country_data(country)  # # country names, NOT country code
          except Exception as e:
            print("invalid")
            print(e)
            await ctx.send(e)
        print(data)
        await ctx.send(embed=Embed(title=titl, description=data,colour=discord.Colour.green()))

    @commands.command()
    async def population(self,ctx):
        data = pop.get_population_data()
        print(data)
        await ctx.send(embed=Embed(title="world's population", description=data,colour=discord.Colour.green(),timestamp=datetime.datetime.utcnow()))


#
#   @commands.command(aliases=['timenow'])
#   async def clock(self,ctx):
#        a=datetime.datetime.utcnow()
#        await ctx.send(embed=discord.Embed(title="Right now",description="It's {0}:{1} GMT{2}".format(a.hour,a.minute,mood),timestamp=datetime.datetime.utcnow(),colour=discord.Colour.green()))
#


def setup(client):
  client.add_cog(Informations(client))