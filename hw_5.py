#1. После запуска предлагает пользователю ввести неотрицательные целые числа,
#разделенные через пробел и ожидает ввода от пользователя.
#2. Находит наименьшее положительное число, не входящее в данный пользователем
#список чисел и печатает его.

nums = input("Please, enter some numbers: ")
lst = []
pol = 1   #положительные числа начинаются с 1

nums = nums.split()
for i in nums:
    lst.append(int(i))

lst.sort()
m = set(lst)

for i in m:
    if int(i) == pol:
        pol = pol + 1
    else:
        print(pol)
        break