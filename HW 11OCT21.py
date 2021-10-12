### P15 Ex3

diameter = int(input("Enter diameter:"))
depth = int(input("Enter depth:"))

r = diameter/2
pi= float (3.14)

capacity = (r**2)*pi*depth

print ("The capacity of the pot is:",capacity)

### P15 Ex6

num = int(input("Enter a number:"))

num=num//10
num=num%10

print (num)

### P15 Ex7

num = int(input("Enter a 3 digit number:"))

while num>10:
    num=num//10
print (num)

### P15 Ex8

num = int(input("Enter a 2 digit number:"))
sum=0

while num>0:
    sum = sum + num%10
    num= num//10
print (sum)


### P15 Ex9

num = int(input("Enter a 2 digit number:"))
num1=0
sum=0

while num>10:
    num1 = (num%10)*10
    num= num//10
    sum=num1+num
print (sum)


### P15 Ex10

num = float(input("Enter a number:"))
num1= int(num)


if num1%2 == 0:
 print (num1+2)
else:
    print (num1+1)


### P18 Ex4

num = int(input("Enter a 2 number between 1 and 9999:"))
i=0

while num>0:
    num=num//10
    i=i+1
print (i)

### P18 Ex5

name=input('Enter emplyee name:')
salary=float(input("Enter salary:"))

if salary <= 23000:
    tax1=salary*0.1
    print (name,"will pay",tax1,"NIS in taxes")
elif salary>23000 and salary<=46000:
    tax1 = 23000*0.1
    tax2=(salary-23000)*0.2
    print(name, "will pay", tax1+tax2, "NIS in taxes")
elif salary>46000 and salary<=120000:
    tax1 = 23000 * 0.1
    tax2 = 23000 * 0.2
    tax3=(salary-74000)*0.3
    print (name, "will pay", tax1+tax2+tax3, "NIS in taxes")
elif salary>120000 and salary<=220000:
    tax1 = 23000 * 0.1
    tax2 = 23000 * 0.2
    tax3 = 74000 * 0.3
    tax4=(salary-120000)*0.4
    print(name, "will pay", tax1+tax2+tax3+tax4, "NIS in taxes")
else:
    tax1 = 23000 * 0.1
    tax2 = 23000 * 0.2
    tax3 = 74000 * 0.3
    tax4 = 100000 * 0.4
    tax5 = (salary-220000)*0.5
    print(name, "will pay", tax1 + tax2 + tax3 + tax4 + tax5, "NIS in taxes")

### P20 Ex2

grade=int(input("enter student grade in numbers:"))

if grade<55:
    print ('Not enough')
elif grade>=55 and grade<65:
    print('Enough')
elif grade>=65 and grade<75:
    print('Almost good')
elif grade >= 75 and grade < 85:
    print('Good')
elif grade >= 85 and grade < 95:
    print('Very good')
elif grade >= 95:
    print('Excellent')

### P25 Ex13

X = int(input("Enter a number:"))
dig = int(input("Enter a single digit:"))
i=0

while X>0:
    if X%10 == dig:
        i = i+1
    X=X//10
print (i)

### P25 Ex14

num = int(input("Enter a number:"))
new_num=0

while num > 0 :
    new_num=new_num*10+num%10
    num=num//10
print (new_num)

### P25 Ex15

num = int(input("Enter a number:"))
new_num=0
num1=num

while num > 0 :
    new_num=new_num*10+num%10
    num=num//10
if num1 == new_num:
    print ("Polindrom")
else:
    print ("Not a Polindrom")

### P25 Ex16

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a multiplier:"))
num3=0
i=1

while i <= num2:
    num3 = num3+num1
    i = i + 1
print (num3)

### P33 Ex19

i=int(input("Enter a number for Fibbonaci"))
a=1
b=1

while b<=i:
    c=a+b
    a=b
    b=c
print (b)

### P26 Ex 19

num = int(input("Enter a number:"))
i=2
atzeret=1

while i<=num:
    atzeret=atzeret*i
    i = i + 1
print (atzeret)

### P26 Ex 23

num = int(input("Enter a number:"))
i=1

while i <= num:
    if num%i == 0:
        print (i)
    i = i + 1
### P25 Ex5

n=0

while True:
    x = int(input('Enter a number for prime detection:'))
    i = 2

    while x % i != 0:
      i += 1
    if i == x:
        print("The number of non primes before:",x,"is",n)
        break
    n=n+1
