import os
from discord.ext import commands
from UltimatePandasCovid import *

# Need to run the UltimatePandasCovid script first as it will need to create the DataFrames to pull data from
os.system('python UltimatePandasCovid.py')

client = commands.Bot(command_prefix='.')


# first event just gets bot online
# always need to have '@client.event' to start an event
@client.event
async def on_ready():
    print('Bot is ready')


# When the command needs an argument, the function will require a "ctx" argument before
# the actual argument needed
@client.command(aliases=['firstCase, firstEvent'])
async def firstEvent(ctx, arg1):
    arg1 = str(arg1)
    answer = getFirstEvent(arg1)
    await ctx.send(answer)


@client.command(aliases=['totalUS', 'totalForUS', 'USATotal', 'UStotal', 'USTotal'])
async def totalCases(ctx):
    answer = totalCasesUS()
    # f string format,
    new = (f"{answer:,d}")
    await ctx.send(new)


@client.command(aliases=['previousDays', 'lastCoupleDays'])
async def pastCases(ctx, arg1, arg2):
    days = int(arg2)
    answer = lastCoupleDays(arg1, days)
    answer = (f"{answer:,d}")
    await ctx.send(answer)


@client.command(aliases=['totalState', 'stateCases'])
async def stateTotal(ctx, state):
    answer = totalCasesState(state)
    answer = (f"{answer:,d}")
    await ctx.send(answer)


# This sends the user the following text as a DM. This is a help guide with all the commands.
@client.command()
async def commandList(ctx):

	await ctx.author.send("""```
Replace [state] with the name of the state. Replace [number] with a number. If it's a two word state, place in quotation marks. 
Ex: "South Dakota". 

Example of a command:  .pastCases "North Dakota" 3 



Commands are:
	.stateTotal [state]
	.firstEvent [state]
	.totalCases
	.pastCases [state] [number]


```""")


client.run('NzMxMDU0NDA4MDkxMDQxNzkz.XwmA-w.kt5R2Yyf6sfWWfwGOJifwdyIt5M')
