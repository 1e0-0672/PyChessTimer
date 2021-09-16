import random


while True: 
    
    MAX_VALUE = input('pick a number that would be your highest number in this guessing game for! ex. 0 - 1,000}\n')
    
    try: 
        MAX_VALUE = int(MAX_VALUE)
    except: 
        print('That is not a number, try again')
        #if MAX_VALUE < 0:
            #print ('that is below zero, try again')
        continue
    if MAX_VALUE < 0:
        print('Only positive numbers')
        continue
    break

    
random_num = (random.randint(0,MAX_VALUE))


print (random_num)

while True:

#    x = input('enter a number between 0 and .fomat(random_num) \n')
    x = input("enter a number between 0 and {}\n".format(MAX_VALUE))
    try:
        x = int(x)
    except:
        print('That is not a number, try again')
        continue
        
    if x < random_num:
        print ('too low')
        continue
    if x > random_num:
        print ('too high')
        continue
    if x == random_num:
        print ('YOU GOT IT')
    break
    


    

