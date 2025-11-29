import asyncio
import random

import aiohttp
import requests

from additives import handleAdditives
from bot import bot

@bot.command()
async def repeat(ctx, message: str, times: int = 1, *, args: str = ""):
    times = min(times, 10)
    for i in range(times):
        await ctx.send(handleAdditives(args, message))

@bot.command()
async def quote(ctx, *, args: str = ""):
    url = "https://dummyjson.com/quotes/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            quoteData = await response.json()
            message = f"{quoteData.get('quote')} - {quoteData.get('author')}"
            await ctx.send(handleAdditives(args, message))

@bot.command()
async def slot(ctx, money: int = 100, *, args: str = ""):
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

    await ctx.send(handleAdditives(args, f"You now have ${money}!"))

@bot.command()
async def dadJoke(ctx, *, args: str = ""):
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            await ctx.send(handleAdditives(args, data.get("joke")))

@bot.command()
async def russianRoulette(ctx, *, args: str = ""):
    if random.randint(1, 6) == 1:
        message = "*Bang!*"
    else:
        message = "*Click...*"

    await ctx.send(handleAdditives(args, message))

@bot.command()
async def rand(ctx, n: int = 10, *, args: str = ""):
    await ctx.send(handleAdditives(args, f"{random.randint(1, n)} was chosen!"))

@bot.command()
async def coinFlip(ctx, *, args: str = ""):
    side = "Heads!" if random.randint(1, 2) == 1 else "Tails!"
    await ctx.send(handleAdditives(args, side))

@bot.command()
async def decide(ctx, *, text: str = ""):
    if '|' in text:
        choices, args = [char.strip() for char in text.split('|', 1)]
    else:
        choices = text.strip()
        args = ""

    options = [choice.strip() for choice in choices.split(',')]
    await ctx.send(handleAdditives(args, random.choice(options)))
