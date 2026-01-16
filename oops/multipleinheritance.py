class Movement:
    def walk(self):
        print("Robot is walking")


class Communication:
    def speak(self):
        print("Robot is speaking")


class Robot(Movement, Communication):
    def explore(self):
        print("Robot exploring all features")


obj = Robot()
obj.walk()     
obj.speak()      
obj.explore()   
