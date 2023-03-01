
#Python supports
'''
POP = PROCEDURE ORIENTED PROGRAME
OOP= OBJECT ORIENTED PROGRAME

In procedure oriented  programe  we are using  the  function
and in object oriented programe we use class and  object
'''
'''
suppose we have to solve a problem statement so in order to  solve this  we have  two  approach
we can  use function  or class and  object 
'''

'''
In  function oriented approach  we have  some  restriction i mean  we have  to  do enhancement it is  complex
 or difficult to  enhance  the  existing  function  but  it is  easy  in  class and object  
 
'''

##====================================================================================================================
#CLASS
'''
CLASS is a collection of  similar type of object 

suppose we want to  construct a building 
first we will create a plan and with the  help of same  plan  we can  create  many  buildings 
so the actual building we will construct is  the  object  , indirectly  we can  called  it  class is a collection
of object 


EXAMPLE  INFOSYS IS A CLASS
and the  object is  (employee)
and object is a  real time  entity 

class contain attributes plus operations 


example  Human is class (kalpesh, sujit, raj, snehal)
and  object is  the  

pen  is  a  class  and  object is  (parker pen, cello)


'''


#example
#this is function
'''
def temp():
    return "hi"

a= temp()
print(a)'''

#same with  class and  object

'''class student:
    def __int__(self,roll,name,add):
        self.r=roll
        self.m=name
        self.a=add
    def show(self):
        print(self.r)
        print(self.m)
        print(self.a)'''

#once class is created we can create number of object
#in class we have  variable + methods


#q1 what is the used of init method?
'''
init method is used as a constructor
'''
#if the  function is under class we called it has a method not  a  function
#if the function is  stand  alone we called it has a function
#the more secure is object oriented  then the  procedure oriented


#dunder or magic method
#init=intialisation method
'''
class Test:
    def __init__(self):
        print("Init method")
    def m1(self):
        print("in m1 method")
t1=Test()
t1.m1()'''

#__init__() is a  constructor, use to  initialisation
#self is used for object ref
'''
class Student:
    def __init__(self,roll,name,address):
        self.r = roll
        self.n = name
        self.adr = address
    def show(self):
        print(self.r)
        print(self.n)
        print(self.adr)

p1 = Student(101,'kal','pune')
p1.show()
p2 = Student(12,'rak','we')
p2.show()
print(p1.r)'''


#encapsulation means wrapping data + method  into  one unit

'''
python is  not  100% oop
private  member within 
python outside  name 
'''


#==============================================================================================================

'''
class its an format, once you create a  class you  can  crate any  number of object 
its a collection of similiar type  of object, the  variable + methods
__init__ the use  of this is used to  initialise the  value , and this  is  call once the  object is created 
constructor is start with  double underscore, this  constructor will call when the  object is  created 


what  is the use of self  keyword?
self is just a parameter , we can use  any  name  but  as per the  pep8 we use self 

'''

'''
class and object:
there are three types of variable
1) instance variable  (object level variable) --it is  used in instance method 
2) static varibale ----(class level variable) it is  used in class  method
3) local varibale  -----  (method level variable)   it is  used in  static method 


1) instance variable keep on changing 
2) static varibaleas same value will be  shared among all the  object

'''
#for example

'''class employee:
    company_name = 'SGS'  #static variable
    def __init__(self,id,name):
        self.Id= id
        self.Name = name
    def show(self):
        print("Id is:",self.Id)
        print("Name is:",self.Name)
        print("company  name ",employee.company_name)
a = employee(23,'kal')
a.show()
b  = employee(24,'raj')
b.show()
print(a.Id)
print(a.Name)
print(b.Id)
print(b.Name)
'''

#====================================================================================================================
'''

class & object

***TYPES OF VARIABLE****

instance varibale
static variable
local variable 
'''


'''
in instance varibale  we use  self.varibalename and we can  use inside method and  outside method but we dont use  outside method outside class
in class variable/static varibale  we use  class.varibale name we can  use it inside class and  outside  class
'''
#for example
'''
class employee:
    company_name = 'SGS'  #static variable
    def __init__(self):
        self.name = input("Enter the  name: ")
        self.id = int(input("Enter the  ID:"))
        self.sal = int(input("Enter the current salary:"))


    def show(self):
        def decor(f):
            def inner():
                print("*" * 20)
                f()
                print("*" * 20)
            return inner

        @decor
        def star():
            print("PLEASE CHECK THE BELOW DETAILS")
        star()
        print("Id is:",self.id)
        print("Name is:",self.name)
        print("Company Name: ",employee.company_name)
        s= self.w(self.sal)
        print("Current salary:",self.sal)
        print("Bonus amount",s)
        print("After adding bonus the salary is: ",self.sal+s )

    def w(self,a):
        bonus = 0.12
        c = (self.sal*bonus)
        return c

a= employee()
a.show()
'''


#self################self##################self#################self##############################################

'''
*****TYPES OF METHOD*****

INSTANCE METHOD = object operation maximum variable will be instance variable first parameter  will be  always  self
                90% INSTANCE  METHID  is used
STATIC METHOD  = To perform operation on class variable  first parameter is  cls.variable name 
LOCAL METHOD   = A method which contain logic we can specially  use static method it is  use for  general utility 
'''

'''
class employee:
    company_name = 'SGS'
    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary= salary



    def show(self):
        print("Company Name",employee.company_name)
        print("Employee ID:",self.id)
        print("Employee Name: ",self.name)
        print("*" * 20)
        print("Employee Salary: ",self.salary)
        bonus = self.bonus(self.salary)
        print("bonus",bonus+self.salary)
        print("*" * 20)

    def bonus(self,salary):
        b = 0.12
        c = b*self.salary
        return c

a = employee(12,'kalpesh',20000)
a.show()
'''


