import discord
import os
import responses


async def send_message(message, user_message, isPrivate):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = discord.Client(intents=discord.Intents.all())
    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        print("mensaje recibido de" + username)
        user_message = str(message.content)
        if user_message[0] == '?':
            user_message = user_message[1:]
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, True)
            else: await send_message(message, user_message, False)
  
    client.run(TOKEN)
