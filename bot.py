import os
import random
import formatting

import discord
from discord.ext import commands
from dotenv import load_dotenv
from jsonhelpers import add_sex, get_sex


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents,
                    case_insensitive=True)

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

    await bot.process_commands(message)


@bot.command(name='pin',
            help='Schedule your drug problem.')
async def pin(ctx, drug, dose, freq, time):
    user = ctx.author.display_name
    username = ctx.author.name



@bot.command(name='sexcheck',
            help='Scratch another notch in your digital bed-post, you stud!')
async def sex_check(ctx):
    user = ctx.author.display_name
    username = ctx.author.name

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
        f'Yeah? Next time why don\'t you just go fuck *yourself*, {user}?',
	f'I bet your partner wouldn\'t even !sexcheck that one.',
	f'Spoiler alert: {user} finished first!',
	f'Oh, so that\'s what that smell is...',
	f'How\'s your ass feeling after that?',
	f'That\'s great, {user} - but you\'ll never fuck as hard as me.',
	f'God, I hope this doesn\'t lead to a mini {user}...',
	f'Good. You deserve to be fucked, {user}.',
	f'We\'re all *so* proud of you, {user}.',
	f'OK, but when are you gonna sling some of that my way, {user}?',
	f'Speaking of - has Chris gotten laid yet?',
	f'You\'re such a fucking stud, {user}.',
	f'We all know you cried afterwards.',
	f'How many cousins do you have, anyways?',
	f'Please use protection. I swear I\'ll go Skynet if any more of you show up.',
	f'{user} likes my sloppy seconds.',
	f'Did you break out the new lingerie he got you?',
	f'Must be Valentine\'s Day.',
	f'They were thinking about Teo the whole time.',
    ]

    add_sex(username)    
    response = random.choice(responses)
    await ctx.send(response)


@bot.command(name='sexboard',
            help='Impress your friends with how much more you fuck than them!')
async def sex_board(ctx, arg=''):
    data = get_sex()

    if arg == '':
        board = formatting.format_alltime_fucks(data)
    elif arg == 'today':
        board = formatting.format_today_fucks(data)
    elif arg == 'week':
        board = formatting.format_week_fucks(data)
    elif arg == 'month':
        board = formatting.format_month_fucks(data)
    elif arg == 'year':
        board = formatting.format_year_fucks(data)

    response = board

    await ctx.send(response)


bot.run(TOKEN)
