import tkinter as tk 
import time 

root = tk.Tk()

root.geometry("250x250+1570+10")

root.title("StopWatch")

root.overrideredirect(True)     # Frameless window

root.attributes("-topmost", True)  # Always stays on top

root.bind("<Escape>", lambda e: root.destroy())

time_var = tk.StringVar()
time_var.set("00:00:00:00")

label = tk.Label(root, textvariable= time_var, font = ("Arial", 20), fg = "lime", bg = "black")
label.pack(expand=True, fill="both")

Start_Time = None 
running = False 

def isrunning():
    if running: 
        elapsed = time.time() - Start_Time
        total_seconds = int(elapsed)

        minutes = total_seconds // 60 
        secs = total_seconds % 60

        hrs = minutes // 60
        mins = minutes % 60

        ms = int((elapsed - int(elapsed)) * 100)  # milliseconds (2 digits)

        time_var.set(f"{hrs:02}:{mins:02}:{secs:02}.{ms:02}")
    
    root.after(50, isrunning)  # update every 50ms

def elapsed_time():
    if Start_Time == None:
        return 0
    return time.time() - Start_Time

def Start():
    global Start_Time,running
    if not running:
        Start_Time = time.time() - elapsed_time()
        running = True 

def Stop():
    global running 
    running = False 

def reset():
    global Start_Time,running
    running = False
    Start_Time = None
    time_var.set("00:00:00:00")


def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", do_move)


        
button_frame = tk.Frame(root, bg="black")
button_frame.pack(fill="x")

tk.Button(button_frame, text="Start", command=Start, width=8).pack(side="left", padx=5, pady=5)
tk.Button(button_frame, text="Stop", command=Stop, width=8).pack(side="left", padx=5, pady=5)
tk.Button(button_frame, text="Reset", command=reset, width=8).pack(side="left", padx=5, pady=5)



        
isrunning()  # Kick off the recursive timer

root.mainloop()