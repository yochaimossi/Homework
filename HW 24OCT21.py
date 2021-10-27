### Q2


def split(mat):
    return [char for char in mat]

mat = input ("Enter mathematical expression to check if true or false:")
split(mat)
num1 = int(mat[0])
num2 = int(mat[2])
sum = int(mat[4])

print (bool(num1+num2 == sum))

### Q3

print(a_list)

length = len(a_list)
middle_index = length//2

first_half = a_list[:middle_index]

print(first_half)

### Q4

string_list = ['hello','pen','python','word of coding']

for i in range(len(string_list)):

    string_list[i] = string_list[i].upper()

print(string_list)

### Q5

string_list = ['hello','pen','python','word of coding']

for i in range(len(string_list)):
    if len(string_list[i]) < 4:
        print (string_list[i],"is shorter than 4 letters")
        break
    else:
        continue
### Q6


fullname = input ("Please enter your full name:")

first_five=fullname[0:5]

print ('First five characters:',first_five)

strlen = len(fullname)
third = strlen // 3
first_third = fullname[:third]

print ('First third of characters:',first_third)

a_count=fullname.count('a')

print ('The character A appears in the name',a_count,'times')

b_count=fullname.count('b')

print(bool(b_count >0))

splitname = fullname.split(' ')

fname = splitname [0]
lname = splitname [1]

print ("First name is:",fname)
print ("Last name is:",lname)

rfname = splitname [1]
rlname = splitname [0]

print ("Reverted first name is:",rfname)
print ("Reverted last name is:",rlname)

upperlname = splitname[1].upper()

print ("Last name is:",upperlname)

len_first_name = len(fname)
middle_char = len_first_name//2
if middle_char%2 == 0:
    new_name = fname [:middle_char]+fname[middle_char+1:]
else:
    new_name = fname[:middle_char-1] + fname[middle_char + 1:]

print ("The new name is",new_name)

print ('Your new name is :',new_name,lname)


### Q7

s = 'Hello World!'
c = 'o'
print([pos for pos, char in enumerate(s) if char == c])

first= s.find('o')
print (s[0:first])

second= s.rfind('o')

print (s[second+1:])

### Q8

str = "Hello World!"

no_o = str.replace('o','')

print (no_o)

### Q9

num_list = [8,1000,-3,2,5]

sum = 0

for i in range (0,len(num_list)):
    sum += num_list[i]

print (sum)

print ("The biggest value in the list is:",max(num_list))
print ("The smallest value in the list is:",min(num_list))

avg = float(sum/len(num_list))

print ("The avergae is:",avg)

middle_num = len(num_list)//2

no_middle = num_list [:middle_num]+num_list[middle_num+1:]

print ('No middle number',no_middle)

num_list.sort()

print (num_list)
print ()

for i in range (0,5):
    print (num_list)

print (num_list[1:])

for i in range (0, len(num_list)):
    if num_list[i] < avg :
        print (num_list[i],'',end='')
    else:
        continue


### Q10



str = input(("Enter a list of numbers seperated by a comma:"))

newlist=str.split(',')

biggest = int(newlist[0])

for i in range (1, len(newlist)):
    if biggest < int(newlist[i]) :
        biggest = int(newlist[i])
print (biggest)



