import discord,os  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension,Color

class log(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound):
            embed=discord.Embed(title=f"You type a wrong command!", color=Color.embed_error)
        elif isinstance(error,commands.MissingPermissions):
            embed=discord.Embed(title="You don't have the permission to do that!", color=Color.embed_error)
        elif isinstance(error,commands.MissingRequiredArgument):
            embed=discord.Embed(title="You need to specify a required argument!", color=Color.embed_error)
        else:
            embed=discord.Embed(title=f"Unknown error,check the console log!")
        # print to console
        print("|",error)
        # send to channel
        embed.add_field(name="----------------------------", value=f"{error}", inline=False)
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(log(bot))    