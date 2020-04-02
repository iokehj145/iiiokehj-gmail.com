import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix = '!')
ban_mesg = ['Head CG', 'head CG', 'head cg', 'Head cg', 'head civil guard']

@Bot.event
async def on_ready():
  print("Bot online")
 
@Bot.command( pass_context = True)
@commands.has_permissions( administrator = True )   #!Clear
async def clear(ctx):
  await ctx.channel.purge()
 
@Bot.command( pass_context = True)
async def verify( ctx, member: discord.Member ):

 cg_en = discord.utils.get(ctx.message.guild.roles, name = 'Enlistment CG')
 await member.add_roles(cg_en)
 await ctx.send(f'{member.mention} become Enlistment CG!')
 
@Bot.command( pass_context = True)
@commands.has_permissions( administrator = True )
async def ban(ctx, member: discord.Member, *, reason = None):  #!Ban
 await ctx.channel.purge( limit = 1 )
 await member.ban( reason = reason )
 await ctx.send(f'ban user {member.mention}')
Bot.run('Njg1NzI4Njk3NDk1NDUzNjk4.XmnPlQ.t9uoSe2VHGRQ8ZjZ71hSlqqZkV4')