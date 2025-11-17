import asyncio
import random

import aiohttp
import requests
from flask import ctx

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

@bot.command()
async def slot(ctx, money: int = 100):
    options = ['7️⃣', '🔔', '🍒', '🍇', '🍋']
    await ctx.send(f"Spinning with ${money}...")
    await asyncio.sleep(1)

    roll = [random.choice(options) for i in range(3)]
    await ctx.send("".join(roll))

    if roll[0] == roll[1] and roll[1] == roll[2]:
        money *= 10
    elif roll[0] == roll[1] or roll[1] == roll[2] or roll[0] == roll[2]:
        money *= 2
    else:
        money //= 2

    await ctx.send(f"You now have ${money}!")

@bot.command()
async def dadJoke(ctx):
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            await ctx.send(data.get("joke"))
