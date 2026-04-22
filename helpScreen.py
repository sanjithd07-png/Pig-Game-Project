"""
Program: helpScreen.py - Two-Dice Pig Game Help Screen
Date: November 28, 2025
Programmer: Sanjith Diddla
Description: Displays game instructions and rules for Two-Dice Pig.
Includes buttons to return to main menu or exit the application.
Plays background music using pygame.

"""

import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import subprocess
import pygame 

window = tk.Tk()
window.title("How to Play – Pig Dice Game")

# Window size
WIDTH = 512
HEIGHT = 768
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize pygame mixer
pygame.mixer.init()
try:
    pygame.mixer.music.load(os.path.join(current_dir, "mainmenu.mp3"))
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.3)
except:
    print("mainmenu.mp3 not found, no background music will play.")

# Load background image
try:
    img_path = os.path.join(current_dir, "helpscreen.png")
    help_img = Image.open(img_path).resize((WIDTH, HEIGHT))
    help_img = ImageTk.PhotoImage(help_img)
    tk.Label(window, image=help_img).place(x=0, y=0)
except Exception as e:
    tk.Label(window, text=f"Error loading image:\n{e}", font=("Arial", 14)).pack(pady=20)

# Button functions
def go_main_menu():
    title_path = os.path.join(current_dir, "TitleScreen.py")
    subprocess.Popen([sys.executable, title_path])
    window.destroy()

def exit_game():
    window.destroy()

# Button positions and sizes
button_width = 80
button_height = 40

button_y = (HEIGHT // 2) - 15 - 50
button_x = WIDTH - 10

exit_btn_x = (button_x - button_width) - 18
exit_btn_y = (button_y + button_height + 5) + 20

main_menu_x = exit_btn_x - 5
main_menu_y = button_y - 50 - 210

# Main Menu button
main_menu_btn = tk.Button(window, text="Main Menu", command=go_main_menu, font=("Arial", 12),
                          bg="#49af56", fg="#fffffe", relief="raised", bd=0)
main_menu_btn.place(
    x=main_menu_x,
    y=main_menu_y,
    width=button_width,
    height=button_height
)

# Exit button
exit_btn = tk.Button(window, text="Exit", command=exit_game, font=("Arial", 12),
                     bg="#e26464", fg="#fffffe", relief="raised", bd=0)
exit_btn.place(
    x=main_menu_x - 350,
    y=main_menu_y,
    width=button_width,
    height=button_height
)

window.mainloop()
