import discord,random
from discord.ext import commands
from core.classes import Cog_Extension

class tricks(Cog_Extension):

    @commands.command()
    async def pick(self,ctx,sign:str):
        '''自訂抽籤 <item1,item2,...>'''
        n = list(sign.split(","))
        result = random.choice(n)
        await ctx.send(f":mango: 我選：{result}")

def setup(monbot):
    monbot.add_cog(tricks(monbot))