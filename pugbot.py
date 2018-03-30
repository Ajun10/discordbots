import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
bot = commands.Bot(command_prefix='pug.')
bot.remove_command("help")
print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_status(game=discord.Game(name='pug.help'))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def website(ctx):
    await bot.say("https://ajun10.github.io/pugbot/")

@bot.command(pass_context=True)
async def botinfo(ctx):
    await bot.say("This bot was created by @AjunPug. Enjoy!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="PugBot Help", description="PugBot Commands", color=0x00ff00)
    embed.add_field(name="pug.serverinfo", value="Shows things about the server", inline=True)
    embed.add_field(name="pug.website", value="Shows our website link", inline=True)
    embed.add_field(name="pug.info (username)", value="Shows info about a user on the server", inline=True)
    embed.add_field(name="pug.ping", value="Says pong!", inline=True)
    embed.add_field(name="pug.botinfo", value="Shows info about this bot", inline=True)
    embed.add_field(name="pug.help", value="Shows this", inline=True)
    await bot.say(embed=embed)
    
bot.run("NDI4NTQ4MjkxMDIyODE1MjMy.DZ0sQg.qqLSpxFFiCs967Vw-mZUk8zvrHE")
