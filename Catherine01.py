import discord
from discord.ext import commands
import os

Kat = commands.Bot(command_prefix = 'sw!')
mood = ''

#events
@Kat.event
async def on_ready():
    print("Catherine is on!")

@Kat.event
async def on_member_join(member):
    print(f"{member} joined!")
    general_ch= Kat.get_channel(727092352807731272)
    await general_ch.send(f"Welcome {member}!{mood} \nEnjoy here and feel like home!{mood}")

@Kat.event
async def on_member_remove(member):
    print(f"{member} has left!")
    general_ch= Kat.get_channel(727092352807731272)
    await general_ch.send(f"{member} has left... aww")

#@Kat.event
#async def on_message(self,msg):
#    if msg.content.startswith('Hi' or 'Hello' or 'hi' or 'hello' or 'Hey'):
#        await msg.channel.send("Hello hello!")
#    if msg.content("Why don't you die?"):
#        await .send("Okay")

#spy
@Kat.event
async def on_user_update(before,after):
    print(f"a user changed to: {after}")

#cmds
@Kat.command(aliases=['RepeatAfterMe'])
async def repeat(ctx,*,msg):
    await ctx.send(f"{msg}{mood}")

@Kat.command()
async def story(ctx,character):
    if character == 'Catherine' or 'catherine':
        await ctx.send("I always aimed to be a strong Soul-- and eventually a strong Soulworker!\n")
    elif character == 'Erwin' or 'erwin' or 'Arclight':
        await ctx.send("What Erwin is to me?")
        await ctx.send("First time I saw him, he inspired me!\nHe always does his best and doesn't give up! And he's always been nice to me... So I kind of, love Erwin!\nI gave Erwin a wire ring that I made, maybe it's not very well-made, but he always wears it!")
    elif character == 'Jin' or 'jin' or 'Seipatsu':
        await ctx.send("What do I think of Jin?")

    elif character == '':
        await ctx.send("uh")
        
    else:
        await ctx.send("Who?")

@Kat.command()
async def Kill(ctx, amt=10):
    await ctx.channel.purge(limit=amt)
    await ctx.channel.send(f"{amt} souldregs were killed{mood}!")

@Kat.command()
async def mode(ctx,value):
    global mood
    if value == '0':
        mood = ''
    if value == '1':
        mood = '~'
    await ctx.send("Okay{0}".format(mood))

#Only respond from me (or flamgorl)
@Kat.command()
async def flamegorl(ctx):
    if ctx.author.id == 444806806682730496:
        await ctx.channel.send("That's Aurumiel-sama{0}!".format(mood))
    elif ctx.author.id == 146828906069098496:
        await ctx.send("Yes, You!{0}".format(mood))
    else:
        await ctx.send("Don't bully Aurumiel-sama!")

@Kat.command()
async def die(ctx):
    if ctx.author.id == 444806806682730496:
        await ctx.send("Okay")
        await Kat.logout()
    else:
        await ctx.send("Nope!{0}".format(mood))

@Kat.command()
async def shutdown(ctx):
    await die(ctx)

Kat.run(os.environ['Disc_Token'])