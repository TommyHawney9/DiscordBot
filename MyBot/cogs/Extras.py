import discord
from discord.ext import commands


class Extras(commands.Cog):

    def __init__(self, myBot):
        self.myBot = myBot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.myBot.latency * 1000)}ms')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount)


def setup(myBot):
    myBot.add_cog(Extras(myBot))
