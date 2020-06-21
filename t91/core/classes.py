import discord
from discord.ext import commands
from core.datahook import yamlhook
from discord.ext.commands import check

# --------------------
#
# Cog 核心
# --------------------

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

def permissioncheck():
    def predicate(ctx):
        try:
            ydata = yamlhook("config.yaml").load()
            if ctx.author.id not in ydata['bot']['owner']:
                return False
            else:
                return True
        except TypeError:
            raise TypeError('Sorry but I can`t find anyone in list.')
        except FileNotFoundError:
            raise FileNotFoundError('Sorry but I can`t find the config file.')
        
    return check(predicate)