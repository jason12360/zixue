from tkinter import *
import os
def callback():
	print('called the callback')

root = Tk()
#创建多个窗口
# top = Toplevel()

# #示例menu用法——————————————————————————————————————————————————————
# menu = Menu(root)
# root.config(menu = menu)
# filemenu = Menu(menu)
# menu.add_cascade(label ='File',menu = filemenu)
# filemenu.add_command(label = 'New',command = callback)
# filemenu.add_command(label = 'Open...',command = callback)
# filemenu.add_separator()
# filemenu.add_command(label = 'Exit',command=callback)

# helpmenu = Menu(menu)
# menu.add_cascade(label = 'Help',menu = helpmenu)
# helpmenu.add_command(label = 'About...',command = callback)

#示例使用button和frame完成工具栏模型——————————————————————————————————————
# toolbar = Frame(root)
# b = Button(toolbar,text ='new',width = 6,command =callback)
# b.pack(side = LEFT,padx=2,pady=2)

# b = Button(toolbar,text = 'open',width = 6,command = callback)
# b.pack(side=LEFT,padx =2,pady =2)
# toolbar.pack(side = TOP,fill=X)

# status = Label(root,text = 'gonndljlkajsdkl',bd =1,relief = SUNKEN,anchor = W)
# status.pack(side = BOTTOM,fill =X)

#创建自己的Dialog窗口
# class MyDialog:
# 	def __init__(self,parent):
# 		self.top = Toplevel(parent)
# 		top = self.top
# 		Label(top,text = 'Value').pack()

# 		self.e = Entry(top)
# 		self.e.pack(padx = 5)

# 		b = Button(top,text='OK',command=self.ok)
# 		b.pack(pady =5)
# 	def ok(self):
# 		print('value is',self.e.get())
# 		self.top.destroy()

# Button(root,text='Hello').pack()
# root.update()
# d = MyDialog(root)
# root.wait_window(d.top)

#使用继承创建Dialog类——————————————————————————————————————————————————————

class Dialog(Toplevel):
	def __init__(self,parent,title = None):
		super().__init__(parent)
		self.transient(parent)

		if title:
			self.title(title)
		self.parent = parent
		self.result = None
		body = Frame(self)
		self.initial_focus = self.body(body)
		body.pack(padx = 5,pady = 5)
		self.buttonbox()
		self.grab_set()
		if not self.initial_focus:
			self.initial_focus = self
		self.protocol('WM_DELETE_WINDOW',self.cancel)
		self.geometry('+%d+%d'%(parent.winfo_rootx()+50,parent.winfo_rooty()+50))
		self.initial_focus.focus_set()
		self.wait_window(self)
	def body(self,master):
		pass
	def buttonbox(self):
		box = Frame(self)
		w = Button(box,text= 'OK',width =10,command=self.ok,default = ACTIVE)
		w.pack(side=LEFT,padx = 5,pady = 5)
		w = Button(box,text= 'Cancel',width =10,command=self.cancel)
		w.pack(side = LEFT,padx =5,pady = 5)

		self.bind('<Return>',self.ok)
		self.bind('<Escape>',self.cancel)
		box.pack()
	def ok(self,event = None):
		if not self.validate():
			self.initial_focus.focus_set()
			return
		self.withdraw()
		self.update_idletasks()
		self.apply()
		self.cancel()
	def cancel(self,event = None):
		self.parent.focus_set()
		self.destroy
	def validate(self):
		return 1
	def apply(self):
		pass

class MyDialog(Dialog):
	def body(self,master):
		Label(master,text='用户名：').grid(row = 0)
		Label(master,text='密码：').grid(row = 1)

		self.e1 = Entry(master)
		self.e2 = Entry(master)

		self.e1.grid(row = 0,column =1)
		self.e2.grid(row = 1,column = 1)
		return self.e1

	def apply(self):
		username = self.e1.get()
		password = self.e2.get()
		print(username,password)

Button(root, text="Hello!").pack()
root.update()

d = MyDialog(root)
root.wait_window(d.parent)
# root.mainloop()
