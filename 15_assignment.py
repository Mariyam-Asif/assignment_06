class A: 
    def show(self):
        return "Show from Class A"

class B(A):
    def show(self):
        return "Show from Class B"

class C(A):
    def show(self):
        return "Show from Class C"

class D(B, C):
    pass

d = D()
print(d.show())
print(D.mro()) # Method Resolution Order