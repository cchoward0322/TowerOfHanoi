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
pegs = {1:[3,2,1], 2:[], 3:[]} #state of each peg
colors = {1: "green", 2: "blue", 3: "red"} # color of each disk
moves = solve(3, 1, 3)      #from hanoi.py
step_count = 0

#add text onto the screen
label = tk.Label(root, text = "This is a visualizer for the Tower of Hanoi problem.")
label.place(x=10, y=50)

label2 = tk.Label(root, text = "You can use this window to visualize the steps taken to solve the problem!")
label2.place(x=10, y=70)

# tested disks as rectangles
#canvas.create_rectangle(35, 330, 165, 350, fill="red", outline = "black")
#canvas.create_rectangle(55, 310, 145, 330, fill="blue", outline = "black")
#canvas.create_rectangle(75, 290, 125, 310, fill="yellow", outline = "black")
#(15 + 10*disk(1)) - ignore j messing around

def draw_game():        # so it can run more then just once
    canvas.delete("all")        #restarting the canvas

    #rectangle for pegs
    canvas.create_rectangle(97, 200, 103, 350, fill="gray70")
    canvas.create_rectangle(297, 200, 303, 350, fill="gray70")
    canvas.create_rectangle(497, 200, 503, 350, fill="gray70")

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


def next_step():
    global step_count

    if step_count == len(moves):
        return
    
    start, end = moves[step_count]

    disk = pegs[start].pop()    #remove the top disk from the start peg and keep it
    pegs[end].append(disk)      #put it ontop of the last peg
    step_count = step_count + 1     #done one move

    draw_game()        #redraw board at new state


#add button
button = tk.Button(root, text = "Next Move!", command = next_step)
button.place(x=20, y=110)

draw_game()

#keeping the window open, make sure this line ALWAYS stays at the bottom of the code
root.mainloop()
