import discord,os
from discord.ext import commands
from core.datahook import Hook

monbot = commands.Bot(command_prefix="mon")
bot = Hook("mconfig.yaml").open()

@monbot.event
async def on_ready():
    await monbot.change_presence(activity=discord.Game(name="芒果!(Testing)"))
    print("----------------------")
    print("(MON) Monbot is ready.")

#模組載入
os.system('clear')
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        monbot.load_extension(f'cmds.{filename[:-3]}')
        print(f"(MON) Extension：{filename[:-3]} is loaded.")

if __name__ == "__main__":
    monbot.run(bot['bot']['token'])