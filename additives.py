def surround(message: str, encasing: str):
    message = f"{encasing}{message}{encasing}"
    return message

def forAdditive(message: str, recipient):
    message = f"{recipient} {message}"
    return message

def handleSurroundAdditives(key: str, message: str):
    if key == "spoiler":
        message = surround(message, "||")
    elif key == "bold":
        message = surround(message, "**")
    elif key == "italic":
        message = surround(message, "*")
    elif key == "code":
        message = surround(message, "```")
    return message

def handleAdditives(additives, message: str):
    for pair in additives.split():
        if ":" in pair:
            key, value = pair.split(":", 1)
            key = key.lower()


            if key == "for":
                message = forAdditive(message, value)
            message = handleSurroundAdditives(key, message)

    return message


