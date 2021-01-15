import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from jsonhelpers import add_sex, get_sex
from formatting import format_fucks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if '69' in message.content:
        await message.channel.send('Nice.')
    elif 'Will' in message.content:
        willmoji = bot.get_emoji(799082055139852338)
        await message.add_reaction(willmoji)
    elif 'dick' in (message.content).lower():
        woodmoji = bot.get_emoji(799274321163845683)
        await message.add_reaction(woodmoji)


@bot.command(name='sexcheck',
            help='Scratch another notch in your digital bed-post, you stud!')
async def sex_check(ctx):
    user = ctx.author.name

    responses = [
        f'Congratulations on the sex, {user}!',
        f'Wow, check out the big dick on {user}!',
        f'You sure do know how to sling some genitals, {user}.',
        f'There goes {user}, fucking again.',
        f'Wow! Someone actually fucked {user}?',
        f'Honestly, I can\'t believe {user} gets fucked.',
        f'Way to go, {user}. You do that sex. You do it good.',
        f'Cool story, {user}. We get it. You fuck.',
        f'I bet {user} had to pay for it.',
        f'Yeah? Next time why don\'t you just go fuck *yourself*, {user}?'
    ]

    add_sex(user)    
    response = random.choice(responses)
    await ctx.send(response)


@bot.command(name='sexboard',
            help='Impress your friends with how much more you fuck than them!')
async def sex_board(ctx):
    data = get_sex()
    board = format_fucks(data)
    response = board

    await ctx.send(response)


bot.run(TOKEN)