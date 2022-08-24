import random


flag = True
while flag:
     num = input("Enter a number:  ")

     if num.isdigit():
          print("Lets Guess!!!!! ")
          num = int(num)
          flag = False
     else:
          print("Invalid input Try again!")

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
     guess = input("Please type a number between 1 and : " + str(num) + ":")
     if guess.isdigit():
          guess = int(guess)

     if guess == secret :
          print(" You got it! ")
     else:
          print(" try again")
          count += 1
print("It took you " ,  count ,  "guesses! ")


print("Press Enter to exit ")
input()

            
