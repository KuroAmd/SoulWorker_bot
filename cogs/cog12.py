## make listen & talk cmds
## tts & stt

import discord
from discord.ext import commands
import voice_recv


class Tst(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttest(self, ctx):
        def callback(member, packet):
            print(member, packet)
            #await ctx.send(packet)

            ## voice power level, how loud the user is speaking
            # ext_data = packet.extension_data.get(voice_recv.ExtensionID.audio_power)
            # value = int.from_bytes(ext_data, 'big')
            # power = 127-(value & 127)
            # print('#' * int(power * (79/128)))
            ## instead of 79 you can use shutil.get_terminal_size().columns-1
        vc = await ctx.author.voice.channel.connect(cls=voice_recv.VoiceRecvClient)
        vc.listen(voice_recv.BasicSink(callback))

    @commands.command()
    async def ststop(self, ctx):
        ctx.voice_client.stop_listening()
        await ctx.voice_client.disconnect()

    @commands.command()
    async def enuf(self, ctx):
        await self.stop(ctx)
        await ctx.bot.close()

def setup(bot):
    bot.add_cog(Tst(bot))