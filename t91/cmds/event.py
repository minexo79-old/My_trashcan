import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.errors import error_process
from core.datahook import yamlhook

class event(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            # 傳送至錯誤處理器
            await error_process(ctx,error,process="default")
            # 一般方式處理： process = "default"
            # 自訂方式處理： process = "custom"
            
        except AttributeError:
            pass

def setup(bot):
    bot.add_cog(event(bot))