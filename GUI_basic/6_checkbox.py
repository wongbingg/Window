from tkinter import *

root = Tk()
root.title("Wong GUI")
root.geometry("640x480+400+100") #가로x세로
chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기",variable=chkvar)

chkbox.pack()
chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지않기",variable =chkvar2)
chkbox2.pack()
def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root,text="클릭",command = btncmd)
btn.pack()

root.mainloop()