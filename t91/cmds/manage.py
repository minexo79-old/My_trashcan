import discord
from discord.ext import commands
from core.classes import Cog_Extension,permissioncheck
from core.datahook import yamlhook
from core.errors import error_process

class manage(Cog_Extension):

    @commands.command()
    @permissioncheck()
    async def cpccheck(self,ctx):
        '''檢查自訂權限'''
        await ctx.send("> ✅恭喜！你已在自訂權限名單內。")

    @commands.command()
    @permissioncheck()
    async def cpcadd(self,ctx,member:discord.Member):
        '''增加自訂權限者'''
        ydata = yamlhook("config.yaml").load()
        if ctx.author.id in ydata['bot']['owner']: # 檢查一次，防止有兩個同樣的ID存在
            did = member.id
            yamlhook("config.yaml").owner(did,process="append")
            # 輸出增加成功
            await ctx.send(f"> ✅自訂權限者`{member.display_name}`已增加！")
        else:
            error = "對方已在自訂權限名單內。"
            await error_process(self,ctx,error,process="custom")

    @commands.command()
    @permissioncheck()
    async def cpcre(self,ctx,member:discord.Member):
        '''移除自訂權限者'''
        ydata = yamlhook("config.yaml").load()
        try:
            if ctx.author.id in ydata['bot']['owner']:
                did = member.id
                yamlhook("config.yaml").owner(did,process="remove")
                # 輸出移除成功
                await ctx.send(f"> ✅自訂權限者`{member.display_name}`已移除！")
        except ValueError:
            error = "找不到對方資料。"
            await error_process(self,ctx,error,process="custom")         

def setup(bot):
    bot.add_cog(manage(bot))
