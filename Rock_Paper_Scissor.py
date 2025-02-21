import random

computer_score = 0
your_score = 0

print("\n\t\t**************** Wellcome *******************\n")
print("NOTE:~\n\t1 --> is for \"ROCK\" \n\t2 --> is for \"PAPER\" \n\t3 --> is for \"SCISSOR\" \n")

def game():
    
    global computer_score, your_score
    
    computer = random.choice([1, 2, 3])
    you = int(input("Enter a number according to the note that are given: "))

    print(f"YOU chose {you} and COMPUTER chose {computer}!")


    if(computer == you):
        print("\tOOPs it's Tie")
    else:
        if(computer == 1 and you == 3):
                        print("\tCOMPUTER is the winner")
                        computer_score+=1
        elif(computer == 3 and you == 1):
                        print("\tYOU are the winner")
                        your_score+=1
        elif(computer == 2 and you == 3):
                        print("\tYOU are the winner")
                        your_score+=1
        elif(computer == 3 and you == 2):
                        print("\tCOMPUTER is the winner")
                        computer_score+=1
        elif(computer == 2 and you == 1):
                        print("\tCOMPUTER is the winner")
                        computer_score+=1
        elif(computer == 1 and you == 2):
                        print("\tYOU are the winner")
                        your_score+=1
        else:
            print("OOPs! You can only choose between 1 2 & 3")    
                        
    print("\n")  
    
def final_score():         
    print("\t\tCOMPUTER SCORE \t\t|\t\t YOUR SCORE")
    print(f"\t\t\t{computer_score} \t\t|\t\t     {your_score}")     

game()
        
choice = input("Do you want to play again enter 'Yes' or 'No': ")
print("\n")   

while(choice.lower() == "yes"):
        game()
        choice = input("Do you want to play again enter 'Yes' or 'No': ")
        print("\n")   
       
print("FINAL SCORE:~")       
print("\n")          
final_score()       
        
        
        