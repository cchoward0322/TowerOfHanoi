import tkinter as tk
import time
from hanoi import solve

#USING TKINTER, OTHER USES TURTLE

#TO RUN WINDOW, open terminal and type: python visualizer.py

# Imported func solve for recursive problem

#creating the main window
root = tk.Tk()
root.title("Tower of Hanoi: Visualizer")

#setting window dimensions
WIDTH = 600
HEIGHT = 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

#root.geometry("600x400")

peg_X = {1: 100, 2: 300, 3: 500} #centers of each peg, x axis
pegs = {1:[3], 2:[2], 3:[1]} #state of each peg
colors = {1: "yellow", 2: "blue", 3: "red"} # color of each disk

#add text onto the screen
label = tk.Label(root, text = "This is a visualizer for the Tower of Hanoi problem.")
label.place(x=10, y=50)

label2 = tk.Label(root, text = "You can use this window to visualize the steps taken to solve the problem!")
label2.place(x=10, y=70)

#add button
button = tk.Button(root, text = "Solve puzzle!", command = lambda: print("Button clicked!"))
button.place(x=20, y=110)

#rectangle for pegs
canvas.create_rectangle(97, 200, 103, 350, fill="gray70")
canvas.create_rectangle(297, 200, 303, 350, fill="gray70")
canvas.create_rectangle(497, 200, 503, 350, fill="gray70")

# tested disks as rectangles
#canvas.create_rectangle(35, 330, 165, 350, fill="red", outline = "black")
#canvas.create_rectangle(55, 310, 145, 330, fill="blue", outline = "black")
#canvas.create_rectangle(75, 290, 125, 310, fill="yellow", outline = "black")
#(15 + 10*disk(1)) - ignore j messing around

# testing to print out locations of movement of disks on pegs
for peg in pegs:
    stack = pegs[peg]       # the list of disks in this stack
    for level in range(len(stack)):
        disk = stack[level]
        x = peg_X[peg]  # center of each peg
        half = 5 + 20*disk
        bottom = 350 - 20*level
        top = bottom - 20

        canvas.create_rectangle(x - half, top, x + half, bottom, fill=colors[disk], outline = "black")



#keeping the window open, make sure this line ALWAYS stays at the bottom of the code
root.mainloop()
