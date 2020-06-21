import discord
from discord.ext import commands
from core.datahook import yamlhook
import os

bot = commands.Bot(command_prefix="t..")
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Protect your Group."))
    print("[T91] T91 Chan is on! - Protect your Group.")

@bot.command()
async def help(ctx):
    anbhelp = discord.Embed()
    anbhelp.add_field(name="`blist`",value="顯示黑名單",inline=True)
    anbhelp.add_field(name="`bladd <對方id>`",value="增加對方至黑名單",inline=True)
    anbhelp.add_field(name="`blre <對方id>`",value="將對方從黑名單移除",inline=True)
    anbhelp.add_field(name="`cpccheck`",value="檢查自訂權限",inline=True)
    anbhelp.add_field(name="`cpcadd <對方id>`",value="增加對方至自訂權限名單",inline=True)
    anbhelp.add_field(name="`cpcre <對方id>`",value="將對方從自訂權限名單移除",inline=True)\

    anbhelp.set_footer(text="my prefix is t91. !")
    await ctx.send(embed=anbhelp)

# 裝載Cog
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    # console 訊息清除 
    # windows        : os.system("cls")
    # linux or other : os.system("clear")
    os.system("clear")
    # 抓取 bot token
    ydata = yamlhook("config.yaml").load()
    bot.run(ydata['bot']['token'])