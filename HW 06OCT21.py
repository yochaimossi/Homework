### P25 Ex 8

import math

small = math.nan
num1 = int(input("Enter a number:"))

if num1 <= 0:
    print("no positives")
else:
    while True:
        num2 = int(input("Enter a 2 number:"))
        if num2 > 0:
            if num2 < num1:
                small = num2
            else:
                small = num1
        elif num2 <= 0:
            break
    print("The smallest positive", small)

### P25 Ex 9

num1 = int(input("Enter a number:"))
n = 1
i = 1

while n < 100:
    num2 = int(input("Enter a number:"))
    i = i + 1
    if num2 > num1:
        num1 = num2

    elif num2 < num1:
        i = i - 1
    n = n + 1

print("The index is", i)


### P25 Ex 10

num1 = int(input("Enter a number:"))

while num1//10 > 0:
    num1 = num1//10
print (num1)

### P25 Ex 11

num1 = int(input("Enter a number:"))
i=1

while num1//10 > 0:
    num1 = num1//10
    i = i + 1
print ("The number of digits is", i)

#### P25 Ex 12

num1 = int(input("Enter a number:"))
sum=0


while num1 > 0:
    sum = sum+ num1%10
    num1 = num1//10
print ("The sum of digits is", sum)

### HW Q2
while True:
    num1 = int(input("Enter a number:"))
    while num1 == 0:
        num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a  number:"))
    while num2 == 0:
        num2 = int(input("Enter a number:"))

    if num1 > num2:
     print ("bigger")
     continue
    else:
        break
### HW Q3

a = int(input("Enter a:"))
b = int(input("Enter b:"))
p=1


while b>0:
    m = 0
    t = a
    while t>0:
        m=m+p
        t=t-1
    p=m
    b=b-1

print (p)


### HW Q4

num = int(input("Enter a number:"))
sum = 0

while True:
    if num <=0:
        print ("Not a positive number")
        break
    elif num > 0:
        sum=0
        while num > 0:
            sum=sum+num%10
            num=num//10
    print(sum)
    num = int(input("Enter a number:"))
