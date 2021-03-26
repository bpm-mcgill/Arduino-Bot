import discord, random, serial, time
from discord.ext import commands, tasks
client = commands.Bot(command_prefix="$")
ledstate = False
#serport = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)
serport = serial.Serial("PUT YOUR ARDUINO PATH HERE", baudrate=9600, timeout=1)

@client.event
async def on_ready():
    print("Bot Prepared!")

@client.command()
async def toggleled(ctx):
    global ledstate
    ledstate = not ledstate
    if ledstate:
        serport.write(b'o')
        await ctx.send("Turned led on")
    else:
        serport.write(b'f')
        await ctx.send("Turned led off")

# EXTRA CODE FOR BUZZER (Ignore if you aren't going to add a buzzer)

@client.command(aliases=["annoyBPM","pingbpm","annoybpm"])
async def pingBPM(ctx):
    serport.write(b'q')
    await ctx.send("Pinging BPM")

# Run client ------------------------------------------------------------------- #
client.run("BOT TOKEN")
