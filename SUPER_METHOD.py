
#Super Method
'''
super() method:
the use of this  method is that  if we have  a  parent class and  child  class and both  have the  same method name
for  example  m1
Normally what  we do  if we have  a parent  class already  and  we need to add something in  the  same  class
for example
class employee:
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("city")

And now  we want to add instagram ID as well in the same method
so  we can  do it  like  this

class employee:
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("city")


class extended_emp(employee):
    def m1(self):
        print("instagram ID")

a = extended_emp()
a.m1()
#Answere will be (instagram ID) as per MRO First it will search for m1 in self first

but in this  case  the  old m1 is not  displayed it is  overwritten , and  we need the  old  plus the  new  one as well
so  in this  case need to use  super method
for example
class employee:
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("city")


class extended_emp(employee):
    def m1(self):
        super().m1()   #supermethod help to call the  old method  as well
        print("instagram ID")

a = extended_emp()
a.m1()
#Answere will be
Age
Name
city
instagram ID

'''


'''class employee:
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("city")


class extended_emp(employee):
    def m1(self):
        super().m1()
        print("instagram ID")

a = extended_emp()
a.m1()
'''


'''class employee:
    def __init__(self):
        pass
    def m1(self):
        print("Age")
        print("Name")
        print("city")


class extended_emp(employee):
    def m1(self):
        super().m1()
        print("instagram ID")

class new_ext(extended_emp):
    def m1(self):
        super().m1()   #by using this  we can  call the  parent  method
        print("whatsapp")


obj = new_ext()
obj.m1()'''


#Note
'''
variable  or  function need to  use  snake cassing   (snake_case)
class name should be  in  pascal cassing (PascalCase), camelCase)

'''


#Q1 suppose if we want  to call any  method inside the  method  we can  do it in this  way
'''
class A:
    def __init__(self):
        pass
    def m1(self):
        print("in m1 ")
    def m2(self):
        print("in m2")

class B(A):
    def m3(self):
        super().m1()
        super().m2()
        print("in m3")

obj = B()
obj.m3()'''



'''class A:
    def m3(self):
        print("in m3 of A")

class B:
    def m3(self):
        super().m3()
        print("in m3 of B")

class C(B,A):
    def m3(self):
        super().m3()
        print("in m3 of C")


obj = C()
obj.m3()'''



#if we want to  call a specific method insted of following the  MRO rule we can  do it  by  the  follow  method

'''class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(B):
    def m1(self):
        print("m1 from C")
class D(C):
    def m1(self):
        print("m1 from D")
class E(D):
    def m1(self):
        super(C,self).m1()   #this  method we use to call the  directed method
        print("m1 from E")
        
obj = E()
obj.m1()
'''

'''class X:
    def m1(self):
        super().m1()
        print("m1 from X")

class A(X):
    def m1(self):
        super().m1()
        print("m1 from A")
class B:
    def m1(self):
        print("m1 from B")
class C(A,B):
    def m1(self):
        super().m1()
        print("m1 from C")

obj = C()
obj.m1()'''

#================================================Abstractmethod=============================================================