'''
class product:
    product_company = 'pixel'
    def __init__(self,prdid,prdname,prdquantity):
        self.prdid = prdid
        self.prdname = prdname
        self.prdquantity = prdquantity
        self.price = 20

    @classmethod
    def product_name_cal(cls):
        cls.product_company = 'pixel ltd'

    def product_prise_change(self):
        self.price = 40
        return self.price


    @staticmethod
    def total_quantity_prise_cal(self,q,p):
        quantity_prise= q*p
        return quantity_prise

    def show(self):
        print("Product ID: ",self.prdid)
        print("Product Name : ", self.prdname)
        print("Product quantity: ", self.prdquantity)
        print("product old prise: ",self.price)
        self.product_prise_change()
        print("product new prise: ", self.product_prise_change())
        a= self.total_quantity_prise_cal(self,self.prdquantity,self.price)
        print("Total quantity ", a)
        print("Product company Name before ",product.product_company)
        self.product_name_cal()
        print("Product company Name after ",product.product_company)

c= product(234,'iron',10)
c.show()'''

#========================================================================================================================
#========================================================================================================================

#INHERITANCE
'''
Is one of the object oriented  features 

there are types of Inhritance
1) single Inheritance (single parent  and  one child)
2) Multi level  Inheritance ( parent to child  then to another child )
3) Multiples Inheritance (two parents one child )
4) Hirchical Inheritance (parent then two child then child  of child  like  a  reverse tree)


'''
'''
#single inheritance

class A:
    def fun(self):
        print("fun")

    def fun0(self):
        print("fun")

class B(A):  #CHILD CLASS
    def fun1(self):
        print("fun1")

a = B()  #class B ---> fun, fun0 and fun1

print("Single Inheritance")
a.fun()
a.fun0()
a.fun1()

#ANS
'''
'''fun
fun0
fun1'''
'''


#Multi level inheritance

class A:  #PARENT CLASS
    def fun(self):
        print("fun")

class B(A):  #CHILD CLASS
    def fun1(self):
        print("fun1")

    def fun2(self):
        print("fun2")

class C(B):
    def fun3(self):
        print("fun3")

    def fun4(self):
        print("fun4")

b = C()   #class C -----> fun,fun0,fun1,fun2,fun3 and fun4
print("Multi level inheritance")
b.fun()
b.fun1()
b.fun2()
b.fun3()
b.fun4()

#ans
'''
'''Multi level inheritance
fun
fun1
fun2
fun3
fun4'''
'''

#Multiples inheritance

class A:  #PARENT CLASS
    def fun(self):
        print("fun")

    def fun1(self):
        print("fun1")

class B:  #PARENT CLASS
    def fun2(self):
        print("fun2")

    def fun3(self):
        print("fun3")

class C(A,B):
    def fun4(self):
        print("fun4")

c = C()   #class C ----> fun,fun0,fun1,fun2,fun3 and fun4
print("Multiples Inheritance")
c.fun()
c.fun1()
c.fun2()
c.fun3()
c.fun4()

#ans
'''
'''Multiples Inheritance
fun
fun1
fun2
fun3
fun4'''
'''

#Hybrid inheritance

class A:  #PARENT CLASS
    def fun(self):
        print("fun")

    def fun1(self):
        print("fun1")

class B:  #PARENT CLASS
    def fun2(self):
        print("fun2")

    def fun3(self):
        print("fun3")

class C:
    def fun4(self):
        print("fun4")

class D:
    def fun5(self):
        print("fun5")

class E(B,D):
    def fun6(self):
        print("fun6")

d = E()  #class E ---> fun2,fun3,fun5,fun6
print("Hybrid inheritance")
d.fun2()
d.fun3()
d.fun5()
d.fun6()

#Hirarchical inheritance

class A:  #PARENT CLASS
    def fun(self):
        print("fun")

    def fun1(self):
        print("fun1")

class B(A):  #PARENT CLASS
    def fun2(self):
        print("fun2")

    def fun3(self):
        print("fun3")

class C(A):
    def fun4(self):
        print("fun4")

class D(B,A):
    def fun5(self):
        print("fun5")

class E(B,A):
    def fun6(self):
        print("fun6")

class F(C,A):
    def fun7(self):
        print("fun7")

class G(C,A):
    def fun8(self):
        print("fun8")

e = G()  #class F ---> fun,fun1,fun4,fun8
print("Hirarchical inheritance")
e.fun()
e.fun1()
e.fun4()
e.fun8()
'''

#=======================================MRO===================MRO=========================MRO======================



class Z:
    pass
class Y:
    pass
class A:
    pass
class B(A):
    pass
class X(Z,Y):
    pass
class C(X,B):
    pass
class P(C):
    pass
class Q(C):
    pass
class E(B):
    pass
class G(E):
    pass
class F(E):
    pass


print(P.mro())
#[<class '__main__.P'>, <class '__main__.C'>, <class '__main__.X'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(Q.mro())
#[<class '__main__.Q'>, <class '__main__.C'>, <class '__main__.X'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(G.mro())
#[<class '__main__.G'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(F.mro())
#[<class '__main__.F'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(C.mro())
#[<class '__main__.C'>, <class '__main__.X'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(E.mro())
#[<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(X.mro())
#[<class '__main__.X'>, <class '__main__.Z'>, <class '__main__.Y'>, <class 'object'>]

print(B.mro())
#[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(X.mro())
#[<class '__main__.X'>, <class '__main__.Z'>, <class '__main__.Y'>, <class 'object'>]

print(Y.mro())
#[<class '__main__.Y'>, <class 'object'>]

print(A.mro())
#[<class '__main__.A'>, <class 'object'>]





