import users
from bot import bot

@bot.command()
async def again(ctx):
    last = users.lastCommands.get(ctx.author.id)

    if not last:
        return await ctx.send("No previous commands")

    lastCommand = ctx.message
    lastCommand.content = last

    await bot.process_commands(lastCommand)
    return None