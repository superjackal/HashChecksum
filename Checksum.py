# filepath = r"D:\Home\Noman\Paper\PaperFormattedUpdated.pdf"
def check():
    if (input_hash.get().strip() == hash_text):
        decision.set("Given Hash is CORRECT")
    else:
        decision.set("Given Hash is INCORRECT")

def hash_file(e):
    hash_type = hash_box.get()
    file = text.get().encode("unicode_escape")
    global hash_text
    if hash_type == "SHA-1":
        hash_text = sha1(open(file, "rb").read()).hexdigest()
    elif hash_type == "SHA-224":
        hash_text = sha224(open(file, "rb").read()).hexdigest()
    elif hash_type == "SHA-256":
        hash_text = sha256(open(file, "rb").read()).hexdigest()
    elif hash_type == "SHA-384":
        hash_text = sha384(open(file, "rb").read()).hexdigest()
    elif hash_type == "SHA-512":
        hash_text = sha512(open(file, "rb").read()).hexdigest()
    elif hash_type == "MD5":
        hash_text = md5(open(file, "rb").read()).hexdigest()
    else:
        return
    if len(hash_text) > 64:
        hash_text = hash_text[:65] + "\n" + hash_text[65:]
    ttk.Label(frame1, text="Checksum of File:").grid(row=2,column=0)
    ttk.Label(frame1, text=hash_text).grid(row=2, column=1, sticky="w")
    print(hash_text)

def open_file_and_hash():
    file = filedialog.askopenfile(filetypes=[('All Files', "*.*")])
    text.insert(0, file.name)

from hashlib import md5, sha1, sha256, sha224, sha384, sha512
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar


window = tk.Tk()
window.title("MD5 Checksum")
window.geometry("640x360")
window.resizable(False, False)

frame1 = tk.Frame(window)
frame1.place(x=30, y=150)

ttk.Label(frame1, text="Enter File Path").grid(row=0, column=0)
text = tk.Entry(frame1, width=40)
text.grid(row=0, column=1)
ttk.Button(frame1, text="Browse", command=open_file_and_hash).grid(row=0, column=2)

ttk.Label(frame1, text="Choose Hash").grid(row=1, column=0)
hash_name = StringVar()
hash_box = ttk.Combobox(frame1, textvariable=hash_name)
hash_box['values'] = ("SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512", "MD5")
hash_box.grid(row=1, column=1)
hash_box.bind("<<ComboboxSelected>>", hash_file)
# ttk.Button(frame1, text="Hash", command=hash_file).grid(row=1, column=2)

# Checking with user given hash
ttk.Label(frame1, text="Compare Against:").grid(row=3, column=0)
input_hash = tk.Entry(frame1, width=40)
input_hash.grid(row=3, column=1)
ttk.Button(frame1, text="Compare", command=check).grid(row=3, column=2)
decision = StringVar()
decision.set("")
ttk.Label(frame1, textvariable=decision).grid(row=4, column=1)

window.mainloop()