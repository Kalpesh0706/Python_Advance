'''
Access Specifiers:
means  a  variable  where  we can  access it
so in generally  in order to  maintain the  security  we  have  three types  of  varibale
1. public
2. protected
3. private
'''

'''
PUBLIC
public means  we can  access anywhere within the class  and  out side  the  class
for example :
'''
'''course = 100  #global variable
class A:
    course = "python"  #class level
    def m1(self):
        print("in m1 from A")
        print(A.course)  #insie  the class

obj = A()
obj.m1() #call from inside  the class
print(A.course)   #class variable outside the  class
print(course) #global varibale'''

'''
A vaibale  which  is  accessable  anywhere  it is  called  public  variable (public  access specifier)
we can  access within the class  or  outside  as well 

whenever  we create  a  variable in  class  it is  by  default  public  
'''




'''
PROTECTED
This  says  within  the class  you  can  call it  anywhere and  in  child  class
can  be access by  parent and  child  
only  if it is  inheritance in child  
'''

'''
class A:
    _course = "python"  #protected
    def m1(self):
        print("in m1 from A")

class B(A):
      def m2(self):
        print("from m2:",A._course)

obj = B()
obj.m2()
print(A._course)
print(B._course)'''

'''
Note : public  and  protected are both  same  
both are accessable  within and  outside  the  class so the  exactly differece  is by  syntatically  and its a duty  of  developer
to state the  varibale public  or  protected 
And in protected  varibale  we need to  use  it within  the child  only  as it is  a  good  practise 
'''


'''
PRIVATE
This  varibale  can be  only  access within the  class  not  outside the  class
for example

'''
class A:
    __course = "python"
    def m1(self):
        print(A.__course)

obj = A()
obj.m1()
#print(A.__course)  # not accessable  because  it is  a  private
'''
but we can still access  it  by  the  following
'''
print(obj._A__course)  #this  concept is  called name  mangling
'''
ILLEGAL practise don't  try 
'''

'''
IMPORTANT
Public
_Protected ---> parent, child
__Private  ----> within  the  class  
'''