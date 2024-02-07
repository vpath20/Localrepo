print('Lets play KBC')
questions = ['What is the national animal of India?']
options = ['A.Tiger', 'B.Crocodile', 'C.Zebra', 'D.Lion']
print(questions)
print(options)

answer = input("Enter the correct option")

print(str.upper(answer))
if(str.upper(answer) == "A"):
    print('Correct Answer: You win 1 crore')
else:
    print("Wrong Answer: Better luck next time")




questions = [["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",4],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",1],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3],["Which language was used to create facebook", "Python", "Javascript", "French", "PHP", "None",3]
    ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(questions[0])
    print(f"a. {question[1]} b. {question[2]}")
    print(f"c. {question[3]} d. {question[4]}")
    reply = int(input("Enter your answer (1-4) "))

    if reply == question[-1]:
        print(f"correct answer. you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000

    else:
        print("Wrong answer!")
        print("you won : ", money)
        break






