from tkinter import *

root = Tk()

def key(event):

	print('pressed',repr(event.char))
#使用button-1event
def callback(event):
	frame.focus_set()
	print('click at',event.x,event.y)


frame = Frame(root,width = 100,height = 100)
#为button-1事件绑定callback
frame.bind('<Key>',key)
frame.bind('<ButtonRelease-1>',callback)
frame.pack()

root.mainloop()