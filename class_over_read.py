class A:
    def show(self):
        print("i am from parent class")
class B(A):
    def show(self):
    
        print("i am from child class")
c=B()
c.show()              
