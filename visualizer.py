import tkinter as tk
import time
from hanoi import solve

#USING TKINTER

#TO RUN WINDOW, open terminal and type: python visualizer.py

# Imported func solve for recursive problem

#creating the main window
root = tk.Tk()
root.title("Tower of Hanoi: Visualizer")

#CONFIGURATION: Change these values to adjust the puzzle!
num_disks = 3  #change to any number (3, 4, 5, 7, etc.)
num_pegs = 3   #kept at 3 for testing

#setting window dimensions
WIDTH = 600
HEIGHT = 400
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

#adjust window size to fit moves display
root.geometry("800x500")

#root.geometry("600x400")

peg_X = {1: 100, 2: 300, 3: 500} #centers of each peg, x axis

# state of each peg
#first peg gets all disks in descending order
pegs = {1: list(range(num_disks, 0, -1)), 2: [], 3: []}

#generate colors dynamically for all disks
disk_colors = ["green", "blue", "red", "yellow", "orange", "purple", "cyan", "magenta"]
colors = {i + 1: disk_colors[i % len(disk_colors)] for i in range(num_disks)}

moves = solve(num_disks, 1, num_pegs)      #from hanoi.py
step_count = 0

#add text onto the screen
label = tk.Label(root, text = "This is a visualizer for the Tower of Hanoi problem.")
label.place(x=10, y=50)

label2 = tk.Label(root, text = "You can use this window to visualize the steps taken to solve the problem!")
label2.place(x=10, y=70)


#add text onto the screen labeling each peg (1-3)
label3 = tk.Label(root, text = "Peg 1")
label3.place(x=90, y=180)

label4 = tk.Label(root, text = "Peg 2")
label4.place(x=290, y=180)

label5 = tk.Label(root, text = "Peg 3")
label5.place(x=490, y=180)

#create a frame to dipslay list of moves (peg -> peg) on right side of window
#setting dimensions of the frame to fit the moves display
moves_frame = tk.Frame(root, bg="lightgray", width=150, height=150)
moves_frame.place(x=620, y=0)

#lightgrey box labeled "Moves:"
moves_label = tk.Label(moves_frame, text="Moves:", bg="lightgray", font=("Arial", 10, "bold"))
moves_label.pack(side=tk.TOP, padx=5, pady=5)

#add a scrollable text widget to display moves (if needed)
moves_text = tk.Text(moves_frame, width=20, height=8, font=("Arial", 8))
moves_scrollbar = tk.Scrollbar(moves_frame, command=moves_text.yview)
moves_text.config(yscrollcommand=moves_scrollbar.set)
moves_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
moves_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Populate the text widget with all moves
for i, (start, end) in enumerate(moves):
    moves_text.insert(tk.END, f"{i+1}. Peg {start} → {end}\n")
moves_text.config(state=tk.DISABLED)  #make it read-only, no manipulation from user end

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

    #draw disks on pegs, scale disk size based on number of disks
    #calculate max disk width to prevent mishappening of disks when there are many disks
    max_width = 90  # Maximum width a disk can have
    base_width = max_width / num_disks if num_disks > 0 else 20
    
    for peg in pegs:
        stack = pegs[peg]       # the list of disks in this stack
        for level in range(len(stack)):
            disk = stack[level]
            x = peg_X[peg]  # center of each peg
            # scale disk width based on disk size and number of disks
            half = base_width*disk / 2
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

    #as pegs move, next steps on right side are highlighted in yellow
    moves_text.config(state=tk.NORMAL)
    moves_text.tag_remove("highlight", "1.0", tk.END)
    current_line = f"{step_count}.0"
    moves_text.tag_add("highlight", current_line, f"{step_count}.end")
    moves_text.tag_config("highlight", background="yellow")
    #moves_text.see(current_line)  #scroll to show current move
    moves_text.config(state=tk.DISABLED)

    draw_game()        #redraw board at new state


#add button
button = tk.Button(root, text = "Next Move!", command = next_step)
button.place(x=20, y=110)

draw_game()

#keeping the window open, make sure this line ALWAYS stays at the bottom of the code
root.mainloop()
