# Check Your Knowledge on Technical Abbreviation#
print("Welcome to the Technical Abbreviation Quiz")

doplay = input("Do you want to play? ")

if doplay.lower() != "yes":
    quit()

print("Okay Let's Start the Quiz! ")

point = 0

answer = input("What does CPU Stands for? ")

if answer.lower() == "central processing unit":
    print('Correct Answer!')
    point += 1
else:
    print("Wrong Answer!")

answer = input("What does RAM Stands for? ")

if answer.lower() == "random access memory":
    print("Correct Answer!")
    point += 1
else:
    print("Wrong Answer!")

answer = input("What does ROM Stands for? ")

if answer.lower() == "read only memory":
    print("Correct Answer!")
    point += 1
else:
    print("Wrong Answer!")

answer = input("What does UPS Stands for? ")

if answer.lower() == "uninterruptible power supply":
    print("Correct Answer!")
    point += 1
else:
    print("Wrong Answer!")

answer = input("What does GPU Stands for? ")

if answer.lower() == "graphics processing unit":
    print("Correct Answer!")
    point += 1
else:
    print("Wrong Answer!")
# Passing percent is 60#
print("Your Total Score for the Quiz is!: " + str(point))
percent = (point/5)*100
if percent >= 60:
    print("Congrats!, You got " + str(percent) + "%")
else:
    print(" Sorry!, You only got " + str(percent) + "% Try again Later!")
