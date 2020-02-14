import discord
from discord.ext.commands import CommandNotFound
from discord.ext import commands
import os
import json

with open("./admin.json") as f:
    permission = json.load(f)

bot = commands.Bot(command_prefix='c>')  #指令偵測
bot_m = "[BH]"
bot.remove_command('help')  #刪除help


@bot.event  #開機
async def on_ready():
    os.system('clear')
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("清除訊息：c>clear"))  #bot狀態
    print(bot_m, "booting successful.")
    botuser = bot.user.name
    botid = bot.user.id
    print(bot_m, f"bot login as {botuser}({botid})\n------------------")


"""模組控制"""

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')


@bot.command()
async def reload(ctx, extension):  #重裝模組
    user_id = ctx.message.author.id
    if str(user_id) in permission["admin"]:  #有權限
        bot.reload_extension(f'cmds.{extension}')
        print(bot_m, f"<{extension}> reload complete!")
        await ctx.send(f">>> 模組 {extension} 已重裝。")
    else:  #沒權限
        pass

if __name__ == "__main__":
    bot.run(f"",bot=True,reconnect=True)
