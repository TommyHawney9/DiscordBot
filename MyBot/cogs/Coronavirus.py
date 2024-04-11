import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen


class Coronavirus(commands.Cog):

    def __init__(self, myBot):
        self.myBot = myBot

    @commands.command(aliases=['cv'])
    async def corona_virus(self, ctx, *, type):
        if type == 'd':
            await ctx.send(f'The number of covid deaths in the UK is: {death_count()}')
        elif type == 'r':
            await ctx.send(f'The recoveries from covid in the UK is: {recovered_count()}')
        else:
            await ctx.send(f'The number of cases in the UK is: {corona_count()}')


def corona_count():
    req = Request('https://www.worldometers.info/coronavirus/country/uk/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    for number in soup.find_all('div', {"class", "maincounter-number"}, limit=1):
        number = str(number.text)
    return number


def death_count():
    req = Request('https://www.worldometers.info/coronavirus/country/uk/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    for number in soup.find_all('div', {"class", "maincounter-number"}, limit=2):
        number = str(number.text)
    return number


def recovered_count():
    req = Request('https://www.worldometers.info/coronavirus/country/uk/', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = bs(webpage, 'html.parser')
    for number in soup.find_all('div', {"class", "maincounter-number"}, limit=3):
        number = str(number.text)
    return number



def setup(myBot):
    myBot.add_cog(Coronavirus(myBot))


