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
fun
fun0
fun1
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

'''Multi level inheritance
fun
fun1
fun2
fun3
fun4'''


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

'''Multiples Inheritance
fun
fun1
fun2
fun3
fun4'''


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
