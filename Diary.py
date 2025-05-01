from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

def submit():
    input = text.get("1.0",END)
    print(input)

def openFile():
    file_path = filedialog.askopenfilename(initialdir="// Put your directory link here!",
                                           title="File Explorer",
                                           filetypes=(("Text files", "*.text"),
                                                      ("All files", "*.*")))
    file = open(file_path, 'r')
    print(file.read())
    file.close()
    print("File opened!")

def saveFile():
    file = filedialog.asksaveasfile(initialdir="// Put your directory link here!",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                        ("Microsoft pdf document", ".pdf")
                                    ])
    filetext = str(text.get(1000000, END))
    file.write(filetext)
    print("File saved!")
    file.close()

def cut():
    print("Cut some text!")

def copy():
    print("Copied some text!")

def paste():
    print("Pasted some text!")

def save():
    print("Saved some text!")


window = Tk()

text = Text(window,
            bg="White",
            font=('Calibri', 15),
            height=1000,
            width=200,
            padx=10,
            pady=10,
            fg="Blue")

text.pack()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Bahnschrift", 10))
menubar.add_cascade(label="FILE", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("Elegant", 10))
menubar.add_cascade(label="EDIT", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

button1 = Button(text='save', command=saveFile)
button2 = Button(text='open', command=openFile)
button3 = Button(text='cut', command=cut)
button4 = Button(text='open', command=copy)
button5 = Button(text='open', command=paste)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

percent = StringVar()
text = StringVar()

window.geometry('1000x1000')
window.title('AFJ Diaries')
window.config(background='BLACK')

window.mainloop()
