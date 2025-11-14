import requests
from bot import bot

@bot.command()
async def repeat(ctx, message: str, times: int = 1):
    times = min(times, 10)
    for i in range(times):
        await ctx.send(message)

@bot.command()
async def quote(ctx):
    quoteData = requests.get("https://dummyjson.com/quotes/random")
    await ctx.send(f"{quoteData.json()["quote"]} - {quoteData.json()["author"]}")