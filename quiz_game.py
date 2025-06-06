print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print("Okay! Let's play ")  
score = 0  

answer = input("What does CPU stands for? ")
if answer == "Central Processing Unit":
    print('your answer is correct')
    score += 1
else:
    print('your answer is incorrect')

answer = input("What does GPU stands for? ")
if answer == "Graphics Processing Unit":
    print('your answer is correct')
    score += 1
else:
    print('your answer is incorrect') 

answer = input("What does RAM stands for? ")
if answer == "Random Access Memory":
    print('your answer is correct')
    score += 1
else:
    print('your answer is incorrect')

answer = input("What does PSU stands for? ")
if answer == "Power Supply":
    print('your answer is correct')
    score += 1
else:
    print('your answer is incorrect')    

print("You got " + str(score) + " questions correct!")    
print("You got " + str((score/4)*100) + "%")    