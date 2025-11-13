import users
from bot import bot

@bot.command()
async def repeat(ctx, message: str, times: int = 1):
    times = min(times, 10)
    for i in range(times):
        await ctx.send(message)