import discord  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio
import json
import random

with open("./admin.json") as f:
    permission = json.load(f)


class message(Cog_Extension):
    """訊息清理"""

    @commands.command()  #清理訊息
    async def clear(self, ctx, num: int):
        user_id = ctx.message.author.id
        if str(user_id) in permission["admin"]:  #有權限
            await ctx.channel.purge(limit=num + 1)
            await ctx.send("訊息清除完畢!此訊息將會在三秒後清除......")
            await asyncio.sleep(3)
            await ctx.channel.purge(limit=1)
        else:  #沒權限
            pass


def setup(bot):
    bot.add_cog(message(bot))
