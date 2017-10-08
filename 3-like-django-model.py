from inspect import Signature, Parameter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def make_signature(fields):
    return Signature([Parameter(f, Parameter.POSITIONAL_OR_KEYWORD) for f in fields])

class Contract:
    
    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        print('setting')
        instance.__dict__[self.name] = value


class Type(Contract):
    ty = None
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.ty}')
        super().__set__(instance, value)


class String(Type):
    ty = str

class Integer(Type):
    ty = int

#here is the core part to know
class CustomType(type):
    '''Type subclass'''
    def __new__(cls, clsname, bases, clsdict):
        fields = [key for key, val in clsdict.items() if isinstance(val, Contract)]
        if fields:
            sig = make_signature(fields)
            clsdict['sig'] = sig
        return super().__new__(cls, clsname, bases, clsdict)

#and we used it here which gives us a concept of meta programming
class Base(metaclass=CustomType):
    fields = []
    def __init__(self, *args, **kwagrs):
        bound = self.sig.bind(*args, **kwagrs)
        for key, value in bound.arguments.items():
            setattr(self, key, value)

class Person(Base):
    name = String()
    age = Integer()