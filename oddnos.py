for num in range(1, 101):
    if num % 2 != 0:
        print(num)
odd_numbers = [n for n in range(1, 101) if n % 2 == 1]
print(odd_numbers)
num = int(input("Enter a number: "))

if num % 2 != 0:
    print(num, "is odd")
else:
    print(num, "is not odd")
numbers = [10, 15, 22, 33, 47, 50]

odd_nums = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odd_nums)
numbers = [10, 15, 22, 33, 47, 50]

odd_nums = [n for n in numbers if n % 2 != 0]
print("Odd numbers:", odd_nums)
