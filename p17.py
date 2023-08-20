#6. Create Array using NumPy and Perform Operations on Array

import numpy as np
a = np.array( [20, 30, 40, 50] )
print(f'Elements of array a:: {a}')
b=np.arange(1,8,2)
print(f'Elements of array b:: {b}')
print(f'Addition:: {a+b}')
print(f'with add() method::{np.add(a,b)}')
print(f'Substraction:: {a-b}')
print(f'with substract() method::{np.subtract(a,b)}')
print(f'Multiplication:: {a*b}')
print(f'with multiply() method::{np.multiply(a,b)}')
print(f'Division:: {a/b}')
print(f'with divide() method::{np.divide(a,b)}')