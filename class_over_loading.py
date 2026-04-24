class overload:
    def add(self,a,b,c=0):
        return a+b+c
ob=overload()
print(ob.add(10,20))
print(ob.add(10,20,40))