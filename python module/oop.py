#!/usr/bin/env python3

class truck:
    wheels = True
    def __init__(self,color,doors): #always call it as self
        self.color = color
        self.doors = doors
        self.speed = 0
        self.bearing = 0
        
    def accelerate(self,num):
        self.speed += num
        
    def decelerate(self,num):
        self.speed -= num
        
    def stop(self):
        self.speed = 0

    def dirChange(self,dir):
        self.bearing = (self.bearing + dir) % 360

    def __str__(self):
        return "The {} {}-door truck is moving at {} speed on {} heading.".format(self.color,self.doors,self.speed,self.bearing)

if __name__ == '__main__':
    cyberTruck = truck('silver',2)
    cyberTruck.accelerate(15)
    cyberTruck.accelerate(12931)
    cyberTruck.stop()
    cyberTruck.dirChange(900)
    cyberTruck.accelerate(3520)
    cyberTruck.decelerate(3000)
    print(cyberTruck)