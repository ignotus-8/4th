import os
os.system("cls")

import re

def validMAC (string: str)->bool:
    pattern = r"^([0-9A-Fa-f]{2}[-:]){5}([0-9A-Fa-f]{2})$"

    return (re.fullmatch(pattern, string))

if(validMAC("00:1A:2B:3C:4D:5E")):
    print("valid")
else:
    print("Invalid")