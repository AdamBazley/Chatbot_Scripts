ScriptName = "The Arena Damage Calculator"
Website = "https://sparabel.com/arena/"
Description = "Takes damage dealt in as a parameter, deducts it from the defenders health and adds it to the attackers damage dealt total"
Creator = "SparahawkNZ"
Version = "1.0.0"

Command = "!attack"

def Init():
    return

def Execute(data):
    if data.GetParam(0) != Command:
        return
    
    attacker = str(data.GetParam(1))
    defender = str(data.GetParam(2))
    damage = int(data.GetParam(3))

    damageDeltFile = r"D:\\Chatbot Text Files\\The Arena\Damage Dealt\\" +attacker+"Damage.txt"
    defenderHealthFile = r"D:\\Chatbot Text Files\\The Arena\Health\\"+defender+"Health.txt"

    f = open(damageDeltFile, "r")
    currentDamage = f.read()[3:]
    f.close()

    log("Stripped Number Read From Damage File: "+currentDamage)
    newDamage = int(currentDamage) + damage

    newDamageStr = "DD:"+str(newDamage)
    log("Modded Damge Writen To File: "+newDamageStr)

    f2 = open (damageDeltFile, "w")
    f2.write(newDamageStr)
    f2.close

    f3 = open(defenderHealthFile, "r")
    currentHealth = f3.read()[3:]
    f3.close()

    log("Stripped Number Read From Health File: "+currentHealth)

    newHealth = int(currentHealth) - damage
    newHealthStr = "HP:"+str(newHealth)

    log("Modded Health Writen To File: "+newHealthStr)

    f4 = open (defenderHealthFile, "w")
    f4.write(str(newHealthStr))
    f4.close
    send_message(attacker+" Total Damage Delt: "+str(newDamage))
    send_message(defender+" Current Health: "+str(newHealth))
    return

def Tick():
    return

def Log(message):
    Parent.Log(Command, message)
    return

def send_message(message):
    Parent.SendStreamMessage(message)
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

def log(message):
    
    Parent.Log(Command, message)
    return