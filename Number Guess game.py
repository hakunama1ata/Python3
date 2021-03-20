import random
y = random.randint(1,10)
for i in range (1,5) :
    a = input("Enter a number between 1 and 10:")
    try :
        x = int(a)
    except :
        print ("Enter a valid number")
        break
    if y == x : 
        print ("You guessed it correctly in " + str(i) +" chances")
        break
    elif x < y :
        print ("Your guess is too low")
    else :
        print ("Your guess is too high")
