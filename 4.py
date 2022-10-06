# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите число: "))
binary_number = list()
while n>=1:
    ost=n%2
    n=int(n/2)
    binary_number.append(ost)
for i in range(int(len(binary_number)/2)):
    binary_number[i], binary_number[-i-1] = binary_number[-i-1], binary_number[i]
print(*binary_number, sep="")

