filename = 'guest.txt'
s = input('请输入用户名： ')
with open(filename,'w') as file_object:
    file_object.write(s)