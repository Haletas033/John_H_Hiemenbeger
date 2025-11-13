import requests
from bot import bot

@bot.command()
async def dog(ctx):
    await ctx.send(requests.get("https://random.dog/woof.json").json()["url"])

@bot.command()
async def cat(ctx, *, args: str = ""):
    basic = ""
    advanced = ""

    #Check for basic and advanced
    for pair in args.split():
        if ":" in pair:
            key, value = pair.split(":", 1)
            key = key.lower()
            if key == "basic":
                basic = value
            elif key == "advanced":
                advanced = value

    await ctx.send(requests.get(f"https://cataas.com/cat{basic}?{advanced}json=true").json()["url"])