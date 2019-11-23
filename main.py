import os
import shutil
                



def replace(string, source):
    with open(source, "r") as f:
        lines = f.readlines()
    with open(source, "w") as f:
        for line in lines:
            if not (string in line):
                f.write(line)
            else:
                print(line)

def haupt(ordner):
    subfolder = os.listdir(ordner)
    
    for i in subfolder:
        print(i)
        try:
            haupt(ordner + "\\" + i)

        except:




#requires any entry as input
def hauptsimon(entry_path):
  if (os.path.isfile(entry_path)):
  else:
    aa = os.listdir(entry_path)
    for i in aa:
        hauptsimon(entry_path + "\\" + i)        


print("create a new mod by starting the launcher, scrolling down to or clicking on 'Mods', then click on 'Mod-tool', then input any name, the current version and the folder.")
quellort = input("if you're done, search for hoi4 dir, and put it in here, but replace every '\\' with '\\\\\', (its propably something like 'SteamLibrary\steamapps\common\Hearts of Iron IV') :")
zielort = input("input the mod folder, usually on C:\\User\\username\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\modname: ")


##lst = ("decisions", "national_focus", "opinion_modifiers", "technologies", "wargoals")
##os.mkdir(zielort + "common")
##for i in lst:
##    shutil.copytree(quellort + "\\common\\"+i, zielort + "\\common")
haupt(zielort)

print("success!")




