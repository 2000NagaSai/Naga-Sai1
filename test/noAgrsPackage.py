def dec(fun):
    def inner(*args):
        print('start')
        fun(*args)
        print('end')
    return inner

class dwa:
    def init(self,function):
        self.function=function

    def call(self,*args):
        self.function(*args)




@dec
def fun2(a,b):
    print(f'we will win the soccere WC {a} {b}')
fun2(111,222)







