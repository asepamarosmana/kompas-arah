import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk

def direction(facing, turn):
    directions = ["N","NE","E","SE","S","SW","W","NW"]
    start = directions.index(facing)
    steps = round(turn / 45)
    value = (start + steps) % 8
    return directions[value]

def draw_compass(current):
    directions = ["N","NE","E","SE","S","SW","W","NW"]
    angles = np.linspace(0, 2*np.pi, 9)[:-1]
    x = np.cos(angles)
    y = np.sin(angles)
    
    fig, ax = plt.subplots(figsize=(3,3))
    ax.set_aspect("equal")
    ax.axis("off")
    
    circle = plt.Circle((0,0), 1, fill=False)
    ax.add_artist(circle)
    
    for i, d in enumerate(directions):
        ax.text(1.2*x[i], 1.2*y[i], d, ha="center", va="center", fontsize=10, fontweight="bold")
    
    idx = directions.index(current)
    ax.arrow(0,0, x[idx]*0.8, y[idx]*0.8, head_width=0.1, head_length=0.1, fc="red", ec="red")
    
    file_path = "compass_result.png"
    plt.savefig(file_path)
    plt.close()
    return file_path

def calculate():
    facing = entry_facing.get().upper()
    try:
        turn = int(entry_turn.get())
    except ValueError:
        messagebox.showerror("Error", "Turn harus angka!")
        return
    
    if facing not in ["N","NE","E","SE","S","SW","W","NW"]:
        messagebox.showerror("Error", "Facing harus salah satu dari N, NE, E, SE, S, SW, W, NW")
        return
    
    result = direction(facing, turn)
    label_result.config(text=f"Arah akhir: {result}")
    
    img_path = draw_compass(result)
    img = Image.open(img_path)
    img = img.resize((200,200))
    photo = ImageTk.PhotoImage(img)
    
    label_img.config(image=photo)
    label_img.image = photo

root = tk.Tk()
root.title("Kompas Arah")

tk.Label(root, text="Facing (N, NE, E, SE, S, SW, W, NW):").pack()
entry_facing = tk.Entry(root)
entry_facing.pack()

tk.Label(root, text="Turn (derajat):").pack()
entry_turn = tk.Entry(root)
entry_turn.pack()

btn = tk.Button(root, text="Hitung", command=calculate)
btn.pack(pady=5)

label_result = tk.Label(root, text="Arah akhir: -", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

label_img = tk.Label(root)
label_img.pack()

root.mainloop()





