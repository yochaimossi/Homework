import random
import re
import time

#ask Name
name=input("Enter your name:")
print(f"Hi {name} , Let's start the game")

print("\t ***Word Guessing Game*** ")
print ('Enter lower case letters only')
print ('Enter each letter only once')

random_list = [['always','be','yourself'],['be','the','change'],
               ['believe','in','yourself'],['change','is','good'],
               ['competition','fuels','growth'],['dreams','come','true'],
               ['just','be','awesome'],['life','is','awesome'],
               ['never','look','back'],['nothing','is','impossible']]


chosen_quote = random.choice(random_list)


new_quote = chosen_quote[0]+' '+chosen_quote[1]+' '+chosen_quote[2]
#print(new_quote)
new_quote_blanks = re.sub('[a-zA-Z]','_',new_quote)
print (new_quote_blanks)


score = 0

start_time = time.time()

while new_quote_blanks != new_quote:
    char = str(input("Enter a letter to check if it's a part of the quote:"))
    if char in new_quote:
        for g in range (len(new_quote)):
            if char == new_quote[g]:
                 new_quote_blanks = new_quote_blanks[:g]+char+new_quote_blanks[g+1:]
        print(new_quote_blanks)
        score += 5


    else:
     print ("Wrong guess,try again!")
     print(new_quote_blanks)
     score -=1
     continue
elapsed_time = time.time()-start_time
print ("Congrats! You finished the game with a score of:",score," it took you",int(elapsed_time),"seconds to complete")
if int(elapsed_time) <= 30:
    score += 100
    print ("Because you finished the game in less than 30 seconds you receive a 100 point bonus and your new score is",score)





























