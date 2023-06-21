#Classes and Objects in Python
#Everything is an object: Strings, booleans, numbers, and even Python functions are objects
#Method: 

"test".__len__()
4
len("test")
4

#class: 

type('a')
<class 'str'>
type(1)
<class 'int'>
type(True)
<class 'bool'>

# Class
class Car:
    #variables: This is data that all instances of this class will have.
    speed = 0
    started = False

    #three methods that operate on the variables
    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooom!")
        else:
            print("You need to start the car first!")

    def stop(self):
        self.speed = 0
        print("Halting")

        
#Object
car = Car()
car.increase_speed(10)
You need to start the car first!
car.start()
Car started, let's ride!
car.increase_speed(40)
Vrooom!
car.stop()
Halting
car.shut_down()


#Creating multiple objects
>>> car1 = Car()
>>> car2 = Car()
>>> id(car1)
139771129539104
>>> id(car2)
139771129539160