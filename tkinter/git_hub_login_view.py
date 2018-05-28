from tkinter import *
from PIL import Image,ImageTk

class Login_view(Frame):
	def __init__(self,parent):
		super().__init__(parent)
	#	b = Button(self,text='OK')
		# load = Image.open('buttons.jpg')
		# render = ImageTk.PhotoImage(load)
		# b = Button(self, image=render)
		# b.pack()


root = Tk()
root.geometry('400x500')
load = Image.open('button.png')
# load = load.crop((140,70,658,266)).resize((60,30))

render = ImageTk.PhotoImage(load)

b = Button(root, image=render)
b.pack()
# log = Login_view(root)
# log.pack()
mainloop()