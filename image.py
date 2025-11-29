from io import BytesIO

import aiohttp
import discord
import requests
import users
from additives import handleAdditives
from bot import bot
from PIL import Image, ImageDraw
from math import sin, cos, pi
@bot.command()
async def dog(ctx, *, args: str = ""):
    url = "https://random.dog/woof.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            await ctx.send(handleAdditives(args, data.get("url")))

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

    url = f"https://cataas.com/cat{basic}?{advanced}json=true"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            await ctx.send(handleAdditives(args, data.get("url")))

@bot.command()
async def inspire(ctx, args: str = ""):
    url = "https://inspirobot.me/api?generate=true"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            inspiration = await response.text()
            await ctx.send(handleAdditives(args, inspiration))

@bot.command()
async def completeGraph(ctx, *, args: str = ""):

    #options for true and false
    truthy = {"1", "true", "yes", "on"}
    falsy = {"0", "false", "no", "off"}

    k = 6
    width = 1
    size = 5000
    colour = "white"

    await ctx.send("Command received. Note: large graphs may take a while to complete or fail to complete.")

    #Handle args
    for pair in args.split():
        if ":" in pair:
            key, value = pair.split(":", 1)
            key = key.lower()
            if key == "nodes":
                k = int(value)
            elif key == "width":
                width = int(value)
            elif key == "transparent":
                colour = (0,0,0,0) if value.lower() in truthy else "white"
            elif key == "size":
                size = int(value)


    img = Image.new("RGBA", (size, size), colour)
    draw = ImageDraw.Draw(img)

    nodes = []

    for i in range(k):
        radian = (360 / k) * (pi / 180)
        nodes.append((cos(radian * i) * size//2 + size//2, sin(radian * i) * size//2 + size//2))

    for x in range(k):
        for y in range(x+1, k):
            draw.line([nodes[x], nodes[y]], fill="black", width=width)

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    try:
        await ctx.send(file=discord.File(buffer, filename="completeGraph.png"))

    except discord.errors.HTTPException as e:
        if e.code == 40005:
            await ctx.send("Graph failed due to 8mb image limit set by discord.")



