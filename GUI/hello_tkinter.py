import tkinter as tk
from PIL import Image,ImageTk




#创建Tk对象
root = tk.Tk()
image = Image.open('buttons.jpg')
#创建图片对象
photo = ImageTk.PhotoImage(image)
#创建label对象
w = tk.Label(root,image = photo)
w.pack()
root.mainloop()