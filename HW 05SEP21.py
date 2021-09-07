#Homework 05SEP21 - Yochai Mossi - 300604121
#1st Exercise

a=int(input('Enter a number:'))

if a%5==0 and a%2==0:
    print (a,"is divded by 10 without remainder")
else:
    print (a,"does not divide by 10 without remainder")

#2nd Exercise

b=int(input('Enter a number:'))

if b==0 or b==1:
    print ("0 or 1")
else:
    if b==-1:
        print ("-1")
    else:
        print ("unknown number")

#3rd Exercise

c=int(input('Enter a number:'))
asarot = c//10
if asarot>=1 and asarot<=10:
    print (c%10)
else:
    print ("Not a two digit number")

#4th Exercise

d=int(input('Enter a number:'))
asarot=d//10
ahadot=d%10
if asarot==ahadot and asarot>1 and ahadot>1:
    print ('Both tens and singles are the same and above 1')
else:
    print ('Tens and singles are not the same or not above 1')
