# determining prime number

num = int(input())
count = int(0)

if num == 2:
    print('prime')

elif num > 1 and num != 2:
    for i in range(2, num):
        if num % i == 0:
            print('not prime')
            break
        else:
            print('prime')
           
else:
    print('not prime') 
                        
        