class Restaurant(object):
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 11
    def describe_restaurant(self):
        print(self.restaurant_name,self.cuisine_type)
    def open_restaurant(self):
        print('餐厅正在营业')
    def set_number_served(self,n):
        self.number_served = n
    def increment_number_served(self,n):
        self.number_served += n

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def describe_icecream(self):
        print(self.flavors)

hagengdasi = IceCreamStand('哈更达斯','冰激凌','草莓味')
hagengdasi.describe_restaurant()
hagengdasi.describe_icecream()



# waipojia = Restaurant('外婆家','杭帮菜')
# waipojia.describe_restaurant()
# waipojia.open_restaurant()
# bingsheng = Restaurant('炳胜','粤菜')
# qiaojiangnan = Restaurant('俏江南','川菜')
# bingsheng.describe_restaurant()
# qiaojiangnan.describe_restaurant()
# waipojia.set_number_served(10)
# waipojia.increment_number_served(10)
# print(waipojia.number_served)