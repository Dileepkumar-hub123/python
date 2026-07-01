#convert seconds into hourss,minutes,days
class Time :
    def read(self,seconds):
        self.seconds=seconds
    def to_convert(self) :
       self.hour=self.seconds//3600
       self.minutes=(self.seconds-(self.hour*3600))//60
       self.seconds=self.seconds-self.hour*3600-self.minutes*60
    def display(self) :
        print("Hours=",self.hour)
        print("minutes=",self.minutes)
        print("seconds=",self.seconds)
t=Time()
t.read(4000)
t.to_convert()
t.display()       
            