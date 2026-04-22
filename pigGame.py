"""
Program: pigGame.py - Two-Dice Pig Game
Date: November 28, 2025
Programmer: Sanjith Diddla
Description: The actual game code with all the functions including rolling, hold, new game, quit and sounds.
"""

import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import pygame
import subprocess
import sys

# ---- Window ---- #
window = Tk()
window.title("Two-Dice Pig")
window.geometry("991x587")
window.resizable(False, False)

current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize pygame mixer for sound
pygame.mixer.init()

# Load background music
try:
    pygame.mixer.music.load(os.path.join(current_dir, "background.mp3"))
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.3)
except:
    print("Background music not found")

# Load dice roll sound effect
try:
    dice_sound = pygame.mixer.Sound(os.path.join(current_dir, "dice.mp3"))
except:
    dice_sound = None
    print("Dice roll sound not found")

# Background image
image1 = Image.open(os.path.join(current_dir, "piggame.png"))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(window, image=test)
label1.image = test
label1.place(x=0, y=0)

# Game state variables
turn = True
next = "Player 1's Turn"
P1RS, P1TS, P2RS, P2TS = 0, 0, 0, 0

# Text fields
t3 = Entry(window, font=("Courier New", 16, "bold"), justify="center", bg="#c4426b", fg="white")
t4 = Entry(window, font=("Courier New", 16, "bold"), justify="center", bg="#c4426b", fg="white")
t5 = Entry(window, font=("Courier New", 16, "bold"), justify="center", bg="#c4426b", fg="white")
t6 = Entry(window, font=("Courier New", 16, "bold"), justify="center", bg="#c4426b", fg="white")
t7 = Entry(window, font=("Comic Sans MS", 12, "bold"), justify="center", bg="white", fg="#2d1810")

t3.place(x=219, y=315, width=60, height=40)
t4.place(x=219, y=435, width=60, height=40)
t5.place(x=718, y=315, width=60, height=40)
t6.place(x=718, y=435, width=60, height=40)
t7.place(x=421, y=100, width=160, height=30)

# Dice images
dice_imgs = [
    os.path.join(current_dir, "one.png"),
    os.path.join(current_dir, "two.png"),
    os.path.join(current_dir, "three.png"),
    os.path.join(current_dir, "four.png"),
    os.path.join(current_dir, "five.png"),
    os.path.join(current_dir, "six.png")
]

# Blank dice image
blank_img = Image.open(os.path.join(current_dir, "blank.jpg")).resize((120, 120))
blank_photo = ImageTk.PhotoImage(blank_img)

l1 = tkinter.Label(window, image=blank_photo, bd=0, highlightthickness=0)
l1.image = blank_photo
l1.place(x=435, y=137, width=120, height=120)

l2 = tkinter.Label(window, image=blank_photo, bd=0, highlightthickness=0)
l2.image = blank_photo
l2.place(x=435, y=262, width=120, height=120)

# Status message
status_msg = tkinter.Label(window, text="Roll the dice to begin!", font=("Arial", 13, "bold"), bg="#d49cae", fg="#2d1810")
status_msg.place(x=350, y=550, width=300, height=30)

# Check winner
def check_winner():
    global turn
    if P1TS >= 100:
        status_msg.config(text="Player 1 wins! 🎉")
        messagebox.showinfo("Game Over!", "🎉 Player 1 WINS! 🎉")
        roll_dice.config(state=DISABLED)
        hold.config(state=DISABLED)
        return True
    elif P2TS >= 100:
        status_msg.config(text="Player 2 wins! 🎉")
        messagebox.showinfo("Game Over!", "🎉 Player 2 WINS! 🎉")
        roll_dice.config(state=DISABLED)
        hold.config(state=DISABLED)
        return True
    return False

# Pass turn
def Pass():
    global turn, P1RS, P1TS, P2RS, P2TS, next
    if turn:
        P1TS += P1RS
        P1RS = 0
        turn = False
        next = "Player 2's Turn"
        status_msg.config(text="Player 1 held! Turn passed.")
    else:
        P2TS += P2RS
        P2RS = 0
        turn = True
        next = "Player 1's Turn"
        status_msg.config(text="Player 2 held! Turn passed.")

    t3.delete(0, END)
    t3.insert(0, str(P1RS))
    t4.delete(0, END)
    t4.insert(0, str(P1TS))
    t5.delete(0, END)
    t5.insert(0, str(P2RS))
    t6.delete(0, END)
    t6.insert(0, str(P2TS))
    t7.delete(0, END)
    t7.insert(0, next)

    check_winner()

