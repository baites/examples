
class Identity:
    def run(self, x):
        return x

def MandelbrotSeq(Base, n):
    def Mandelbrot(Base, n):
        if n == 0:
            return Base
        class _(Base):
            def run(self, x):
                x = super().run(x)
                return x**2 + self.c
        return Mandelbrot(_, n-1)
    return Mandelbrot(Base, n).__mro__

M = MandelbrotSeq(Identity, 5)

m = M[0]()
m.c = 1
# print 677 the value at 5th iteration for c=1
print(m.run(0))

m = M[1]()
m.c = 1
# print 26 the value at 4th iteration for c=1
print(m.run(0))

m = M[2]()
m.c = 1
# print 5 the value at 3th iteration for c=1
print(m.run(0))
