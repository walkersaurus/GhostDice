# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import drew_dbot
import re

TOKEN = 'NDc3MzIwODY1OTIzNzI3Mzcz.Dk6k1A.HdpX4joH5qrtLu-O7AgcBwfaQbQ'

client = discord.Client()

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.startswith('/roll'):
		try:
			qty = int(message.content.split()[1])
			if qty < 666:
				msg = 'Rolling ' + str(qty) + ' dice...You got ' + GhostyMcGhostface(qty)
			else:
				msg = 'That\'s too many dice. I only have 111 arms. Yeah that\'s fifty times more than you have (assuming you have two), but even robots have their limitations.'
		except:
			msg = "Roll what? That's not even a number."
		finally:
			await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
