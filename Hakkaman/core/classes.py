import discord,json
from discord.ext import commands

class Cog_Extension(commands.Cog): # Cog
    def __init__(self,bot):
        self.bot = bot

class Color: # 自訂顏色
    embed_normal = 0x6b6b6b
    embed_error = 0xff0000
    embed_pass = 0x80ff00