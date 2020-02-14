import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import pytz
import json

with open("./admin.json") as f:
    permission = json.load(f)

tz = pytz.timezone('Asia/Taipei')
title = ""
title_url = "https://www.youtube.com/channel/UCVF3bTd3dxM4IfOMFCbNADA"
helpmsg = "如要使用請在指令前方打上 c> (只有管理員才可使用)"


class trick(Cog_Extension):
    """雜七雜八"""

    @commands.Cog.listener()  #使用者加入
    async def on_member_join(self, member):
        
        time = datetime.datetime.now(tz).strftime("%Y-%m-%d %I:%M:%S %p")
        channel = self.bot.get_channel()
        role_c = self.bot.get_channel()
        # embed
        embed = discord.Embed(title=title, color=0x606060, url=title_url)
        embed.set_thumbnail(
            url="http://www.pngmart.com/files/3/Welcome-PNG-File.png")
        embed.add_field(
            name="歡迎你~",
            value=f"歡迎{member.mention}。\n發言之前，先到{role_c.mention}觀看本群規則喔!!",
            inline=False)
        embed.set_footer(text=f"現在時間:{time}")
        await channel.send(embed=embed)

    @commands.command()  #時間
    async def time(self, ctx):
        user_id = ctx.message.author.id
        if str(user_id) in permission["admin"]:  #有權限
            time = datetime.datetime.now(tz).strftime("%Y-%m-%d %I:%M:%S %p")
            # embed
            embed = discord.Embed(title=title, color=0x606060, url=title_url)
            embed.set_thumbnail(
                url="https://img.icons8.com/cotton/2x/time-1.png")
            embed.add_field(name="現在時間", value=f"{time}", inline=False)
            embed.set_footer(text=helpmsg)
            await ctx.send(embed=embed)
        else:  #沒權限
            pass

    @commands.command(pass_context=True)  #HELP
    async def help(self, ctx):
        user_id = ctx.message.author.id
        if str(user_id) in permission["admin"]:  #有權限
            embed = discord.Embed(title=title, color=0x606060, url=title_url)
            embed.set_thumbnail(
                url="https://img.icons8.com/plasticine/2x/about.png")
            embed.add_field(
                name="管理專用", value="clear + 數字 `=>` 清除數筆訊息", inline=False)
            embed.add_field(
                name="根本沒用",
                value="time `=>` 查詢時間\nhelp `=>` 使用幫助",
                inline=False)
            embed.set_footer(text=helpmsg)
            await ctx.send(embed=embed)
        else:  #沒權限
            pass

    @commands.command() #查詢伺服器狀態
    async def info(self,ctx):
        user_id = ctx.message.author.id
        if str(user_id) in permission["admin"]:  #有權限
            server_name = ctx.guild.name
            server_create_date = ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
            server_user = len(ctx.guild.members)
            text_channel = len(ctx.guild.text_channels)
            voice_channel = len(ctx.guild.voice_channels)
            # embed 訊息
            embed = discord.Embed(title=title, color=0x606060, url=title_url)
            embed.set_thumbnail(
                    url="https://img.icons8.com/plasticine/2x/about.png")
            embed.add_field(name="伺服器訊息", value=f"名稱：{server_name}\n創建日期：{server_create_date}\n伺服器人數：{server_user}\n文字頻道：{text_channel}\n語音頻道：{voice_channel}\n機器人延遲：{round(self.bot.latency*1000)} ms", inline=False)
            embed.set_footer(text=helpmsg)
            await ctx.send(embed=embed)
        else:  #沒權限
            pass            

def setup(bot):
    bot.add_cog(trick(bot))
