'''
class Robot(object):
    def __init__(self):
        self.a=123
        self._b=123
        self.__c=123
    
obj= Robot()
print(obj.a)
print(obj._b)
print(obj.__c)
'''


'''
class Car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

blackcar = Car()
blackcar.drive()
'''
# cannot access a private method (__updatesoftware)outside the class.


class Car:
    __maxspeed=0
    __name=""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
    
redcar = Car()
#redcar.__maxspeed = 300 # can't access outside of this  variable.
redcar.drive()
redcar.setspeed(100)
