import discord
client = discord.client()

@client.event
async def on_ready():
    print(f"{client}がオンラインになりました")

client.run("Token")
