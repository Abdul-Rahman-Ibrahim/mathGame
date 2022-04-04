import random
import os

def getUserPoint(userName):
    
    try:
        file = open("userScores.txt", "r")
        for line in file:
            content = line.split(",")
            if userName in content:
                return content[1]
        
        file.close()    
        return "-1"
     
    # creates new text file if the text file not exist
    except IOError:
        file = open("userScores.txt", "w")
        file.close()
        return "-1"
        

def updateUserPoint(newUser, userName, score):
    
    if newUser:
        file = open("userScores.txt", "a")
        file.write(userName+", "+str(score)+"\n")
    else:
        tempFile = open("userScores.tmp", "w")
        oldFile = open("userScores.txt", "r")
        
        for line in oldFile:
            if userName in line:
                tempFile.write(userName+", "+str(score)+"\n")
            else:
                tempFile.write(line+"\n")
        tempFile.close()
        oldFile.close()
        
        os.remove("userScores.txt")
        os.renames("userScores.tmp", "userScores.txt")

   
def generateQuestion():
    
    operatorDict = {1:" + ",2:" - ",3:"*",4:"/",5:"**"}
    operandList = list(range(5)) #intentionally filling the list with 5 entries
    operatorList = list(range(4)) #intentionally filling the list with 4 entries
    questionString = ""
    
    # filling operandList with random integers from 1 to 9
    for i in range(len(operandList)):
        operandList[i] = random.randint(1, 9)
    
    # filling the operatorList with random operators from operatorDict
    for i in range(len(operatorList)):
        operatorList[i] = operatorDict[random.randint(1, 5)]
    
    # modifying opertorList to remove replace one of any two consecutive "**"
    count = 0
    for i, operator in enumerate(operatorList):
        if operator == "**":
            count += 1
            if count > 1:
                new_operator = operatorDict[random.randint(1, 4)]
                operatorList[i] = new_operator
                count = 0
            continue
    
    for num, operator in zip(operandList, operatorList):
        questionString += str(num) + operator
    questionString += str(operandList[-1])
    
    
    outputQuestionString = questionString.replace("**", "^")
    print("\n")
    print("Solve:", outputQuestionString)
    
    return questionString
         

def getUserAnswer():
    
    userAnswer = input("Enter Answer ")
    
    return userAnswer

def checkAnswer(userAnswer, questionString):
    
    try:
        if int(userAnswer) == round(eval(questionString)):
            print("Correct!")
            return 1
        
        else:
            print("Incorrect! Correct answer is", end=" ")
            print(round(eval(questionString)))
            return 0
    
    # prompts user if the answer entered is a string instead of a number
    except: 
        print("Your entry is invalid")
        userAnswer = input("Enter answer as integer ")
        score = checkAnswer(userAnswer, questionString)
        return score
