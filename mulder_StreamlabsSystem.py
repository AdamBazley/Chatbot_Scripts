ScriptName = "Mulder"
Website = "https://sparabel.com/arena/"
Description = ""
Creator = "SparahawkNZ"
Version = "1.0.0"
Command = "!mulder"


def Init():
    return


def Execute(data):
    log("Entered Execute")
    if data.GetParam(0) != Command:
        return

    userName = data.UserName

    if is_alien():
        sendMessage("I knew it! So you are an alien after all, " + userName + "!")
    else:
        sendMessage("Alright, " + userName + ", you're no alien, I suppose.....")

    log("Exiting Execute")
    return


def Tick():
    return


def is_alien():
    log("Entered Is Alien")
    alienProbabilty = 10
    randomChance = Parent.GetRandom(0,100)
    log("Random Chance: "+ str(randomChance))
    log("Exiting Is Alien")
    return randomChance <= alienProbabilty

def sendMessage(message):
    log("Entering Send Message")
    Parent.SendStreamMessage(message)
    log("Exiting Send Message")
    return

def log(message):
    
    Parent.Log(Command, message)
    return

