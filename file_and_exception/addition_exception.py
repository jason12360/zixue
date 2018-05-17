
while 1:
    s1 = input('请输入第一个数字')
    s2 = input('请输入第二个数字')    
    try:
        n1 = int(s1)
        n2 = int(s2)
    except ValueError:
        print('您输入的不是数字')
        continue
    else:
        print(n1 + n2)
