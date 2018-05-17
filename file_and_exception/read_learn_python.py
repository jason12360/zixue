filename = 'learn_python.txt'
l = []
# with open(filename) as file_object:
#     print(file_object.read())
#     file_object.close
# with open(filename) as file_object:    
#     for line in file_object:
#         print(line)
#     file_object.close
with open(filename) as file_object:
    l = file_object.readlines()
    file_object.close
for i in l:
    s = i.replace('Python','C')
    print (s)
