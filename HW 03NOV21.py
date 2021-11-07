### Q1
def isDictKeysAlpha (d):
    for key in d:
        print(key.isalpha())

dict = {'Danny' : 42 , 'Ronny' : 35,'Benny' : 41 , 'Avi' : 42}

isDictKeysAlpha (dict)

### Q2

def popByValue (d,v):

    keys_to_remove = [k for k, v in d.items() if v == val]
    for key in keys_to_remove:
         d.pop(key)
    print(f'removed subjects who have the grade {val}:',keys_to_remove)




val = 89
d = { 'Physics': 91, 'Chemistry': 89, 'Math': 89 }

popByValue(d,val)
print (f"The list of subjects who don't have the grade {val} are:",d)

### Q3

def compareDict (a_dict,b_dict):
    res = a_dict==b_dict
    print(res)

a_dict = {'Danny' : 42 , 'Ronny' : 35 ,'Benny' : 41 , 'Avi' : 42 ,'Johnny' : 35}
b_dict = {'Benny' : 41 , 'Ronny' : 35 ,'Danny' : 42 , 'Avi' : 42 ,'Johnny' : 35}

compareDict(a_dict,b_dict)


### Q4

def newList (list1,list2):
    if len(list1) != len(list2):
        return None
    if (len(set(list1)) != len(list1)):
        return None
    else:
        dictionary = dict(zip(list1, list2))
        print(dictionary)


keys = ['a', 'b', 'c']
values = [1, 2, 3]

newList (keys,values)