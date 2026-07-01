class feet:
    def read(self,inches):
        self.inches=inches
    def to_feet(self):
        self.feet=self.inches/12
    def display(self):
        print("inches:",self.inches)
        print("feets:",self.feet)
a=feet()
a.read(65)
a.to_feet()
a.display()                