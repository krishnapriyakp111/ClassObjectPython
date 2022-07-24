class Addition():
    def __init__(self,x):
        self.x=x
    def add(self):
        res=[i for i in set(self.x) if self.x.count(i)>1]
        for i in res:
            print(i,end=' ')


p=input('enter the string: ')
tos=Addition(p)
n=tos.add()
