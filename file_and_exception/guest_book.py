filename = 'guest.book.txt'
while 1:
    s = input('请输入名字')
    with open(filename,'a') as file_object:
        file_object.write(s+'\n')
