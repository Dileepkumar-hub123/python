class a:
    def add_1(self):
        self.a=10
        print("a=",self.a)
class b(a):
    def add_2(self):
        self.b=20
        print("b=",self.b+ self.a) 
class c(b):
    def add_3(self):
        self.c=30
        print("c=",self.a+self.b+self.c)     
class d:
    def add_4(self):
        self.d=40
        print("d=",self.d)
class e(c,d):
    def add_5(self):
        print("e=",self.c+self.d)

ob_2=e()
ob_2.add_1()
ob_2.add_2()
ob_2.add_3()
ob_2.add_4()
ob_2.add_5()