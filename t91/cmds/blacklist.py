import discord
from discord.ext import commands
from core.classes import Cog_Extension,permissioncheck
from core.datahook import yamlhook
from core.errors import error_process

class blacklist(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        # 被動Ban掉黑名單內的指定用戶
        ydata = yamlhook("config.yaml").load()
        if member.id in ydata['blacklist']:
            await member.kick(reason=None)
            print(f"[T91] Detected {member}! has been kicked!")

    @commands.command()
    @permissioncheck()
    async def blist(self,ctx):
        '''瀏覽黑名單'''
        ydata = yamlhook("config.yaml").load()
        blacklist = [bm for bm in ydata['blacklist']]
        await ctx.send(f"```md\n{blacklist}\n```")

    @commands.command()
    @permissioncheck()
    async def bladd(self,ctx,member:int):
        '''增加至黑名單 <對方id>'''
        ydata = yamlhook("config.yaml").load()
        if member not in ydata['blacklist']: # 檢查一次，防止有兩個同樣的ID存在        
            yamlhook("config.yaml").operate(member,db="blacklist",process="append")
            # 輸出增加成功
            await ctx.send(f"> > ✅`{member}`已增加到黑名單！")
        else:
            error = "已增加到黑名單。"
            await error_process(ctx,error,process="custom") 

    @commands.command()
    @permissioncheck()
    async def blre(self,ctx,member:int):
        '''從黑名單移除 <對方id>'''
        try:
            yamlhook("config.yaml").operate(member,db="blacklist",process="remove")
            # 輸出移除成功
            await ctx.send(f"> ✅`{member}`已從黑名單移除！")
        except ValueError: # 找不到ID
            error = "找不到對方資料。"
            await error_process(ctx,error,process="custom") 
def setup(bot):
    bot.add_cog(blacklist(bot))