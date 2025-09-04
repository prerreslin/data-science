import numpy as np

coeffs = [2, -8, 6, -4, 2]
poly = np.poly1d(coeffs)

print("Поліном:")
print(poly)

roots = poly.r
print("\nКорені полінома:")
print(roots)

der_1 = poly.deriv()
print("\nПерша похідна:")
print(der_1)

der_2 = poly.deriv(2)
print("\nДруга похідна:")
print(der_2)

n = 50
value = poly(n)
print(f"\nЗначення полінома при n={n}: {value}")
