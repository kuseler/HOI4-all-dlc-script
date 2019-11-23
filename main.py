import os
import shutil
                
##aa = os.listdir("C:\\Users\\kimue\\Documents\\Paradox Interactive\\Hearts of Iron IV\mod\\unlock\\national_focus")
##for i in aa:
##    ersetzen("has_dlc", "C:\\Users\\kimue\\Documents\\Paradox Interactive\\Hearts of Iron IV\mod\\unlock\\national_focus" + "\\" + i)
##


def ersetzen(string, quelle):
    with open(quelle, "r") as f:
        lines = f.readlines()
    with open(quelle, "w") as f:
        for line in lines:
            if not (string in line):
                f.write(line)
            else:
                print(line)

def haupt(ordner):
    aa = os.listdir(ordner)
    
    for i in aa:
        print(i)
        try:
            haupt(ordner + "\\" + i)

        except:
            ersetzen("has_dlc", ordner + "\\" + i)


def überordner(überordner):
    for i in os.listdir(überordner):
        haupt(überordner+"\\"+i)


#requires any entry as input
def hauptsimon(entry_path):
  if (os.path.isfile(entry_path)):
    ersetzen('has_dlc', entry_path)
  else:
    aa = os.listdir(entry_path)
    for i in aa:
        haupt(entry_path + "\\" + i)        
##überordner("C:\\Users\\kimue\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\ert\\common\\decisions")


print("create a new mod by starting the launcher, scrolling down to or clicking on 'Mods', then click on 'Mod-tool', then input any name, the current version and the folder.")
quellort = input("if you're done, search for hoi4 dir, and put it in here, but replace every '\\' with '\\\\\' :")
zielort = input("input the mod folder, usually on C:\\User\\username\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\modname: ")
lst = ("decisions", "national_focus", "opinion_modifiers", "technologies", "wargoals")
os.mkdir(zielort + "common")
for i in lst:
    shutil.copytree(quellort + "\\common\\"+i, zielort + "\\common")
haupt(zielort)

print("success!")

##haupt("C:\\Users\\kimue\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\ert\\common")



