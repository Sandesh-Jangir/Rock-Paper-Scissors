import random

Base_List = ['rock', 'paper', 'scissors']

print("Welcome To Rock Paper Scissors!!")
# Mainloop
while True:
    User_Command = input("User: ")
    Computer_Output = random.choice(Base_List)

    if User_Command.lower() in Base_List:
        print("Computer:", Computer_Output)

        if User_Command == Computer_Output:
            print("Tied!!!!!!\n----------------")

            
        elif User_Command.lower() == "rock" and Computer_Output == "paper":
            print("Computer Won!\n----------------")

        elif User_Command.lower() == "rock" and Computer_Output == "scissors":
            print("You Won!\n----------------")

        elif User_Command.lower() == "paper" and Computer_Output == "rock":
            print("You Won!\n----------------")

        elif User_Command.lower() == "paper" and Computer_Output == "scissors":
            print("Computer Won!\n----------------")

        elif User_Command.lower() == "scissors" and Computer_Output == "rock":
            print("Computer Won!\n----------------")

        elif User_Command.lower() == "scissors" and Computer_Output == "paper":
            print("You Won!\n----------------")


    elif User_Command.lower() == "exit":
            print("Thanks For Playing Rock Paper Scissors")
            break

    else:
        print("Please Enter Valid Value")
