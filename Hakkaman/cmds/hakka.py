import discord
from discord.ext import commands
from core.classes import Cog_Extension,Color

class hakka(Cog_Extension):

    @commands.command()
    async def about(self,ctx):
        '''關於此機器人'''
        embed=discord.Embed(title="關於/About",color=Color.embed_normal)
        embed.set_thumbnail(url="https://truth.bahamut.com.tw/s01/201903/23a81e36725a207faa1bf9d85a250e6e.JPG")
        embed.add_field(name="作者/Author",value="minexo79",inline=False)
        embed.add_field(name="建立日期/Build Date",value="20200127",inline=False)
        embed.add_field(name="版本/Version",value="1.0(Hakka)",inline=False)
        embed.set_footer(text="客家人寫什麼聊天機器人?都馬撿現成的。要把寫機器人的力氣省下來！")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(hakka(bot))