import json
def get_stored_fav_nums():
    filename='fav_num.json'
    try:
        with open(filename) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num 
def get_new_fav_nums():
    filename='fav_num.json'
    fav_num = input('请输入您最喜爱的数字')
    with open(filename,'w') as f_obj:
        json.dump(fav_num,f_obj)
    return fav_num

def show_fav_num(): 
    user_input = input('请输入您最喜爱的数字：')   
    fav_num = get_stored_fav_nums()
    if fav_num != user_input:
        print('您输入的数字和我记得的不一样，请重新输入您喜爱的数字')
        fav_num = get_new_fav_nums()
        print('我已经记住你最喜欢的数字是 '+ fav_num + '!')
    else:
        print('您最喜爱的数字我记得是 ' + fav_num +'!' )

show_fav_num()