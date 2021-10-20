### Q2

def function ():
    print (index)
for index in range (1,101):
    function()


### Q3

x=int(input("Enter number here:"))

def function (x=10):
    print (index)

for index in range (1,x+1):
    function()

### Q4

import random
i = 1
lucky_card= random.randint (1,100)


while True:
    user=int(input("Please enter a number:"))

    if user > lucky_card:
     print ("Too high")
     i += 1
    elif user < lucky_card:
     print ("Too low")
     i += 1
    else:
     print ("Bingo")
     print ("Total tries:",i)
     break


### Q5

import random

highest=1

for index in range (1,4):

    i = 1
    lucky_card= random.randint (1,100)

    if highest < lucky_card:
        highest = lucky_card

    while True:
        user=int(input("Please enter a number:"))

        if user > lucky_card:
         print ("Too high")
         i += 1
        elif user < lucky_card:
         print ("Too low")
         i += 1
        else:
            print ("Bingo")
            print ("Total tries:",i)
            break

print ("The highest cards is:",highest)