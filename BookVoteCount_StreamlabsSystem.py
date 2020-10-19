ScriptName = ""
Website = ""
Description = ""
Creator = ""
Version = ""

Command = "!bookvotecount"
FilePath = r"C:\Users\adamba\Documents\NextBook.txt"
def Init():
    return

def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    message = Count(ReadFile)
    listToStr = ' '.join([str(elem) for elem in message])
    send_message(listToStr)

    return

def Tick():
    return

def Log(message):
    Parent.Log(Command, message)
    return

def send_message(message):
    Parent.sendStreamMessage(message)
    return

def SaveToFile(text):
    f = open(FilePath, "a")
    f.write(text)
    f.close()
    return

def WriteToFile(text):
    f = open(FilePath, "w")
    f.write(text)
    f.close()
    return

def ReadFile():
    f = open(FilePath, 'r+')
    lines = [line for line in f.readlines()]
    f.close()
    return lines

def Count(list):
    for x in list:
        counted = [x + ": " + list.count(x) + "\n"]
    return counted
