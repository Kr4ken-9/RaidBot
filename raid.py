import discord
import asyncio
import argparse

client = discord.Client()
parser = argparse.ArgumentParser()
parser.add_argument('token', type=str, help='Token of the user to login as')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content == 'raid':
        await raid(message)

async def hubbub(message):
    mention = ""

    members = dict(message.server.members)
    for user in members:
        if user.bot:
            continue

        mention += user.mention + '\n'

        if len(mention) >= 1977:
            await client.send_message(message.channel, mention)
            mention = ""

    await client.send_message(message.channel, mention)

async def large(channel):
    await client.send_message(channel, '\u2800' + ('\n' * 1991) + '\u2800')

async def raid(message):
    while True:
        await hubbub(message)
        await asyncio.sleep(1)
        await large(message.channel)
        await asyncio.sleep(2)

client.run(parser.parse_args().token, bot=False)
