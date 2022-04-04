import myPythonFunctions as mf

print("Welcome To My Math Operations Game")
print("Solve the following math questions")
print("NB: If answer is decimal, ROUND to the nearest INTEGER")

try:
    userName = input("Enter your name ")
    
    userScore = mf.getUserPoint(userName)
    
    if userScore == "-1":
        newUser = True
        userScore = 0
    else:
        newUser = False
    
    userChoice = 0
    while userChoice != -1:
        
        questionString = mf.generateQuestion()
        if eval(questionString) > 50000 or eval(questionString) < -50000:
            continue
        userAnswer = mf.getUserAnswer()
        score = mf.checkAnswer(userAnswer, questionString)
        
        #updates the user's score
        userScore += score
        userChoice = int(input("To exit, enter -1. To play again, enter any value "))
    
    mf.updateUserPoint(newUser, userName, userScore)

except:
    print("An error occured. Program will exit") 
   
