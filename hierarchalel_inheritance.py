class a:
    def add_1(self):
        self.a=10
        print("a=",self.a)
class b(a):
    def add_2(self):
        self.b=20
        print("a+b=",self.b+ self.a) 
class c(a):
    def add_3(self):
        self.c=30
        print("c+a=",self.a+self.c)     
d=b()
e=c()
d.add_1()
d.add_2()    
e.add_1()
e.add_3()  