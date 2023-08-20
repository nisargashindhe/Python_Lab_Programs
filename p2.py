#2. Solve Quadratic Equations

import cmath
a=int(input(" Enter a value of a : "))
b=int(input(" Enter a value of b : "))
c=int(input(" Enter a value of c : "))
d=((b**2)-(4*a*c))
sol1=(((-b)+cmath.sqrt(d))/(2*a))
sol2=(((-b)-cmath.sqrt(d))/(2*a))
print(f' The Quadratic Equation are ---\n {sol1}\n {sol2}')