import tkinter as tk
from webscrape.webscrape.SeleniumSD.automate_servicedesk import AutoSD # importing my own script class

def close_app():
    window.destroy()

def print_val():
    print(inputDc_entry.get())

def run_app():
    print('It is running')
    bot = AutoSD()
    bot.main()



window = tk.Tk()
window.title('CSI Quick Tools')
window.geometry("600x600")
window.resizable("true", "false") # (hor, ver.)

# Splitting the window in 3 zones
frame_header = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

# Attributing them to grid
frame_header.grid(row=0, column=0)
center_frame.grid(row=1, column=0)
bottom_frame.grid(row=2, column=0)

#header = tk.Label(frame_header, text="Something", bg="grey", fg="black", height="3", width="20", font={"Helvetica 18 bold"})
#header.grid(row="0", column="0")

# DC Frame and its display
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief="sunken")

# DC Label and its display
inputDc = tk.Label(frame_main_1, text="Domain Controller ")
inputDc_StringVar = tk.StringVar()
inputDc_entry = tk.Entry(frame_main_1, textvariable=inputDc, width="25") # this is what holds data
inputDc_entry.insert(0, 'e.g masthaven niuadmin')

# Button 1
button_run = tk.Button(frame_main_1, text="Open", command=print_val, bg="dark green", fg="white", relief="raised", width="10", font={"Helvetica 10 bold"})

# Button 2
button_run1 = tk.Button(bottom_frame, text="Group Unassigned", command=run_app, bg="orange", fg="white", relief="raised", width="15", font={"Helvetica 10 bold"})
button_run1.grid(column=0, row=1, sticky="w", padx=5, pady=2)

# Button 2
button_run2 = tk.Button(bottom_frame, text="My Tickets", command=run_app, bg="orange", fg="white", relief="raised", width="15", font={"Helvetica 10 bold"})
button_run1.grid(column=0, row=1, sticky="w", padx=5, pady=2)

#Packing the things visually
frame_main_1.pack(fill="x", pady="2")
inputDc.pack(side="left", padx="5")
inputDc_entry.pack(side="left", padx="5")
button_run.pack(side="left", padx="2")

window.mainloop() # End

