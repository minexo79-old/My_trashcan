import discord
from discord.ext import commands
from core.classes import Cog_Extension

# --------------------
# 
# 錯誤處理器
# --------------------

async def error_process(ctx,error,process="default"):
    await ctx.channel.purge(limit=1)
    member = ctx.author.name
    # 印出至console
    print(f"E>> {error}")
    embed=discord.Embed(color=0xff0000)
    # 聊天室顯示
    if process == "custom": # 自訂錯誤處理
        embed.add_field(name="使用者",value=member,inline=False)
        embed.add_field(name="錯誤訊息",value=f"**{error}**",inline=False)
        embed.set_footer(text="👾")
        await ctx.send(embed=embed)

    else: # 一般錯誤處理
        embed=discord.Embed()
        embed.add_field(name="使用者",value=member,inline=False)
        embed.add_field(name="錯誤訊息",value=f"**{error}**",inline=False)
        embed.set_footer(text="👾")
        await ctx.send(embed=embed)