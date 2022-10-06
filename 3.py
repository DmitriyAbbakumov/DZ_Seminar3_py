# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_real_numbers = [1.1, 1.2, 3.1, 5, 10.01]
list_real_numbers2=list()
for i in range (len(list_real_numbers)):
    if '.' in str(list_real_numbers[i]):
        list_real_numbers2.append (round(list_real_numbers[i]%1,2))
minim = list_real_numbers2[0]
maxim = list_real_numbers2[0]
for i in range (len(list_real_numbers2)):
    if list_real_numbers2[i]>maxim: maxim=list_real_numbers2[i]
    if list_real_numbers2[i]<minim: minim=list_real_numbers2[i]
print(list_real_numbers, maxim-minim, sep=' => ')
