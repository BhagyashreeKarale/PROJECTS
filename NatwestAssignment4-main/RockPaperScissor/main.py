import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
while True:
    user1=input("Enter your name:\n")
    playwith=input("Enter your choice\n1 to play with friend \n2 to play with computer\n")
    flag=True
    while flag==True:
        if playwith=="1":
            user2=input("Enter your friend's name:\n")
            flag=False
        elif playwith=="2":
            user2="computer"
            flag=False
        else:
            playwith=input(("Enter valid input: "))

    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
    user1_choice = int(input(user1 +"'s turn: "))
     
    # looping until user enter invalid input
    while user1_choice > 3 or user1_choice < 1:
        user1_choice = int(input("Enter valid input: "))
         
 
    # initialize value of user1_choice_name variable
    # corresponding to the user1_choice value
    if user1_choice == 1:
        user1_choice_name = 'Rock'
    elif user1_choice == 2:
        user1_choice_name = 'paper'
    else:
        user1_choice_name = 'scissor'
         
    # print user1 choice
    print("user user1_choice is: " + user1_choice_name)
    print("\nNow its "+user2+"'s turn.")
 
    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    if user2=="computer":
        user2_choice = random.randint(1, 3)
    else:
        print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")
        user2_choice = int(input(user2 +"'s turn: "))
        while user2_choice > 3 or user2_choice < 1:
            user2_choice = int(input("Enter valid input: "))
    # initialize value of user2_choice_name
    # variable corresponding to the choice value
    if user2_choice == 1:
            user2_choice_name = 'Rock'
    elif user2_choice == 2:
            user2_choice_name = 'paper'
    else:
            user2_choice_name = 'scissor'
         
    print(user2+"'s choice is: " + user2_choice_name)
    
    print(user1_choice_name + " V/s " + user2_choice_name)
 
    # condition for winning
    if((user1_choice == 1 and user2_choice == 2) or
      (user1_choice == 2 and user2_choice ==1 )):
        print("paper wins => ", end = "")
        result = "paper"
         
    elif((user1_choice == 1 and user2_choice == 3) or
        (user1_choice == 3 and user2_choice == 1)):
        print("Rock wins =>", end = "")
        result = "Rock"
    elif user1_choice==user2_choice:
        result="none"
    else:
        print("scissor wins =>", end = "")
        result = "scissor"
 
    # Printing who wins
    if result == user1_choice_name:
        print("<== "+user1+" wins ==>")
    elif result==user2_choice_name:
        print("<== "+user2+" wins ==>")
    else:
        print("Match Drawn")
    print("Do you want to play again? (Y/N)")
    ans = input()
    if ans!="y" or ans!="Y":
        break
