import discord,random
from discord.ext import commands
from core.classes import Cog_Extension
from core.datahook import Mongodb,get_time

class chatmonitor(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        chat_data = {
            "_id":get_time(choose='sql'),
            "mid":msg.id,
            "duserid":msg.author.id,
            "duser":f"{msg.author.name}({msg.author.display_name})",
            "dcontent":msg.content,
            "utf8-time":get_time(choose='default')
        }
        p = Mongodb(msg.guild.name, msg.channel.name, chat_data)
        p.connect()
        p.insert()
    
    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        chat_data = {
            "_id":get_time(choose='sql'),
            "mid":msg.id,
            "duserid":msg.author.id,
            "duser":f"{msg.author.name}({msg.author.display_name})",
            "dcontent":"Message has deleted.",
            "utf8-time":get_time(choose='default')
        }
        p = Mongodb(msg.guild.name, msg.channel.name, chat_data)
        p.connect()
        p.insert()

    @commands.Cog.listener()
    async def on_message_edit(self,after:discord.Message,msg):
        chat_data = {
            "_id":get_time(choose='sql'),
            "mid":msg.id,
            "duserid":msg.author.id,
            "duser":f"{msg.author.name}({msg.author.display_name})",
            "dcontent":f"{after.content}(Edited)",
            "utf8-time":get_time(choose='default')
        }
        p = Mongodb(msg.guild.name, msg.channel.name, chat_data)
        p.connect()
        p.insert()
        
def setup(monbot):
    monbot.add_cog(chatmonitor(monbot))