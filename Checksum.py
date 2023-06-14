# filepath = r"D:\Home\Noman\Paper\PaperFormattedUpdated.pdf"
def check():
    if (input_hash.get().strip() == md5_hash):
        # ttk.Label(frame1, text=" Given Hash is CORRECT  ").grid(row=4, column=1)
        decision.set("Given Hash is CORRECT")
        print("Given Hash is CORRECT")
    else:
        # ttk.Label(frame1, text="Given Hash is INCORRECT ").grid(row=4, column=1)
        decision.set("Given Hash is INCORRECT")
        print("Given Hash is INCORRECT")

def open_file():
    file = filedialog.askopenfile(filetypes=[('All Files', "*.*")])
    text.insert(0, file.name)
    # Calculating MD5
    global md5_hash
    md5_hash = md5(open(file.name, "rb").read()).hexdigest()
    ttk.Label(frame1, text="MD5 Checksum of File:").grid(row=2,column=0)
    ttk.Label(frame1, text=md5_hash).grid(row=2, column=1, sticky="w")
    print(md5_hash)

from hashlib import md5, sha256
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar


window = tk.Tk()
window.title("MD5 Checksum")
window.geometry("480x360")
window.resizable(False, False)

frame1 = tk.Frame(window)
frame1.place(x=30, y=150)

ttk.Label(frame1, text="Enter File Path").grid(row=0, column=0)
text = tk.Entry(frame1, width=40)
text.grid(row=0, column=1)
ttk.Button(frame1, text="Browse", command=open_file).grid(row=0, column=2)

# Checking with user given hash
ttk.Label(frame1, text="Compare Against:").grid(row=1, column=0)
input_hash = tk.Entry(frame1, width=40)
input_hash.grid(row=1, column=1)
ttk.Button(frame1, text="Compare", command=check).grid(row=1, column=2)
decision = StringVar()
decision.set("")
ttk.Label(frame1, textvariable=decision).grid(row=4, column=1)

window.mainloop()