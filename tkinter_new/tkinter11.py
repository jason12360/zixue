import tkinter as tk

class Mybutton(tk.Label):
	def __init__(self,master,fun,**kwargs):
		super().__init__(master,kwargs)
		self.fun = fun
		self.config(fg = '#555555')
		self.config(bg = '#F8F8FF')
		self.bind('<Button-1>',self.fun_button1)
		self.bind('<ButtonRelease-1>',self.fun_br1)
		self.bind('<Enter>',self.fun_enter)
		self.bind('<Leave>',self.fun_leave)
	def fun_enter(self,event):
		self.config(bg = '#32CD32')
		self.config(fg = '#FFFFFF')
	def fun_leave(self,event):
		self.config(bg = '#F8F8FF')
		self.config(fg = '#555555')
	def fun_button1(self,event):
		self.config(relief = tk.SUNKEN)
		self.fun()
	def fun_br1(self,event):
		self.config(relief = tk.FLAT)

class Myentry(tk.Entry):
	def __init__(self,master,**kwargs):
		super().__init__(master,kwargs)
		self.config(highlightcolor = '#32CD32',highlightthickness = 2,bd = 0.5,relief = tk.FLAT,highlightbackground='#CCCCCC')
def fun1():
	print('hahahhah')
top = tk.Tk()
top.geometry('400x500')
l = tk.Label(text = '用户名:',anchor = tk.W,width = 20,height =1,fg = '#555555')
l.pack()
e = Myentry(top)
e.pack()
e.focus_set()
l = tk.Label(text = '密码:',anchor = tk.W,width = 20,height =1,fg = '#555555')
l.pack()
e = Myentry(top)
e.pack()
b = Mybutton(top,fun1,text = '登录',width = 15,height =2)
b.pack(pady = 10)

top.wm_title('菜单')
top.mainloop()