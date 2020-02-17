import discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>') #指令偵測
bot.remove_command('help') #刪除help
bot_m = "[VM]"

@bot.event #開機
async def on_ready():
    os.system('clear')
    print(bot_m,"booting successful.")

@bot.event #錯誤的指令
async def on_command_error(ctx,error):
    if isinstance(error,CommandNotFound) and ctx.author != bot.user:
        await ctx.send("嗯?我看不懂啊......")

"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def reload(ctx,extension): #重裝模組
    bot.reload_extension(f'cmds.{extension}')
    print(bot_m,f"<{extension}> reload complete.")
    await ctx.send(f">>> 模組 {extension} 已重裝。")

if __name__ == "__main__":
    bot.run(f"",bot=True,reconnect=True)