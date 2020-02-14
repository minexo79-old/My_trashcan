import discord,os
from discord.ext import commands
from core.datahook import datahook

bot = commands.Bot(command_prefix="h>")

@bot.event
async def on_ready():
    os.system('cls')
    print(f"| Using {bot.user.name} login.")
    print("| Bot OK!")
    await bot.change_presence(activity=discord.Game(name="我是客家人"))

#模組控制
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    f1 = datahook("hconfig.json").open()
    bot.run(f1['token'],bot=True,reconnect=True)