# Roll dice
def Roll():
    global turn, P1RS, P1TS, P2RS, P2TS, l1, l2, next

    if dice_sound:
        dice_sound.play()

    rand1 = random.randint(1, 6)
    rand2 = random.randint(1, 6)

    for i in range(10):
        random_dice1 = random.randint(1, 6)
        random_dice2 = random.randint(1, 6)
        img1 = Image.open(dice_imgs[random_dice1-1]).resize((120, 120))
        img2 = Image.open(dice_imgs[random_dice2-1]).resize((120, 120))
        photo1 = ImageTk.PhotoImage(img1)
        photo2 = ImageTk.PhotoImage(img2)
        l1.config(image=photo1)
        l1.image = photo1
        l2.config(image=photo2)
        l2.image = photo2
        window.update()
        window.after(50)

    img1 = Image.open(dice_imgs[rand1-1]).resize((120,120))
    img2 = Image.open(dice_imgs[rand2-1]).resize((120,120))
    final_photo1 = ImageTk.PhotoImage(img1)
    final_photo2 = ImageTk.PhotoImage(img2)
    l1.config(image=final_photo1)
    l1.image = final_photo1
    l2.config(image=final_photo2)
    l2.image = final_photo2

    if turn:
        if rand1==1 and rand2==1:
            P1TS = 0
            P1RS = 0
            turn = False
            next = "Player 2's Turn"
            status_msg.config(text="Snake eyes! Total reset!")
            messagebox.showerror("Snake Eyes! 🎲🎲", f"Player 1 rolled double 1s!\nTotal score reset to 0!\n\nPlayer 2's turn now.")
        elif rand1==rand2:
            P1RS += rand1 + rand2
            hold.config(state=DISABLED)
            status_msg.config(text=f"Doubles ({rand1},{rand2}) - Must roll again!")
            messagebox.showwarning("Doubles! 🎲", f"Player 1 rolled doubles ({rand1},{rand2})!\nYou MUST roll again!")
        elif rand1==1 or rand2==1:
            P1RS = 0
            turn = False
            next = "Player 2's Turn"
            status_msg.config(text="Rolled a 1 - Turn ends!")
            messagebox.showwarning("Rolled a 1!", f"Player 1 rolled a 1!\nTurn score lost!\n\nPlayer 2's turn now.")
        else:
            P1RS += rand1 + rand2
            hold.config(state=NORMAL)
            status_msg.config(text=f"Rolled {rand1} and {rand2} - Roll or Hold?")
    else:
        if rand1==1 and rand2==1:
            P2TS = 0
            P2RS = 0
            turn = True
            next = "Player 1's Turn"
            status_msg.config(text="Snake eyes! Total reset!")
            messagebox.showerror("Snake Eyes! 🎲🎲", f"Player 2 rolled double 1s!\nTotal score reset to 0!\n\nPlayer 1's turn now.")
        elif rand1==rand2:
            P2RS += rand1 + rand2
            hold.config(state=DISABLED)
            status_msg.config(text=f"Doubles ({rand1},{rand2}) - Must roll again!")
            messagebox.showwarning("Doubles! 🎲", f"Player 2 rolled doubles ({rand1},{rand2})!\nYou MUST roll again!")
        elif rand1==1 or rand2==1:
            P2RS = 0
            turn = True
            next = "Player 1's Turn"
            status_msg.config(text="Rolled a 1 - Turn ends!")
            messagebox.showwarning("Rolled a 1!", f"Player 2 rolled a 1!\nTurn score lost!\n\nPlayer 1's turn now.")
        else:
            P2RS += rand1 + rand2
            hold.config(state=NORMAL)
            status_msg.config(text=f"Rolled {rand1} and {rand2} - Roll or Hold?")

    t3.delete(0, END)
    t3.insert(0, str(P1RS))
    t4.delete(0, END)
    t4.insert(0, str(P1TS))
    t5.delete(0, END)
    t5.insert(0, str(P2RS))
    t6.delete(0, END)
    t6.insert(0, str(P2TS))
    t7.delete(0, END)
    t7.insert(0, next)

    check_winner()

# New game function
def new_game_func():
    global turn, P1RS, P1TS, P2RS, P2TS, next
    turn = True
    next = "Player 1's Turn"
    P1RS, P1TS, P2RS, P2TS = 0, 0, 0, 0

    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t7.insert(0, next)

    status_msg.config(text="New game started! Player 1 begins.")
    l1.config(image=blank_photo)
    l2.config(image=blank_photo)

    roll_dice.config(state=NORMAL)
    hold.config(state=NORMAL)

def quit_to_menu():
    title_path = os.path.join(current_dir, "TitleScreen.py")
    subprocess.Popen([sys.executable, title_path])
    window.destroy()  # Close the current game window

# Buttons
new_game = Button(window, text="NEW GAME", font=("Arial", 13, "bold"), bg="#28a745", fg="white", command=new_game_func)
new_game.place(x=414, y=43, width=165, height=38)

roll_dice = Button(window, text="ROLL DICE", font=("Arial", 12, "bold"), bg="#007bff", fg="white", command=Roll)
roll_dice.place(x=419, y=396, width=155, height=38)

hold = Button(window, text="HOLD", font=("Arial", 12, "bold"), bg="#ffc107", fg="black", command=Pass)
hold.place(x=433, y=467, width=127, height=33)

exit_button = Button(window, text="EXIT", font=("Arial", 12, "bold"), bg="#dc3545", fg="white", command=window.destroy)
exit_button.place(x=433, y=510, width=127, height=33)

menu_button = Button(window, text="QUIT TO MENU", font=("Arial", 14, "bold"), bg="#a73681", fg="white", command=quit_to_menu)
menu_button.place(x=420, y=5, width=150, height=35)  

window.mainloop()
