pi=3.14
def cube(s):
    return s**3
def pilar(r,h):
    return pi*r**2*h
def sphere(r):
    return 4/3*pi*r**3
def square(l,w,h):
    return l*w*h
def corn(r,h):
    return 1/3*pi*r**2*h
print(cube(12))
print(cube(20))
print(square(3,5,6))
print(corn(20,10))
print(sphere(15))
print(pilar(20,10))