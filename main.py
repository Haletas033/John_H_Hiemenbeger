from bot import bot, TOKEN
import image
import text

@bot.event
async def on_ready():
    print(f"{bot.user} is awake")

bot.run(TOKEN)
