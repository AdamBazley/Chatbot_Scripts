ScriptName = "Book Vote Tally"
Website = ""
Description = "Counts the number of votes each book has."
Creator = "SparahawkNZ"
Version = "1.0.0"

Command = "!bookvotecount"
FilePath = r"D:\Chatbot Text Files\Bookish Bel\NextBook.txt"

def Init():
    return

def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    lines = []
    with open(FilePath) as f:
        for line in f:
            lines.append(line.lower())

    lines[0] = lines[0][3:]

    message = Count(lines)
    uniqueMessage = unique(message)

    for x in uniqueMessage:
        send_message(x)


    return

def Tick():
    return

def Log(message):
    Parent.Log(Command, message)
    return

def unique(list1):
    list_set = set(list1)
    uniqueList = (list(list_set))
    return uniqueList


def send_message(message):
    Parent.SendStreamMessage(message)
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
    #f = open(FilePath, 'r+')
    lines = []
    with open(FilePath) as f:
        for line in f:
            lines.append(line)

    #f.close()
    return lines

def Count(list):
    counted =[]
    for x in list:
        x2 = x.replace("\n", " ")
        counted.append(x2 + ": " + str(list.count(x)) + "\n")
    return counted
