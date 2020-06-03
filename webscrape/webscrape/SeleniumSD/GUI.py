import tkinter as tk
from tkinter.ttk import Progressbar
from webscrape.webscrape.SeleniumSD.automate_servicedesk import AutoSD # importing my own script class
import threading
import asyncio
import time


# Controlled by start_submit_thread
def submit():
    print('It is running')
    bot = AutoSD()
    bot.main()

    #text1.insert(tk.INSERT, "Done")

def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True
    progressbar.start()
    submit_thread.start()
    window.iconify()
    window.after(20, check_submit_thread)

def check_submit_thread():
    if submit_thread.is_alive():
        window.after(20, check_submit_thread)
    else:
        #progressbar.stop()
        progressbar.stop()

def close_app():
    window.destroy()

def print_val():
    print(inputDc_entry.get())


window = tk.Tk()
window.title('CSI Quick Tools')
window.geometry("420x600")
window.resizable("false", "false") # (hor, ver.)


# Splitting the window in 3 zones
frame_header = tk.Frame(window, borderwidth=2, pady=2, bg="#263D42")
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

# Attributing them to grid
frame_header.grid(row=0, column=2)
center_frame.grid(row=1, column=2)
bottom_frame.grid(row=2, column=2)

# Header
header = tk.Label(frame_header, text="Other Tools", bg="grey", fg="black", height="1", width="34", font={"Helvetica 14 bold"})
header.grid(row="0", column="0")

# Center frame split into two frames
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief="sunken")
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief="sunken")

#Bottom frame too
frame_bottom_1 = tk.Frame(bottom_frame, borderwidth=2)
frame_bottom_2 = tk.Frame(bottom_frame, borderwidth=2)
frame_bottom_3 = tk.Frame(bottom_frame, borderwidth=2)

# First row - Domain Controller
inputDc = tk.Label(frame_main_1, text="Domain Controller ")
inputDc_StringVar = tk.StringVar()
inputDc_entry = tk.Entry(frame_main_1, textvariable=inputDc, width="25") # this is what holds data
inputDc_entry.insert(0, 'e.g masthaven niuadmin')
domainController_button = tk.Button(frame_main_1, text="Open", command=print_val, bg="dark green", fg="white", relief="raised", width="10", font={"Helvetica 10 bold"})

# VDI Broker
vdiBroker = tk.Label(frame_main_2, text="VDI Broker")
vdiBroker_StringVar = tk.StringVar()
vdiBroker_entry = tk.Entry(frame_main_2, textvariable=vdiBroker, width="33") # this is what holds data
vdiBroker_entry.insert(0, 'e.g cambridge')
vdiBroker_button = tk.Button(frame_main_2, text="Open", command=print_val, bg="dark green", fg="white", relief="raised", width="10", font={"Helvetica 10 bold"})




# Bottom row Frame1 - Buttons
groupUnassigned = tk.Button(frame_bottom_1, text="Group Unassigned", command=submit, bg="orange", fg="white", relief="raised", width="15", font={"Helvetica 10 bold"})
groupUnassigned.grid(row=2, column=0, sticky="w", padx=5, pady=2)

myTickets = tk.Button(frame_bottom_1, text="My Tickets", command=print_val, bg="orange", fg="white", relief="raised", width="15", font={"Helvetica 10 bold"})
myTickets.grid(row=2, column=1, sticky="w", padx=5, pady=2)

# Bottom row Frame2 - Text Box
text1 = tk.Text(frame_bottom_2, height=10, width=34)
text1.config(state="disabled")



#Packing the things visually
frame_main_1.pack(fill="x", pady="2")
frame_main_2.pack(fill="x", pady="2")

inputDc.pack(side="left", padx="5")
inputDc_entry.pack(side="left", padx="5")
domainController_button.pack(side="left", padx="2")

vdiBroker.pack(side="left", padx="5")
vdiBroker_entry.pack(side="left", padx="5")
vdiBroker_button.pack(side="left", padx="2")

frame_bottom_1.pack(fill="x", pady="2") # add the row-cell size of 1
frame_bottom_2.pack(fill="x", pady="2")
frame_bottom_3.pack(fill="x", pady="2")

text1.pack()# without .pack() there is no render on screen


progressbar = Progressbar(frame_bottom_3, mode='indeterminate', length=100)
progressbar.grid(column=1, row=0, sticky="w")

tk.Button(frame_bottom_3, text="Group Unassigned", command=lambda: start_submit_thread(None)).grid(column=0, row=1, sticky="E") # this is how you call function on a separate thread
tk.Button(frame_bottom_3, text="Group Unassigned", command=lambda: start_submit_thread(None)).grid(column=0, row=2, sticky="E") # this is how you call function on a separate thread


window.mainloop() # End

