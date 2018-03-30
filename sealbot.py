import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
bot = commands.Bot(command_prefix='seal.')
bot.remove_command("help")
print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_status(game=discord.Game(name='seal.help'))

@bot.command(pass_context=True)
async def botinfo(ctx):
    await bot.say("This bot was created by @AjunPug. Enjoy!")

@bot.command(pass_context=True)
async def slap(ctx):
    await bot.say("*slap slap* oof")
    
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="PugBot Help", description="PugBot Commands", color=0x00ff00)
    embed.add_field(name="seal.slap", value="Slaps Seal Bot", inline=True)
    embed.add_field(name="seal.botinfo", value="Shows info about this bot", inline=True)
    embed.add_field(name="seal.help", value="Shows this", inline=True)
    await bot.say(embed=embed)
    
bot.run("NDI5MjY3NjU4MjM2NzU1OTY4.DZ_KLw.5gkcsSP21CLUL0sbjb0L7p3Z3X4")
