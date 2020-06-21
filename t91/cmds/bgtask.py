import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio

class bgtask(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        async def countguild():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await self.bot.change_presence(activity=discord.Activity(name=f"[t.help] Protect {len(self.bot.guilds)} Groups",type=discord.ActivityType.watching)) # 計算有多少人
                await asyncio.sleep(10)

        self.count = self.bot.loop.create_task(countguild())

def setup(bot):
    bot.add_cog(bgtask(bot))
