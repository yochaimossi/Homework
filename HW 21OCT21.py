### Q8

def getCircleHekef(radius):
    return 2*3.14*radius

radius= float(input("Enter Radius:"))

Hekef = getCircleHekef(radius)

print (f'hekef is:{Hekef}')


### Q9

def div(x=0,y=0):
    return x/y
def mul (x=0,y=0):
    return x*y
def add (x=0,y=0):
    return x+y
def sub (x=0,y=0):
    return x-y
x= int (input("Enter first number:"))
y= int (input("Enter second number:"))

add1=add(x,y)
mul1=mul(x,y)
div1=div (x,y)
sub1=sub (x,y)

print (f'Division is:{div1}')
print (f'Multiply is:{mul1}')
print (f'Addition is:{add1}')
print (f'Subtract is:{sub1}')

### Q10

def getInRange (min,max,num):
    if num<=min and num >= max:
        return False
    return True

min=int (input("Enter the minimum number:"))
max=int (input("Enter the maximum number:"))
num = int(input("Enter a number to check if it's in the range of numbers:"))

if num >= max or num <= min:

    while getInRange (min,max,num):
      num = int(input("Enter a number to check if it's in the range of numbers:"))
      print (num,"is within range")
      break
else:
    print (num,"is within range")


### Q11

def smallest (x,y,z):
    if z>x and y>x:
        print (x,"is the smallest")
    elif z>y and x>y:
        print(y, "is the smallest")
    elif x>z and y>z:
        print(z, "is the smallest")

x=int (input("Enter first number:"))
y=int (input("Enter second number:"))
z=int (input("Enter third number:"))

smallest(x,y,z)