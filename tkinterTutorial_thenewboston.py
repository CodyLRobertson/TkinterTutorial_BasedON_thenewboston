#TUTORIAL 1 w/ thenewboston - Introduction

"""
from tkinter import *
root = Tk() #{Equals Blank Window}]
#{Frame = basic squarecontainer that fits within window.}
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
#exampleInstance = #object(#Where, text="#What", fg="#color", ETC.....)
button1 = Button(topFrame, text="Button 1 ", fg="red")
button2 = Button(topFrame, text="Button 2 ", fg="blue")
button3 = Button(topFrame, text="Button 3 ", fg="green")
button4 = Button(bottomFrame, text="Button 4 ", fg="purple")
#pack parameters 
#instance.pack(side=#direction(LEFT))
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
root.mainloop()
"""

#TUTORIAL 2 - Organizing your layout
"""
from tkinter import *
root =Tk()
one = Label(root, text="One", bg="red",fg="white")
two = Label(root, text="two", bg="black",fg="green")
three = Label(root, text="three", bg="blue",fg="white")
one.pack()
two.pack(fill=X)
three.pack(side=LEFT, fill=Y)
root.mainloop()
"""

#TUTORIAL 3/4/5? {3 - Fitting Widgets into Layout ; 4 - Grid Layout ; 5 - More grid layout}
""" 
SCP FOUNDATION GOOF


from tkinter import *
root=Tk()
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
label_3 = Label(root, text="SCP Foundation Database: Employee Terminal", font='Helvetica 18 bold')
label_4 = Label(root, text="Please input Credentials and Clearance Level")
label_5 = Label(root, text="Clearance level (Number Only)")
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
label_1.grid(row=2, column=0, sticky=E)
label_2.grid(row=3, column=0, sticky=E)
entry_1.grid(row=2, column=1)
entry_2.grid(row=3, column=1)
label_3.grid(row=0, columnspan=2)
label_4.grid(row=1, columnspan=2)
entry_3.grid(row=4, column=1)
label_5.grid(row=4, column=0, sticky=E)
c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)
root.mainloop()


"""
#TUTORIAL 6 - Binding functions to layouts
"""

from tkinter import *
root=Tk()
r=root
def printName(event):
	print("Chello my name is Cody!")
button_1 = Button(r, text="Print my Name")
button_1.bind("<Button-1>", printName)
button_1.pack()
r.mainloop()
"""

#TUTORIAL 7 - Mouse Click Events
"""

from tkinter import *
root=Tk()
r = root 
def leftClick(event):
	print("Left")
def RightClick(event):
	print("Right")
def MiddleClick(event):
	print("Middle")
frame = Frame(r, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", MiddleClick)
frame.bind("<Button-3>", RightClick)
frame.pack()
r.mainloop()
"""

#TUTORIAL 8 - Using Classes {in conjunction with Python Programming Tutorial - 29 - Classes and Objects: https://www.youtube.com/watch?v=POQIIKb1BZA&index=29&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_ }
#Must ReDo. A malfunction occured.
#{URL: https://www.youtube.com/watch?v=IYHJRnVOFlw}

from tkinter import *


class CodysButtons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("Wow, This actually worked!")

root = Tk()
b = CodysButtons(root)
root.mainloop()