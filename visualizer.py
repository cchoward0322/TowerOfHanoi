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

#centers of each peg, x axis
PEG_X = {1: 100, 2: 300, 3: 500} 

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

#add rectangles for disks
canvas.create_rectangle(55, 330, 145, 350, fill="red", outline = "black")
#(15 + 10*disk(1)) - ignore j messing around


#keeping the window open, make sure this line ALWAYS stays at the bottom of the code
root.mainloop()
