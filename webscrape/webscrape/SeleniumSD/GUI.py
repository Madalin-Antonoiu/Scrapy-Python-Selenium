import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar
from webscrape.webscrape.SeleniumSD.automate_servicedesk import AutoSD  # importing my own script class
import threading
import asyncio
import time
import subprocess


def text(index, string):
    # I do all 3 so it stays disabled again like default after inserting
    text1.configure(state='normal')
    text1.insert(index, string)
    text1.configure(state='disabled')


# Controlled by start_submit_thread
def submit():
    row = groupUnassigned_entry.get() # previously hardcoded '0', now gets value from input field
    print('Script running...')

    text(0.0, '\n \n ')
    text(1.0, '---- Group Unassigned, row:' + ' ' + row + '----' + '\n')
    text(2.0, 'Script running...' + '\n')
    progressbar.grid(column=0, row=0, sticky="w")  # Start showing the progress bar
    window.iconify() # you can remove it or put it someweherelse
    bot = AutoSD()
    output = bot.main(row)  # return from main function, pass it the row number

    text(3.0, '====================================' + '\n')
    text(4.0, output + '\n')
    text(5.0, '====================================' + '\n')
    text(6.0, 'Script ended.      '
              '                 ' + '\n ')
    progressbar.grid_forget()  # Hide the progress bar


def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=event)
    submit_thread.daemon = True
    progressbar.start()
    submit_thread.start()
    window.after(20, check_submit_thread)


def check_submit_thread():
    if submit_thread.is_alive():
        window.after(20, check_submit_thread)
    else:
        # progressbar.stop()
        progressbar.stop()


def close_app():
    window.destroy()


def print_val():
    print(inputDc_entry.get())  # gets the value from inputDc input field from user
    text1.insert(0.0, "Shazaam")

def hello():
    text(0.0, "hello!")

def open_logs():
    # filename = askopenfilename(parent=window) # this is how you open File Explorer
    import os
    os.system('C:\\Users\\antonoium\\Desktop\\venv\\webscrape\\webscrape\\SeleniumSD\\logs.txt') # this is how you open a file directly


window = tk.Tk()
window.title('CSI Quick Tools')
window.geometry("440x660")
window.resizable("true", "true")  # (hor, ver.)
window.columnconfigure(0, weight=1)
window.rowconfigure(2, weight=1)

#Menu bar
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Logs", command=lambda: start_submit_thread(open_logs))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)


# Splitting the window in 2 zones
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)

# Attributing them to grid
center_frame.grid(row=0, column=0, sticky='n')
bottom_frame.grid(row=1, column=0, sticky='s')

# Header
header = tk.Label(center_frame, text="Other Tools", bg="grey", fg="black", height="1", width="34", font={"Helvetica 14 bold"})
header.pack(fill="x", pady="20 0")

# Center frame split into two frames

frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief="sunken")
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief="sunken")
frame_main_3 = tk.Frame(center_frame, borderwidth=2, relief="sunken")
frame_main_4 = tk.Frame(center_frame, relief="sunken")
frame_main_5 = tk.Frame(center_frame, borderwidth=2)


# First row - Domain Controller
inputDc = tk.Label(frame_main_1, text="Domain Controller ")
inputDc_StringVar = tk.StringVar()
inputDc_entry = tk.Entry(frame_main_1, textvariable=inputDc, width="25")  # this is what holds data
inputDc_entry.insert(0, 'e.g masthaven niuadmin')
domainController_button = tk.Button(frame_main_1,
                                    text="Open",
                                    command=print_val,
                                    bg="dark green",
                                    fg="white",
                                    relief="raised",
                                    width="10",
                                    font={"Helvetica 10 bold"})

# VDI Broker
vdiBroker = tk.Label(frame_main_2, text="VDI Broker")
vdiBroker_StringVar = tk.StringVar()
vdiBroker_entry = tk.Entry(frame_main_2, textvariable=vdiBroker, width="33")  # this is what holds data
vdiBroker_entry.insert(0, 'e.g cambridge')
vdiBroker_button = tk.Button(frame_main_2,
                             text="Open",
                             command=print_val,
                             bg="dark green",
                             fg="white",
                             relief="raised",
                             width="10",
                             font={"Helvetica 10 bold"})

# Group Unassigned
groupUnassigned = tk.Label(frame_main_3, text="Group Unassigned")
groupUnassigned_StringVar = tk.StringVar()
groupUnassigned_entry = tk.Entry(frame_main_3, textvariable=groupUnassigned, width="18")
groupUnassigned_entry.insert(0, '0')
groupUnassigned_button = tk.Button(frame_main_3,
                                   text="Assign Row",
                                   command=lambda: start_submit_thread(submit),
                                   bg="orange",
                                   fg="white",
                                   relief="raised",
                                   width="15",
                                   font={"Helvetica 10 bold"})

text1 = tk.Text(frame_main_4,  bg="gray", fg="black", wrap="word", state='disabled')


# Packing the things visually
# here you define padding from frame to frame
frame_main_1.pack(fill="x", pady="2")
frame_main_2.pack(fill="x", pady="2")
frame_main_3.pack(fill="x", pady="2")
frame_main_4.pack(fill="both", expand = True)
frame_main_5.pack(fill="x", pady="2")

inputDc.pack(side="left", padx="5", expand=False)
inputDc_entry.pack(side="left", padx="5", expand=False)
domainController_button.pack(side="left", padx="2", expand=False)

vdiBroker.pack(side="left", padx="5", expand=False)
vdiBroker_entry.pack(side="left", padx="5", expand=False)
vdiBroker_button.pack(side="left", padx="2", expand=False)

groupUnassigned.pack(side="left", padx="5", expand=False)
groupUnassigned_entry.pack(side="left", padx="5", expand=False)
groupUnassigned_button.pack(side="left", padx="2", expand=False)

text1.pack(side="left", expand = True)  # without .pack() there is no render on screen
progressbar = Progressbar(frame_main_5, mode='indeterminate', length=100)

#tk.Button(bottom_frame, text="Open Logs", command=lambda: start_submit_thread(None)).grid(column=0, row=0, sticky="S") # sticky is cardinal points

window.config(menu=menubar)
window.mainloop()  # End


# model, don't delete # tk.Button(frame_bottom_3, text="Group Unassigned", command=lambda: start_submit_thread(None)).grid(column=0, row=2, sticky="E") # this is how you call function on a separate thread
# tk.Button(frame_bottom_3, text="Tickets Number Dropdown", command=lambda: start_submit_thread(None)).grid(column=0, row=2, sticky="E") # this is how you call function on a separate thread
