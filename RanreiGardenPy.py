import discord
client = discord.client()

@client.event
async def on_ready():
    print(f"{client.user}がオンラインになりました")

client.run("Token")
