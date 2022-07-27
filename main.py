import os
import shutil

print("You will have to run this every time roblox updates. I might be able to make it automatic.")



def deleteFile(dirSounds):
    if os.path.exists(dirSounds):
        if os.path.exists(dirSounds+"\\content\\sounds\\ouch.ogg"):
            os.remove(dirSounds+"\\content\\sounds\\ouch.ogg")
            print("Removed new Ouch sound")
        else:
            print("The file does not exist")

dirRoblox = input("Dir: \n")
deleteFile(dirRoblox)
oofSound = "sounds/ouch.ogg"


movedOofSound = shutil.move(oofSound, dirRoblox+"\\content\\sounds")
print("Added new oof")
shutil.copy(movedOofSound, "sounds")
print("Duplicated oof sound")
