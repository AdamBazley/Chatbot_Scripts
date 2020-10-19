ScriptName = ""
Website = ""
Description = ""
Creator = ""
Version = ""

Command = "!bookvote"
FilePath = r"C:\Users\adamba\Documents\NextBook.txt"
def Init():
    return

def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    SaveToFile(data.GetParam(1).lower(), FilePath)
    send_message("Vote for "+ data.GetParam(1) + " saved <3")
    return

def Tick():
    return

def Log(message):
    Parent.Log(Command, message)
    return

def send_message(message):
    Parent.sendStreamMessage(message)
    return

def SaveToFile(text, filePath):
    f = open(filePath, "a")
    f.write(text)
    f.close()
    return

def WriteToFile(text, filePath):
    f = open(filePath, "w")
    f.write(text)
    f.close()
    return
    
