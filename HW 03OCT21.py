###Ex1

##### P35 ex 1

First=int(input("Enter a number:"))

n=1

while n<=9:
    Second = int(input("Enter a number:"))
    if Second<First:
        print ("unsorted")
        break
    First=Second
    n=n+1
if n==10:
    print ("sorted")


##### P35 ex 2

ticket=int(input("Enter 1st ticket number:"))
sum=0
n=1

while n<=10:
    sum=sum+ticket
    ticket = int(input("Enter another ticket number:"))
    if sum == ticket:
        print('The sum is', ticket)
        break
    n=n+1
else:
    print ("number not found")

##### P35 ex 3

i=1

while i<10:
    temp = int(input("Enter the temprature ticket:"))
    if temp > 40 or temp < -5:
        print ("Wrong data")
        break
    else:
        i=+1
if i==10:
    print ("Valid data")

##### P35 ex 4


pro=0
con=0
abstain=0
n=1

while n<10:
    vote = input("Please enter your vote:")
    if vote == 'veto':
        print ("The veto country serial number is:",n)
        break
    elif vote == 'pro':
        pro=pro+1
    elif vote == 'con':
        con = con+1
    elif vote == 'abstain':
        abstain = abstain+1
    n = n+1
print ("Pro:",pro,"Con:",con,"Abstain:",abstain)

### Ex2

i=0
sum=0

while True:
    num = int(input("Enter a number:"))
    if num == 0:
        break
    elif num > 77:
        sum=sum+num
        i=i+1
    else:
        continue

print ("Numbers above 77:",i, "Sum is:",sum)

### Ex3

import math
old = math.nan
n=2


while n<=10:
    num = int(input("Enter a number:"))
    if num==old:
        print ("Error:Same number entered twice")
        break
    if num % n == 0 :
        if n == 10:
            print("Number is divided by", n, ",Time to break out of the loop")
            break
        else:
            print ("Number is divided by",n,"now let's check if the numbers are divided by",n+1)
        n = n + 1
    old=num


