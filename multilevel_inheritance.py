class a:
    def add_1(self):
        self.a=10
        print(self.a)
class b(a):
    def add_2(self):
        self.b=20
        print(self.b+ self.a) 
class c(b):
    def add_3(self):
        self.c=30
        return self.a+self.b+self.c     
d=c()
d.add_1()
d.add_2()    
print(d.add_3())    