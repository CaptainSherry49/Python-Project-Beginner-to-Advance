# -------------------------- Diamond Shape Problem ----------------------- #
'''
In Python Diamond Shape Problem  is not that much difficult Yeah some time if your code is more lengthy it can be difficult
but in others languages programmers trying to avoid multiple inheritance because of this problem, one more thing is that
'java' doesn't support multiple inheritance.
'''
class A:

    def met(self):
        print('I am Method in Class A')


class B(A):

    def met(self):
        print('I am Method in Class B')


class C(A):

    def met(self):
        print('I am Method in Class C')


class D(B, C):  # order matters
    pass


a = A()
b = B()
c = C()
d = D()

d.met()

'''
Agar to ya method 'D' k andar hoga to ya yahi sa run karda ga warna pehla ya 'B' ma dhonda ga phir 'C' ma q k inherit 
karta waqt ham na order ma (B, C) diya tha agar dono ma nhi mila to phir 'A' ma chala jai ga q k 'B' or 'C' both class 'A'
sa inherit horahi ha
'''