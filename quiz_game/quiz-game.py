#Create a program that asks user a bunch of questions, then if they answer the right thing, add 1 to their score and at the end of the program print their score on the screen.

score = 0

answer = input("Whats the name of the program creator? ")
if answer == "Rodrigo":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = int(input("How many fingers a human hand has? "))
if answer == 5:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("CPU stands for ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("christmas is good yes or not? ")
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("Your score is ", score,"/4")