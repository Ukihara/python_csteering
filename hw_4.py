#1. После запуска предлагает пользователю ввести целые неотрицательные числа,
#разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
#2. Получив вводные данные, выделяет полученные числа, суммирует их,
#и печатает полученную сумму.

nums = input("Enter numbers: ")

l = len(nums)
integ = list()
i = 0
summa = 0

while i < l:
    s_int = ''
    a = nums[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = nums[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
    
for i in integ: summa += i
print(summa)