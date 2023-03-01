'''
POLYMORPHISM

POLY ---> MANY
MORPHISM ---> FORMS
ONE METHOD  CAN  USE  N NUMBERS  OF TIMES , METHOD WILL BE THE  SAME  BUT THE  BEHAVIOUR WILL BE  CHNAGE
'''

'''
There are two types of  polymorphism
1.OVERLOADING:
same method name  difference is  data  type
b)method overloading ( not possible )
b)constructor ovrloading  (not possible)
c) operator overloading ( possible magic method )


2.OVERRIDING:
a)oprator overriding  (using super method)
b)method overriding   (using super method)
c)constructor overriding (using super method)


#OVERRIDING
EXAMPLE
'''

'''class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

class B(A):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id = id
        self.salary= salary
    def show(self):
        super().show()
        print("ID: ",self.id)
        print("Salary:",self.salary)

obj = B("kalpesh",26,234,95000)
obj.show()
'''


'''
#OVERLOADING:-
OVERLOADING means same name with  different data  types 
method : not possible 
constructor :not possible 
operator : we can  over load  operator



EXAMPLE

'''
'''class Test:
    def __init__(self,val):
        self.val = val

obj1= Test(450)

obj2 = Test(500)

print(obj1+obj2)'''

'''
the above will give  error because  we cannot add two object
but if we do  obj.val it is  possible 
'''

'''class Test:
    def __init__(self,val):
        self.val = val

obj1= Test(450)

obj2 = Test(500)

print(obj1.val+obj2.val)'''  #obj.val

'''
but if we need to  add the  object we can do it thi way
'''

'''class Test:
    def __init__(self,val):
        self.val = val
    def __add__(self, other):
        return self.val+other.val
obj1= Test(450)

obj2 = Test(500)

print(obj1+obj2)'''

'''
Now  adding  3 object
'''

class Test:
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return "Total of object: {}".format(self.val)  #this is overload
    def __add__(self, other):
        total = self.val+other.val
        return Test(total)
obj1= Test(450)

obj2 = Test(500)

obj3 = Test(450)
print(obj1+obj2+obj3)


#--============================================================================================
