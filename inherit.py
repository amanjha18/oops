# single inheritance
'''
class A():
    def feature1(self):
        print ("feature1 working")
    def feature2(self):
        print("feature2 working")

#child class or subclass
class B(A):
    def feature3 (self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")

b1=B()
b1.feature3()
'''

# multi Level inheritance.
'''
class A():
    def feature1(self):
        print ("feature1 working")
    def feature2(self):
        print("feature2 working")

#child class or subclass
class B(A):
    def feature3 (self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")

class C(B):
    def feature5(self):
        print ("feature5 working")

b1=B()
b1.feature1()
c1=C()
'''

# multiple inheritance

class A():
    def feature1(self):
        print ("feature1 working")
    def feature2(self):
        print("feature2 working")


class B():
    def feature3 (self):
        print("feature3 working")
    def feature4(self):
        print("feature4 working")

class C(A,B):
    def feature5(self):
        print ("feature5 working")
a1=A()
b1=B()

c1=C()
c1.feature4()
