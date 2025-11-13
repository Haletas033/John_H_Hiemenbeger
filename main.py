import users
from bot import bot, TOKEN
import webserver
import utilities
import image
import text

lastMessages = {}

@bot.event
async def on_ready():
    print(f"{bot.user} is awake")

#Save command content as users last message
@bot.listen("on_command")
async def onCommand(ctx):
    if ctx.author.bot:
        return
    users.addLastCommand(ctx)

webserver.keepalive()
bot.run(TOKEN)
