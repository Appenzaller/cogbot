import discord
from discord.ext import commands
import sys, traceback
import asyncio
import datetime
import os
import mysql.connector

#Connects to the DB
"""
db = mysql.connector.connect(
    host="localhost",
    user="staff",
    passwd="Borealis",
    database="bot",
)
cursor = db.cursor()
print(db)
"""
"""
async def usercheck(member: discord.Member):
    query = ("SELECT COUNT(*) FROM users WHERE user_id = %s")
    cursor.execute(query, (member.id,))
    user_count = cursor.fetchone()
    print(user_count)
    if user_count == 1:
        return
    elif user_count >1:
        print("what the fuck")
    else:
        query = ("INSERT INTO users VALUES ('%s', '%s', '%s')")
        cursor.execute(query, (member.id, member.joined_at, member.created_at))
"""




initial_extension = 'cogs.basic'

prefix = '!'
bot = commands.Bot(command_prefix=prefix)

bot.load_extension(initial_extension)
print('Loading default cogs')




@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='PLEASE FUCKING WORK'))
    print('Logged in as ' + bot.user.name)
    print('Connected to the following servers:')
    for guild in bot.guilds:
        print(guild.name)
    print('----')
    debug_channel = bot.get_channel(695592888318296084)
    await debug_channel.send('Bot successfully launched')



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
       await ctx.send('You do not have the required permissions to execute this command!')



bot_token = 'bot_token'
with open(bot_token) as f:
    token = f.readline().strip()
bot.run(token, bot=True, reconnect=True)
