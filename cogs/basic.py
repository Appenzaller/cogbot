import discord
from discord.ext import commands


class basicCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot




    print('Basic cog loaded.')

    @commands.command(name='load', hidden = True)
    @commands.guild_only()
    @commands.has_role('admins')
    async def load(self,ctx,*,cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(str(cog) + " successfully loaded!")

    @commands.command(name='unload', hidden=True)
    @commands.guild_only()
    @commands.has_role('admins')
    async def unload(self,ctx,*,cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(str(cog) + " successfully unloaded!")

    @commands.command(name='reload', hidden=True)
    @commands.guild_only()
    @commands.has_role('admins')
    async def reload(self,ctx,*,cog: str):
        try:
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send(str(cog) + " successfully reloaded!")

def setup(bot):
    bot.add_cog(basicCog(bot))

