import numpy as np

array = np.arange(10, 20)
print(array)
print(array.dtype)
total = array.sum()
print(total)
average = array.mean()
print(average)
minimum = array.min()
print(minimum)
maximum = array.max()
print(maximum)

assert total == 145, "Сума масиву повинна дорівнювати 145"
assert average == 14.5, "Середнє значення масиву повинно дорівнювати 14.5"
assert minimum == 10, "Мінімальне значення масиву повинно бути 10"
assert maximum == 19, "Максимальне значення масиву повинно бути 19"
