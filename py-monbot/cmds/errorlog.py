import discord,os  # 導入discord
from discord.ext import commands
from core.classes import Cog_Extension

class log(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.CommandNotFound): # 找不到commands
            await ctx.send(":mango: 啊遮勒User在公殺。") 
        elif isinstance(error,commands.MissingPermissions): # 權限不允許
            await ctx.send(":mango: 沒權限給偶閉嘴！歐巴馬～")
        elif isinstance(error,commands.MissingRequiredArgument): # 缺少需要的引數
            await ctx.send(":mango: 啊斗謀敏家啊謀敏家謀敏家！")
        elif isinstance(error,commands.NotOwner):
            await ctx.send(":mango: 我才不給逆用雷~ㄟ")
        else: # 其他未知錯誤
            await ctx.send(":mango: 啊斗跨謀啊跨謀跨謀！")
        # print to console
        print(f"(MON) \033[91m{ctx.author.name}({ctx.author.id})\033[0m",error)


def setup(monbot):
    monbot.add_cog(log(monbot))    