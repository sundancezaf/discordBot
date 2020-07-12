import os
from discord.ext import commands
from UltimatePandasCovid import *


os.system('python UltimatePandasCovid.py')

client = commands.Bot(command_prefix = '.')

# first event just gets bot online
# always need to have '@client.event' to start an event
@client.event
async def on_ready():
	print('Bot is ready')

# When the command needs an argument, the function will require a "ctx" parameter before
# the actual needed argument
@client.command(aliases=['firstCase, firstEvent'])
async def firstEvent(ctx, arg1):
	arg1 = str(arg1)
	answer = getFirstEvent(arg1)
	await ctx.send(answer)

@client.command(aliases=['totalUS','totalForUS','USATotal','UStotal','USTotal'])
async def totalCases(ctx):
	answer = totalCasesUS()
	# f string format,
	new = (f"{answer:,d}")
	await ctx.send(new)

@client.command(aliases=['previousDays','lastCoupleDays'])
async def pastCases(ctx, arg1,arg2):
	arg2 = int(arg2)
	answer = lastCoupleDays(arg1,arg2)
	answer = (f"{answer:,d}")
	await ctx.send(answer)

@client.command(aliases=['totalState','stateCases'])
async def stateTotal(ctx,state):
	answer = totalCasesState(state)
	answer = (f"{answer:,d}")
	await ctx.send(answer)

client.run(tokenHere)
