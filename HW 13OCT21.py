### P26 Ex 16

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
sum=0

for index in range (1,b+1,1):
    sum=sum+a
print (sum)

### P35 Ex1
a = int (input ("Enter a number:"))
small = a

for index in range (1,100,1):
    b = int(input("Enter a another number:"))
    if b<small:
         break
    else:
        small=b

### P38 Ex8

a = int (input ("Enter the number of rows:"))
b = int (input ("Enter the number of columns:"))
for index in range (1,a+1,1):
    print ('\n')
    for index in range (1,b+1,1):
     print ('*','',end='')