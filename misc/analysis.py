import sympy as sym
import math
x = sym.Symbol('x')
f = x**2+ math.e **(-x)
print("function=", f)
print("integral=", sym.integrate(f, x))
print("derivate=", sym.diff(f, x, 1))

print("\n\n\n\n")
x = sym.Symbol('x')
f = x**2* math.e **(-x)
print("function=", f)
print("integral=", sym.integrate(f, x))
print("derivate=", sym.diff(f, x, 1))


print("\n\n\n\n")
x = sym.Symbol('x')
f = 1/2*2**x
print("function=", f)
print("integral=", sym.integrate(f, x))
print("derivate=", sym.diff(f, x, 1))

import sympy as sym
x = sym.Symbol('x')
f = 1/(sym.cos(x+(sym.pi/4))-1) + 2
print("function=", f)
print("derivate=", sym.diff(f, x, 1))