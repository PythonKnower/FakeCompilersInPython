from tqdm import tqdm
import os
import time
from colorama import Fore as F, Style as S

info = [
    "Making DLL",
    "Translating to Byte code",
    "Compiling to Machine code",
    "Linking",
    "Optimizing",
    "Translating into Bit-Machine code",
    "Translating into Machine code",
    "Decompiling for no errors",
    "Testing",
    "Compiling back to Machine code",
    "Translating into Bit-Machine code",
    "Finalizing",
    "Done"
]
modulesORother = [
    "DLL",
    "libraries",
    "modules"
]
lib_warnings = [
    "Could not define a library, finding source code.. Will not give info after the library is defined.",
    "Could not generate DLL, will use basic terminal instead if failed for 5 attemps, retrying.. --NO-INFO-AFTER-RETRIED-SUCCESS"
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def info_send(msg):
    print(f"{F.CYAN}[INFO] {msg} {S.RESET_ALL}")
def warn_send(msg):
    print(f"{F.YELLOW}[WARN] {msg} {S.RESET_ALL}")
def error_send(msg):
    print(f"{F.RED}[ERROR] {msg} {S.RESET_ALL}")

File = input("File to compile: ")
print(f"Will compile {File} into {File}.exe")

for stage in info:
    info_send(stage)
    time.sleep(0.05)

    if stage == "Optimizing":
        warn_send("Optimizing is not supported yet")
        warn_send("Will skip optimization and continue with current file size")
    elif stage == "Translating into Bit-Machine code":
        error_send("Could not translate into Bit-Machine code, will try using Machine code instead")
    elif stage == "Making DLL":
        error_send("DLL not created, won't continue with the process of making a DLL.")
    elif stage == "Translating to Byte code":
        warn_send("Could not translate to Byte code, will try using Machine code instead")

for i in tqdm(range(100), desc="Converting"):
    time.sleep(0.01)
    clear()
    tqdm.write(f"Step {i} complete!")
    
time.sleep(1)
clear()
print(f"Successfully compiled {File} into {File}.exe")
# With help of: Github Copilot from VS Code
# And also with help from CodeGeeX
# Don't talk to the silent staring guy..
#  _______________           ___________________
# /               \         /     who u         \
# |    0      0   |        |  lookin at         |
# |      ----     |        \_______bru?________/
# \______________/
# Coding is life,
# Style,
# Love
# And the only thing that matters.
# with kitty :3
# Made by Max, Github Copilot VS code and CodeGeeX.
# Released on January 17th, 2025
# Updated in: NONE
