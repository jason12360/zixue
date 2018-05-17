myfile = open('todo.txt','a')
print('这是第一行' ,file = myfile)
print('这是第二行' ,file = myfile)
print('这是第三行' ,file = myfile)
myfile.close()

read = open('todo.txt')
for i in read:
    print(i)
read.close