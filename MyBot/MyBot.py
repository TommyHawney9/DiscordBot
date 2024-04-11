import os
from itertools import cycle
import discord
from discord.ext import commands, tasks


myBot = commands.Bot(command_prefix='-')
status = cycle(['-help for commands', helperBot, ])


@myBot.event
async def on_ready():
    change_status.start()
    print('Bot is online')


@myBot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f'Welcome to the server {member.mention}')


@tasks.loop(seconds=10)
async def change_status():
    await myBot.change_presence(activity=discord.Game(next(status)))


@myBot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command! Use /help for command list')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do this")


@myBot.command()
async def more(self, ctx):
    channel = ctx.message.channel

    embed = discord.MessageEmbed()
    embed.setColor('#31D3FB')
    embed.setTitle('More help')
    embed.setDescription('List of commands')
    embed.addFields(
        {name: '/cv c', value: 'Corona virus cases'}
    )

    embed.add_field(name='/ping', value='', inline=False)

    await myBot.send(channel, embed=embed)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        myBot.load_extension(f'cogs.{filename[:-3]}')

myBot.run('ENTER_BOT_TOKEN_HERE')
