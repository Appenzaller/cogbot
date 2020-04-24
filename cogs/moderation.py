import discord
from discord.ext import commands
#from Botmain import usercheck
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="staff",
    passwd="Borealis",
    database="bot",
)
cursor = db.cursor()
print(db)


def usercheck(member: discord.Member):
    query = ("SELECT COUNT(*) FROM users WHERE user_id = %s")
    cursor.execute(query, (member.id,))
    user_count = cursor.fetchone()
    print(user_count)
    if user_count == 1:
        return
    elif user_count > 1:
        print("what the fuck")
    else:
        query = ("INSERT INTO users VALUES ('%s', '%s', '%s')")
        cursor.execute(query, (member.id, member.joined_at, member.created_at))

class modCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command(name = 'warn', hidden = True, )
    @commands.guild_only()
    @commands.has_any_role('admins', 'moderators')
    async def warn(self,ctx,member: discord.Member,reason: str):
        if not reason:
            await ctx.send('Please provide a reason.')
            return
        else:
            #await usercheck(member)
            await member.send('**You have been warned for the following: **\n' + '*' + reason + '*' + '\n\n **-Project Borealis staff**')
            await ctx.send(str(member) + ' has been warned for: *' + reason + '*')

    @commands.command(name = 'ban', hidden = True)
    @commands.guild_only()
    @commands.has_any_role('admins', 'moderators')
    async def ban(self,ctx,user: discord.Member,reason: str):
        if not reason:
            await ctx.send('Please provide a reason.')
            return
        else:
            await user.ban()
            await ctx.send(str(user) + ' has been banned for: *' + reason + '*')





def setup(bot):
    bot.add_cog(modCog(bot))