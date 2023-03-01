#================================================Abstractmethod=============================================================
'''
NOT USE MUCH

Abstract means hiding complexity from end user
we cant create  an object of  abstract  due to  security  reason  because  it is  only abstract view  not  implemetation

when  we can  say  that  abstraction is  done  ?
Ans:
based on  2 condition
1. class should be  inheritance by  ABC
2. atleast  one  method  should be  abstract
(means  we need to  hide implementation of  one  method
both  condition need  to  be  satisfied

'''
from abc import ABC, abstractmethod


class student(ABC):
    @abstractmethod
    def username(self):
        pass
    @abstractmethod
    def password(self):
        pass

'''
important
we cant create an object unless and until all the  abstract method  is  implemented  
'''




