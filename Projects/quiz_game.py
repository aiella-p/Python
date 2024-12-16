# quiz game by python...

questions = ("How many elements are in the periodic table ?: ",
             "Which animal lays largest eggs?:",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is hottest?:" ) # tuple of question

options = (("A. 116", "B. 117 ", "C. 118 ", "D. 119 "),
           ("A. Whale","B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Diaxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
# 2d tuple of options...for quiz of 5 questions,each inner tuple 
# consits 4 elements

answers = ("C","D","A","A","B") # We have a Tuple of correct answers(Not Changable- Immutable)

guesses = [] # A list of guesses...we wiil be appending our guesses to list
# that why we are using list[], bcoz user can change his options of answer
# bcoz list is changable...that is why we are NOT using here Tuple(is immutable)

score = 0
question_num = 0 # This variable will keep track on what number question we are on...!!
 
for question in questions:
    print("------------------------------")
    print(question)

    for option in options[question_num]:
     print(option)    
     
    guess = input("Enter (A,B,C,D):").upper() # Before iterating the question numbers ....we will ask the 
    # user for guess...!
    guesses.append(guess) # We will take our list of guesses use the append method add our guess to our 
    # list    
    if guess == answers[question_num]: # If guess equal to answers tuple[index of question numbers]...user
    # guessed right answer...!!   
       score += 1
       print("CORRECT !")
    else:
       print("INCORRECT !")
       print(f"{answers[question_num]} is the correct answer")   
    question_num += 1

print("----------------------------")
print("        RESULTS             ")
print("----------------------------")

for answer in answers:
       print(answer, end=" ")
print()

print(guess, end=" ")
for guess in guesses:
       print(guess, end=" ")
print()      

score = int(score / len(questions) *100)
print(f"Your score is: {score}%")