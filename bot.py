import discord
from bot_mantik import gen_pass
from bot_mantik import emoji_olusturucu
from bot_mantik import yazi_tura
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('Bye'):
        await message.channel.send("Bye!")
    elif message.content.startswith('.şifreoluşturucu'):
        await message.channel.send(gen_pass(20))
    elif message.content.startswith('.emojioluşturucu'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('.yazıtura'):
        await message.channel.send(yazi_tura())        
    else:
        await message.channel.send(message.content)

client.run("Token Giriniz")
