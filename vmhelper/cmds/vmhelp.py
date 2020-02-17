import discord # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import embedconfig

class vmhelp(Cog_Extension):
    """雜七雜八"""     

    @commands.Cog.listener() #使用者加入
    async def on_member_join(self,member):
        channel=self.bot.get_channel(620780437672820768)
        role_c=self.bot.get_channel(620780192553762837)
        # embed
        embed = discord.Embed(color=embedconfig.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/621293180964569089.png?v=1")
        embed.add_field(name="!!新夥伴加入!!",value=f"歡迎{member.mention}!!\n先到{role_c.mention}觀看本群規則喔!!", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await channel.send(embed=embed)

    @commands.command() #關於
    async def about(self,ctx):
        embed = discord.Embed(color=embedconfig.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/621293042900402176.png?v=1")
        embed.add_field(name='關於', value='在下是這裡的小助手，\n我的主人是<@191356691185401856>，有甚麼不會的就打`>help`吧!', inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)

    @commands.command() #查詢伺服器狀態
    async def info(self,ctx):
        server_name = ctx.guild.name
        server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        server_user = len(ctx.guild.members)
        text_channel = len(ctx.guild.text_channels)
        voice_channel = len(ctx.guild.voice_channels)
        # embed 訊息
        embed = discord.Embed(color=embedconfig.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/621293042900402176.png?v=1")
        embed.add_field(name="伺服器訊息", value=f"名稱：{server_name}\n創建日期：{server_create_date}\n伺服器人數：{server_user}\n文字頻道：{text_channel}\n語音頻道：{voice_channel}\n機器人延遲：{round(self.bot.latency*1000)} ms", inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)
    
    @commands.command(pass_context = True) #Help
    async def help(self,ctx):
        embed = discord.Embed(title='幫助',color=embedconfig.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/621293042900402176.png?v=1")        
        embed.add_field(name='釣魚', value=">fish now (開釣)\n>fish reg (玩家註冊)\n>fish reg (經驗查詢)", inline=False)
        embed.add_field(name='清除訊息', value='>msgclear + 數字', inline=False)
        embed.add_field(name='關於伺服器', value='>info', inline=False)
        embed.add_field(name='關於此機器人', value='>about', inline=False)
        embed.set_footer(text=embedconfig.footer)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(vmhelp(bot))       
