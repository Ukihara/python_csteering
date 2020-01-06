#The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in
#base 10 and base 2.


def palindr(str1):
    str2 = str1[::-1]
    return str1 == str2

nums = 0
summa = 0
sumbin = 0
while nums != 1000000:
    numb = bin(nums)[2:]

    if palindr(str(nums)):
        summa = summa + int(nums)
    if palindr(str(numb)):
        sumbin = sumbin + int(nums) #суммирует двоичные палиндромы в десятичном виде
    nums = nums + 1

print(summa)
print(sumbin)