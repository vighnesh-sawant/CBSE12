#Write a random number generator that generates random numbers between 1 and 6
import random 
while True:
    choice = input("Do you want to continue to generate? (Y/N)")
    num=random.randint(1,6)
    
    if choice.upper() == "Y":
        print(num)
    else:
        break