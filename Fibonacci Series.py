# Fibonacci series upto an input limit

num = int(input())
num1 = int(0)
num2 = int(1)
sum = int(0)

print(num1, num2, sep = ' ', end = ' ')
while sum < num:
    sum = num1 + num2
    if sum > num:
        break
    print(sum, end = ' ')
    num1 = num2
    num2 = sum
    