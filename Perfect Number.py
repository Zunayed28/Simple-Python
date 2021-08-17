# determining perfect number

num = int(input())
a = []

for i in range(1, num):
    if num % i == 0:
        a.append(i)
        
sum = int(0)
        
for i in range(0, len(a)):
    sum = sum + a[i]
                    
if sum == num:
    print('perfect')
      
else:
    print('not perfect')      