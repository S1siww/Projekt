import tkinter as tk
import random

# vytvorenie okna
okno = tk.Tk()
okno.title("Pexeso")

# vytvorenie premenných
karty = list("AABBCCDDEEFFGGHH")  # 8 párov
random.shuffle(karty)
tlacidla = []
prevratene = []
najdene = []