from bot import bot, TOKEN
import webserver
import image
import text

@bot.event
async def on_ready():
    print(f"{bot.user} is awake")

webserver.keepalive()
bot.run(TOKEN)
