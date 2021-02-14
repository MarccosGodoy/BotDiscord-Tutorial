import discord
import random

client = discord.Client()


insulto = ["bondiola", "HELADERA", "tucumano",
           "musulman", "teton", "trolo", "hater", "de mierda", "tumba ollas"]


def INSULTOIDE():
    global insulto
    return "Godo " + insulto[random.randint(-1, 8)]


@client.event
async def on_message(message):
    if message.content.find("!insulto") != -1:
        await message.channel.send(INSULTOIDE())
    if message.content.find("!twitch") != -1:
        await message.channel.send("twitch.tv/marccos_")

client.run('Aca va tu token')
