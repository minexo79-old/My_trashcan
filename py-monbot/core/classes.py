import discord,os
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,monbot):
        self.monbot = monbot
