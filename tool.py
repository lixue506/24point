import random
from itertools import permutations

class create_game():

    arr = []
    ops = r'+-*/'

    # 生成随机数
    def get_point(self):
        return [random.randint(1, 11) for i in range(4)]

    def cal(self):
        a,b,c,d = self.arr[0], self.arr[1], self.arr[2], self.arr[3]

    #检验是否有机解
    def inspection(self):
        return {"num":[1,11,2,1],"result":"11*2+1+1"}






