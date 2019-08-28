import abc

class My_ABC_Class(object):
    __metaclass__=abc.ABCMeta
    @abc.abstractmethod
    def set_val(self, val):
        return
    
    @abc.abstractmethod
    def get_val(self):
        return

class MyClass(My_ABC_Class):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        print("\ncalling the get_val() method")
        print("I'm part of the Abstract Methods defined in My_ABC_Class()")
        return self.val 
    
    def hello(self):
        print("\ncalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_class()")

My_class = MyClass()

My_class.set_val(10)
print(My_class.get_val())
My_class.hello()


