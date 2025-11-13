lastCommands = {}

def addLastCommand(ctx):
    lastCommands[ctx.author.id] = ctx.message.content