"""
Program: TitleScreen.py - Two-Dice Pig Game Main Menu
Date: November 28, 2025
Programmer: Sanjith Diddla
Description: Main menu interface for the Two-Dice Pig game. Displays title screen
with three buttons: HELP (opens instructions), PLAY (starts game), 
and EXIT (closes application). Features Peppa Pig themed design.
Plays background music using pygame.

"""

import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import subprocess
import pygame  

window = tk.Tk()
window.title("PIG GAME")
window.geometry("758x538")
window.resizable(False, False)

current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize pygame mixer
pygame.mixer.init()
try:
    pygame.mixer.music.load(os.path.join(current_dir, "mainmenu.mp3"))
    pygame.mixer.music.play(loops=-1)  # Loop indefinitely
    pygame.mixer.music.set_volume(0.3)  # Set volume (0.0 to 1.0)
except:
    print("mainmenu.mp3 not found, no background music will play.")

# Load background image
try:
    bg = Image.open(os.path.join(current_dir, "TitleScreen.png")).resize((758, 538))
    bg_img = ImageTk.PhotoImage(bg)
    tk.Label(window, image=bg_img).place(x=0, y=0)
except:
    window.configure(bg="black")

# Run another Python script
def run_script(filename):
    script_path = os.path.join(current_dir, filename)
    subprocess.Popen([sys.executable, script_path])
    window.destroy()

# Button functions
def help_clicked():
    run_script("helpScreen.py")

def play_clicked():
    run_script("pigGame.py")

def exit_clicked():
    window.destroy()

# Buttons at the bottom
tk.Button(window, text="HELP", command=help_clicked, font=("Arial", 16, "bold"), 
          bg="#fbb740", fg="#fffffe", relief="raised", bd=0).place(x=84, y=432, width=163, height=52)

tk.Button(window, text="PLAY", command=play_clicked, font=("Arial", 16, "bold"), 
          bg="#49af56", fg="#fffffe", relief="raised", bd=0).place(x=295, y=431, width=170, height=55)

tk.Button(window, text="EXIT", command=exit_clicked, font=("Arial", 16, "bold"), 
          bg="#e26464", fg="#fffffe", relief="raised", bd=0).place(x=503, y=431, width=169, height=55)

window.mainloop()
