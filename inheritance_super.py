#Inheritance
#super keyword   ----no need to use self
#overridding method

class car:
    def __init__(self, model , topSpeed ,year ):
        self.model = model
        self.topSpeed = topSpeed
        self.year = year
    def gearChange(self):
        print("gear of your car has been changed")    
    def info(self):
        print("car model is {} and car top speed is {}".format(self.model,self.topSpeed))

class sportsCar(car):
    def __init__(self,model,topSpeed ,year, color ,acceleration):
        super().__init__(model , topSpeed , year)
        self.color = color
        self.acceleration = acceleration

        #MEthod Overriding
    def info(self):
        print("Info of sports car")    

porsche = sportsCar('panamera','100kmph',2017,'black',300)      
porsche.info()              