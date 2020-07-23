import os
from dotenv import load_dotenv
from discord.ext import commands
import hashlib
import base64

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
            f'Hello, {member.name}. Welcome to the FITSEC discord server. FITSEC is stands for FITSEC Information Technology Security. FITSEC is a student-led cybersecurity organization at Florida Institute of Technology. For more information on FITSEC visit https://www.fitsec.org.'
    )

@bot.command(name="bof", help="Have FITSEC Bot fuzz discord for a buffer overflow!")
async def bof(context):
    await context.send("A"*1000)

@bot.command(name="md5sum", help="Provide md5 hash of the value provided. i.e. !md5sum <value>")
async def md5sum(context, value=None):
    if value:
        result = hashlib.md5(value.encode('utf-8'))
        await context.send(f"Md5 hash of {value} is {result.hexdigest()}")
    else:
        await context.send("Please provide a value to be hashed. i.e. !md5sum <value>")

@bot.command(name="b64encode", help="Base64 encode the value provided. i.e. !b64encode <value>")
async def b64encode(context, value=None):
    if value:
        result = base64.b64encode(value.encode('utf-8'))
        await context.send(f'Base64 encoded result of {value} is {str(result, "utf-8")}')
    else:
        await context.send("Please provide a value to be encoded. i.e. !b64encode <value>")

@bot.command(name="b64decode", help="Base64 decode the value provided. i.e. !b64decode <value>")
async def b64decode(context, value=None):
    if value:
        result = base64.b64decode(value)
        await context.send(f'Base64 decoded result of {value} is {str(result, "utf-8")}')
    else:
        await context.send("Please provide a value to be decoded. i.e. !b64decode <value>")

bot.run(TOKEN)
