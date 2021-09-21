#Page 26 ex 7

n = int(input("Enter a number:"))
highest_num=n
while n > 0:
    n = int(input("Enter a number:"))
    if highest_num < n :
     highest_num = n
print (highest_num)

#Page 26 ex 8

n = int(input("Enter a number:"))
lowest_num = n
while n > 0:
    n = int(input("Enter a number:"))
    if lowest_num > n and n > 0:
     lowest_num = n
print (lowest_num)

#Page 26 ex 10

n = int(input("Enter a number:"))

while n//10>=1:
    n=n//10
print (n)

#Page 26 ex 12

n = int(input("Enter a number:"))
sum = 0
while n > 0:
    n1=n%10
    sum=sum+n1
    n=n//10
print (sum)

#Page 27 ex 19

n = int(input("Enter a number:"))
sum=1
while n>0:
    sum=sum*n
    n=n-1
print (sum)

#Page 27 ex 23

num = int(input("Enter a number:"))
n=1
while n<=num:
    if num%n == 0:
     print (n)
    n=n+1
#Page 27 ex 24

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
highest_den=1
n=0

if num1>num2:
    while highest_den<=num1:
        if num1%highest_den == 0 and num2%highest_den == 0:
            n=highest_den
        highest_den=highest_den+1
else:
    while highest_den<=num2:
        if num1%highest_den == 0 and num2%highest_den == 0:
          n=highest_den
        highest_den=highest_den+1
print (n)