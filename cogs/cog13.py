import discord
from discord.ext import commands

class Select(discord.ui.select):
  def __init__(self):
    opts =[
      discord.SelectOption(label="Blue TM", emoji="blueberries", description="The Blue Team"),
      discord.SelectOption(label="Red TM", emoji="apple", description="The Red Team"),
      discord.SelectOption(label="Green TM", emoji="leafy_green", description="The Green Team")
    ]
    super().__init__(placeholder="Choose your team", max_values=1, min_values=1, options= opts)

  async def callback(self, interaction: discord.Interaction):
      u= interaction.user
      guild= interaction.guild
      ## Here create colour roles
      

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 20):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Menu(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def menu(self,ctx):
    """testing discord.ui"""
    await ctx.send("pick a team!", view= SelectView(), delete_after= 10)

  
async def set_up(bot):
  await bot.add_cog(Menu(bot))