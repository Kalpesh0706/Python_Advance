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
