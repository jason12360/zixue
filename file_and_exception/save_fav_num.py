import json

filename = 'user_fav_nums.json'
username = input('请输入您的用户名')
with open(filename,'w') as file_object:
    json.dump(username,file_object)
    print("We'll remember you when you come back " + username + "!")

