import discord,random,json
from discord.ext import commands
from core.classes import Cog_Extension
from core.datahook import datahook

morning = ["早安","早"]

class tricks(Cog_Extension):

    @commands.command()
    async def dl(self,ctx):
        '''神社抽籤'''
        f1 = datahook("sign.json").open()
        sign = random.choice(f1[f'draw_lots'])
        await ctx.send(sign)

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in morning and msg.author != self.bot.user:
            await msg.channel.send("早")

def setup(bot):
    bot.add_cog(tricks(bot))