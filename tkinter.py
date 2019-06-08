'''
tkinter
    --desktop application package
'''

# creating a wimdow

from tkinter import *
root=Tk()
root.mainloop()

'''
Tk()-- which contain the window
mainloop()--stays the window untill the user close the window
'''

#size of the window

from tkinter import *
root=Tk()
root.geometry("500x500")
root.mainloop()

#geometry-- gives the default size of the window

#title and icon

from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Cracy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
root.mainloop()

#creating the label of text and image

from tkinter import *
root=Tk()
root.geometry("500x500")

root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
la=Label(root,text="lovely anna")
la.pack()
photo=PhotoImage(file="output.png")
la1=Label(root,image=photo)
la1.pack()
root.mainloop()

'''
label contain two parameters
    -- where we want to place the label  (root--inside the window)
    --the label contains text or image
PhotoImage
    --contain the image path or file
pack()
    --the function used to place the required in the window
'''

#creating the button of text and image

from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
def button():
    print("love the Crazy Programmer")
but=Button(root,text="click me",command=button)
but.pack()
photo=PhotoImage(file="output.png")
butt=Button(root,image=photo,command=button)
butt.pack()
root.mainloop()

'''
button contain three parameters
    -- where we want to place the label  (root--inside the window)
    --the label contains text or image
    --contain the function to be called
'''

'''
menu bar
    --first we create the menu bar
    -- then we create the submenu(file,edit)
    --then cascade the menu(new,cut)
cascade
    -- label and menu()
command
    --label
'''

from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
mbar=Menu(root)
root.config(menu=mbar)      # menu bar is created
smenu=Menu(mbar,tearoff=0)
mbar.add_cascade(label="File",menu=smenu)
smenu.add_command(label="open")
smenu.add_command(label="exit")
ssmenu=Menu(mbar,tearoff=0)
mbar.add_cascade(label="Edit",menu=ssmenu)
ssmenu.add_command(label="cut")
ssmenu.add_command(label="copy")
sssmenu=Menu(mbar,tearoff=0)
mbar.add_cascade(label="help",menu=sssmenu)
sssmenu.add_command(label="about us")
root.mainloop()

'''
functionality in menu bar

filedialog
    --contain all file information
'''
from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("500x500")
root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
mbar=Menu(root)
root.config(menu=mbar)      # menu bar is created
smenu=Menu(mbar,tearoff=0)
def fo():
    filename=filedialog.askopenfilename()
    print(filename)
mbar.add_cascade(label="File",menu=smenu)
smenu.add_command(label="open",command=fo)
smenu.add_command(label="exit",command=root.destroy)
root.mainloop()

'''
messagebox
    -- from the library messagebox
    --showinfo -- contain 2 parameter 
        --title of the message box
        --content of the message box
    --showinfo,showerror,showwaring differ in their symbol
'''

from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("500x500")
root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
def button():
    tkinter.messagebox.showinfo("crazy","hi buddy")
    tkinter.messagebox.showerror("error","file not found")
    tkinter.messagebox.showwarning("warning","try to be safe")
but=Button(root,text="click me",command=button)
but.pack()
root.mainloop()

'''
statusbar
    --present at the bottom
anchor
    --show the text left side of the window
fill
    --show the text x direction(horizontal) of the window
'''

from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Crazy Programmer")
root.iconbitmap(r"C:\Users\lenovA\Desktop\12.ico")
sbar=Label(root,text="love u anna", relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)
root.mainloop()


'''
pack and grid cannot be used at the same time but it is exception in frames
grid --ex excel
pad
    --padding -> space between the elements
    -- x - >horizontal
    -- y - >vertical
'''
#pack

from tkinter import *
root=Tk()
root.geometry('300x300')
middleframe=Frame(root)
middleframe.pack()
pphoto=PhotoImage(file="2.png")
pbtn=Button(middleframe,image=pphoto)       #button
pbtn.pack(side=LEFT,padx=10,pady=20)
sphoto=PhotoImage(file="3.png")
sbtn=Button(middleframe,image=sphoto)
sbtn.pack(side=LEFT,padx=10,pady=20)
pauphoto=PhotoImage(file="4.png")
pb=Button(middleframe,image=pauphoto)
pb.pack(side=LEFT,padx=10,pady=20)
root.mainloop()


#grid


from tkinter import *
root=Tk()
middleframe=Frame(root)
middleframe.pack()
pphoto=PhotoImage(file="2.png")
pbtn=Button(middleframe,image=pphoto)       #button
pbtn.grid(row=0,column=0,padx=10)
sphoto=PhotoImage(file="3.png")
sbtn=Button(middleframe,image=sphoto)
sbtn.grid(row=0,column=1,padx=10)
pauphoto=PhotoImage(file="4.png")
pb=Button(middleframe,image=pauphoto)
pb.grid(row=0,column=2,padx=10)
root.mainloop()

'''
text area and font attribute
Text(root)-->create the text area
font contain fony\t family and font size

if u want to give font family alone-->font=("")
if u want to give font size alone-->font(False,20)
'''

from tkinter import *
root=Tk()
text=Text(root,height=60,width=60,font=("Arial",20),foreground="blue",background="black")
text.pack()
root.mainloop()

'''
text.get()-- used to get the text
'''

'''
entry widgets
    --single line text 
    --ENTRY-->used to create the entry loop
'''

from tkinter import *
root=Tk()
la=Label(root,text="uname")
la.pack(side=LEFT)
e=Entry(root)
e.pack(side=LEFT)
root.mainloop()

#scroll bar

from tkinter import *
root=Tk()
text=Text(root,height=70,width=1250,font=("Arial",10))
scrbar=Scrollbar(root,command=text.yview,width=15)
scrbar.config(command=text.yview)
text.config(yscrollcommand=scrbar.set)
scrbar.pack(side=RIGHT,fill=Y)
text.pack()
root.mainloop()
