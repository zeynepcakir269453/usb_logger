from ctypes import windll
import string

def drive_find():
    bitmask = windll.kernel32.GetLogicalDrives()
    drive=list()
    for harf in string.ascii_uppercase:
        if bitmask & 1:
            drive.append(harf)
        bitmask>>=1
    return drive
print(drive_find())