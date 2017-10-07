#import Signature and Parameter; these class ensure the parameters passed are in correct way or not
from inspect import Signature, Parameter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#function to assign a signature
#Signature a list as parameter
#Parameter ensure either the parameter is positional or keyword or both
def make_signature(fields):
    return Signature([Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) for f in fields])

class Base:
    sig = make_signature([])
    def __init__(self, *args, **kwagrs):
        #bind the signature and ensure that it can bind both positioal and keyword arguments
        bound = self.sig.bind(*args, **kwagrs)
        for key, value in bound.arguments.items():
            #set attribute to this class instance
            setattr(self, key, value)

class Person(Base):
    sig = make_signature('name age'.split())

'''
Let's check the code.
run the script and create Person object
p = Person() #this will show an error which is okay 
p = Person('John', 23)
p.name 
p.age

'''