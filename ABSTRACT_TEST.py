from ABSTRACT_METHOD import student
#we have done the  implemention
'''
class student_imp(student):
    def username(self):
        print("actual implementation")
    def password(self):
        print("password implementation")

obj = student_imp()
obj.username()
obj.password()'''

#now we will do the  seperate  implementation for each  method

class username_imp(student):
    def username(self):
        print("actual implementation")
class password_imp(username_imp):
    def password(self):
        print("password implementation")

obj = password_imp()
obj.username()
obj.password()


#interview question
'''
Q1) diff between pass and  continue?
Ans:
continue will skip the  element but  in pass if we are designing a code on initial level and we dont have  any logic for a  
particlular function we can  use pass 
And pass is executable  code 


'''