import discord
import responses


async def send_message(message, user_message, isPrivate):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA3MjYyMjc4NTY3Mjc5MDEyNw.GqCN6o.o7yyoc2p5qkqvh_2-KwfeliFFanDMZ7ywidoes'
    client = discord.Client(intents=discord.Intents.all())
    bot = discord.Client(command="gpt3", intents = discord.Intents.all())

    @client.event
    async def on_ready():
        print("ready")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        channel = str(message.channel)
        if message.attachments is not None:
            for attachment in message.attachments:
                await attachment.save(attachment.filename)
                with open(attachment.filename, 'r') as file:
                    content = file.read()
                    await message.channel.send(content)
                filename = message.content.split()[1]
                with open(filename, 'r') as file:
                    user_message = file.read()
                    await send_message(message, user_message, False)
        else:
            user_message = str(message.content)
            if user_message[0] == '?':
                user_message = user_message[1:]
                if user_message[0] == '?':
                    user_message = user_message[1:]
                    await send_message(message, user_message, True)
                else: await send_message(message, user_message, False)

    client.run(TOKEN)
