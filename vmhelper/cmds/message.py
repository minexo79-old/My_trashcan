import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import random

class message(Cog_Extension):
    """訊息功能"""

    @commands.command() #清理訊息
    async def msgclear(self,ctx,num:int):
        await ctx.channel.purge(limit=num + 1)
        await ctx.send("訊息清除完畢!")
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)   

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == "ping" and msg.author != self.bot.user:  # 乒乓
            await msg.channel.send(f"Pang!")

        elif msg.content == '早' and msg.author != self.bot.user:  # 早安
            morning=["早安~","早安喔~","早安~","早ㄢ!!","歐嗨喲~","安安~"]
            random_mes=random.choice(morning)
            user = msg.author.mention
            pic = discord.File(".//pic//goodmorning.png")
            await msg.channel.send(file=pic)
            await msg.channel.send(f"{user} {random_mes}")
        
        elif '讚喔' in msg.content and msg.author != self.bot.user:  # 早安
            morning=["棒棒棒!!","恭喜!!","好厲害!!"]
            random_mes=random.choice(morning)
            pic = discord.File(".//pic//fantasic.png")
            await msg.channel.send(f"{random_mes}")
            await msg.channel.send(file=pic)
        
        elif msg.content == '硬啦' and msg.author != self.bot.user:  # 硬LA
            pic = discord.File(".//pic//yinla.png")
            await msg.channel.send("硬啦!!!")
            await msg.channel.send(file=pic)        

        else:
            pass


def setup(bot):
    bot.add_cog(message(bot))
