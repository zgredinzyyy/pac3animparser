import re
import os

translate = {    
    "left finger 01":   "ValveBiped.Bip01_L_Finger01",
    "left finger 1":    "ValveBiped.Bip01_L_Finger1",
    "left finger 2":    "ValveBiped.Bip01_L_Finger2",
    "left finger 3":    "ValveBiped.Bip01_L_Finger3",
    "left finger 4":    "ValveBiped.Bip01_L_Finger4",
    "left finger 02":   "ValveBiped.Bip01_L_Finger02",
    "left finger 11":   "ValveBiped.Bip01_L_Finger11",
    "left finger 21":   "ValveBiped.Bip01_L_Finger21",
    "left finger 31":   "ValveBiped.Bip01_L_Finger31",
    "left finger 41":   "ValveBiped.Bip01_L_Finger41",
    "left finger 12":   "ValveBiped.Bip01_L_Finger12",
    "left finger 22":   "ValveBiped.Bip01_L_Finger22",
    "left finger 32":   "ValveBiped.Bip01_L_Finger32",
    "left finger 42":   "ValveBiped.Bip01_L_Finger42",
    "left hand":        "ValveBiped.Bip01_L_Hand",
    "left forearm":     "ValveBiped.Bip01_L_Forearm",
    "left upperarm":    "ValveBiped.Bip01_L_UpperArm",
    "left calf":        "ValveBiped.Bip01_L_Calf",
    "left thigh":       "ValveBiped.Bip01_L_Thigh",
    "left foot":        "ValveBiped.Bip01_L_Foot",
    "left toe":         "ValveBiped.Bip01_L_Toe1",
    "right finger 01":  "ValveBiped.Bip01_R_Finger01",
    "right finger 1":   "ValveBiped.Bip01_R_Finger1",
    "right finger 2":   "ValveBiped.Bip01_R_Finger2",
    "right finger 3":   "ValveBiped.Bip01_R_Finger3",
    "right finger 4":   "ValveBiped.Bip01_R_Finger4",
    "right finger 02":  "ValveBiped.Bip01_R_Finger02",
    "right finger 11":  "ValveBiped.Bip01_R_Finger11",
    "right finger 21":  "ValveBiped.Bip01_R_Finger21",
    "right finger 31":  "ValveBiped.Bip01_R_Finger31",
    "right finger 41":  "ValveBiped.Bip01_R_Finger41",
    "right finger 12":  "ValveBiped.Bip01_R_Finger12",
    "right finger 22":  "ValveBiped.Bip01_R_Finger22",
    "right finger 32":  "ValveBiped.Bip01_R_Finger32",
    "right finger 42":  "ValveBiped.Bip01_R_Finger42",
    "right hand":       "ValveBiped.Bip01_R_Hand",
    "right forearm":    "ValveBiped.Bip01_R_Forearm",
    "right upperarm":   "ValveBiped.Bip01_R_UpperArm",
    "right calf":       "ValveBiped.Bip01_R_Calf",
    "right thigh":      "ValveBiped.Bip01_R_Thigh",
    "right foot":       "ValveBiped.Bip01_R_Foot",
    "right toe":        "ValveBiped.Bip01_R_Toe1",
    "Name=bone":        "ValveBiped.Bip01_Head1",
    "spine":            "ValveBiped.Bip01_Spine",
    "spine 1":          "ValveBiped.Bip01_Spine1",
    "spine 2":          "ValveBiped.Bip01_Spine2",
    "spine 3":          "ValveBiped.Bip01_Spine3",
    "spine 4":          "ValveBiped.Bip01_Spine4",
    "pelvis":           "ValveBiped.Bip01_Pelvis",
    "left clavicle":    "ValveBiped.Bip01_L_Clavicle",
    "right clavicle":    "ValveBiped.Bip01_R_Clavicle",
}

subject = "onedrive/pictures/pac3/here/toparse.txt"
template = "onedrive/pictures/pac3/template.txt"
steamPath = "Steam/steamapps/common/GarrysMod/garrysmod/addons/"
folder = "jojoposes"

print("Podaj nazwę do folderu")
folderName = input()
folderName = folderName + "_animation_swep"

print("Print name")
printName = input()

print("Prupose")
purpose = input()

print("Instruction")
instr = input()

exp = 14

animFile = open(subject, 'r')

test = animFile.readlines()

with open(template, 'r') as f:
    lines = f.readlines()

os.chdir("F:/" + steamPath + folder + "/lua/weapons")

if not os.path.exists(folderName):
    os.mkdir(folderName)

with open(folderName + "/shared.lua", 'w') as f:
    for i,links in enumerate(lines):
        if i == 5:
            f.write("SWEP.Purpose" + "\t\t\t\t" + "= \"" + purpose + "\"\n")
            f.write("SWEP.Instructions" + "\t\t\t" + "= \"" + instr + "\"\n")
            f.write("SWEP.PrintName" + "\t\t\t\t" + "= \"" + printName + "\"\n\n")
        if i == exp:
            for index, obj in enumerate(test):
                if "Angles" in obj:
                    ang = obj.strip()
                    ang = re.sub(r"[\n\t]*", "", ang)
                    ang = ang.replace("=", "(")
                    ang = ang.replace(" ", ", ")
                    ang = ang.replace("s", "")
                    ang = ang + ")"

                    line = test[index + 1].strip()
                    line = re.sub(r"[\n\t]*", "", line)
                    line = line[5:]
                    if translate[line]:
                        composed = "[\"" + translate[line] + "\"]" + " = " + ang + ","
                        f.write("\t\t\t\t" + composed + "\n")
        f.write(links)