import json

filename = 'user_fav_nums.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, "+ username +"!")