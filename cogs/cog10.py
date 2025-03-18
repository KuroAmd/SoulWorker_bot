import discord
#from discord import Embed
from discord.ext import commands
#import random
#import datetime


class Custom_cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.group()
    async def git(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid git command passed...')

    @git.command()
    async def push(ctx, remote: str, branch: str):
        await ctx.send('Pushing to {} {}'.format(remote, branch))
## This could then be used as ?git push origin master.

    @commands.command()
    async def open_file(self, ctx, fname):
        with open(fname, 'rb') as fp:
            await ctx.send(file=discord.File(fp, 'new_filename.png'))


async def setup(client):
    await client.add_cog(Custom_cmd(client))
    await client.add_cog(Custom_cmd(client))