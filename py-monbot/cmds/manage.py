import discord
from discord.ext import commands
from core.classes import Cog_Extension

class manage(Cog_Extension):

    @commands.command()
    @commands.is_owner()
    async def bye(self,ctx):
        '''close the bot'''
        await ctx.send(":mango: 芒果！")
        await self.monbot.close()

    @commands.command()
    @commands.is_owner()
    async def re(self,ctx,extension):
        '''extension reload'''
        self.monbot.reload_extension(f"cmds.{extension}")
        print(f"(MON) {extension} has reloaded.")
        await ctx.send(f":mango: `{extension} 已重新載入。`")

def setup(monbot):
    monbot.add_cog(manage(monbot))