import discord
from discord.ext import commands
from core.classes import Cog_Extension,Color

class manage(Cog_Extension):

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def test(self,ctx):
        '''檢查訊息管理權限'''
        embed=discord.Embed(title="Congraduations! You can manage messages.", color=Color.embed_pass)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,num:int):
        '''訊息清除'''
        await ctx.channel.purge(limit=num+1) 
        
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def re(self,ctx,extension):
        '''重新載入Extension'''
        self.bot.reload_extension(f"cmds.{extension}")
        print(f"| The [{extension}] was reloaded.")
        embed=discord.Embed(title=f"The `{extension}` was reloaded.", color=Color.embed_normal)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ow(self,ctx):
        '''查詢群主'''
        owner = ctx.guild.owner
        ownerid = ctx.guild.owner_id
        getowner_embed = discord.Embed(color=Color.embed_normal)
        getowner_embed.add_field(name="本群群主",value=owner,inline=False)
        getowner_embed.add_field(name="ID",value=ownerid,inline=False)
        await ctx.send(embed=getowner_embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def bye(self,ctx):
        '''機器人關閉'''
        await ctx.send("掰")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(manage(bot))