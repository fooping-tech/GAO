# This example requires the 'message_content' intent.

import discord 
import serial
import os
import config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#When on_ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


#When message recieved
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('トヨタファースト'):
        m = message.author.name + "さん、それDAOっぽくないギャオ！"
        await message.channel.send(m)
        ser =  serial.Serial('/dev/cu.usbserial-0D5A601EF3',115200,timeout=1)
        print(ser.name)
        print("send data")
        ser.write(bytes('4','utf-8'))#send robot move command
        ser.close()

    if message.content.startswith('トヨタウェイ'):
        m = message.author.name + "さん、これを思い出すんだギャオ！"
        path = os.getcwd() #get current path
        filepath = path + '/img/toyotaway.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
        ser =  serial.Serial('/dev/cu.usbserial-0D5A601EF3',115200,timeout=1)
        print(ser.name)
        print("send data")
        ser.write(bytes('1','utf-8'))#send robot move command
        ser.close()
    if message.content.startswith('ミッション'):
        m = message.author.name + "さん、これを思い出すんだギャオ！"
        path = os.getcwd()
        filepath = path + '/img/toyotamission.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
    if message.content.startswith('ヴィジョン'):
        m = message.author.name + "さん、これを思い出すんだギャオ！"
        path = os.getcwd()
        filepath = path + '/img/toyotavision.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
    if message.content.startswith('toyotaway'):
        m = message.author.name + " san,check it out ...grrrr!"
        path = os.getcwd()
        filepath = path + '/img/toyotaway_e.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
        ser =  serial.Serial('/dev/cu.usbserial-0D5A601EF3',115200,timeout=1)
        print(ser.name)
        print("send data")
        ser.write(bytes('1','utf-8'))#send robot move command
        ser.close()
    if message.content.startswith('mission'):
        m = message.author.name + " san,check it out ...grrrr!"
        path = os.getcwd()
        filepath = path + '/img/toyotamission_e.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
    if message.content.startswith('vision'):
        m = message.author.name + " san,check it out ...grrrr!"
        path = os.getcwd()
        filepath = path + '/img/toyotavision_e.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)
    if '悩' in message.content:
        m = message.author.name + "さん、悩んだ時にはこれを思い出すんだギャオ！"
        path = os.getcwd()
        filepath = path + '/img/toyotamission.jpeg'
        await message.channel.send(file=discord.File(filepath))
        await message.channel.send(m)

client.run(config.DISCORD_TOKEN)
