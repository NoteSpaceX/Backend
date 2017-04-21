from Tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile



# global variable
filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    global filename
    # number on the left is the line, on the right is column
    t = text.get(0.0, END)
    f  = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    # allows us not to cut out the white space
    f.write(t.rstrip())

    # try:
    #     #allows us not to cut out the white space
    #     f.write(t.rstrip())
    #
    # except:
    #     # showerror(title="Oops!", message="Unable to save file")

def openFile():
    f  =askopenfile(mode='r')
    t  = f.read
    text.delete(0.0, END)
    text.insert(0.0, t)

#tk object main window
root = Tk()
root.title("My Python Text editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
Text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="SaveAs", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", commmand=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

