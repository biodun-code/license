import discord
from discord.ext import commands
import string
import secrets

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define a custom function for generating license keys with the "GEMLAB" prefix and hyphens
def generate_license_key():
    # You can customize the length and character set for your license keys
    key_length = 29
    characters = string.ascii_letters + string.digits
    random_part_length = key_length - len("GEMLAB-") - 4  # 4 hyphens
    random_part = ''.join(secrets.choice(characters) for _ in range(random_part_length))

    # Insert hyphens at the appropriate positions
    license_key = f"GEMLAB-{random_part[:5]}-{random_part[5:10]}-{random_part[10:15]}-{random_part[15:20]}"
    return license_key

@bot.command()
async def license(ctx):
    # Generate a license key using the custom function
    license_key = generate_license_key()

    # Send the license key as a reply in the same channel
    await ctx.send(f'Your license key: `{license_key}`')





bot.run('MTE1NzIwODYxNjcyMjUxODA2Ng.GBoA58.uU_Oz309XBW3FkhlGNvB0DBgbSv0cQ1OlEAGyo')


