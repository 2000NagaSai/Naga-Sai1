def dwia(name1,name2,name3):
    print(name1,name2,name3)

    def function(fun):
        def inner(*args):
            print('start')
            fun(*args)
            print('end')
        return inner
    return function

class cdwia:
    def init(self,name4,name5,name6):
        self.name4=name4
        self.name5=name5
        self.name6=name6


    def init(self,*args):
        self.function(*args)

@dwia('sachin','sourav','rahul')
def fun4(x,y):
    print(f'fun4 {x} {y}')
fun4(88,77)