import random
print("Rock, Paper, Scissors, Shoot!")


# ASK for a user input
# source: https://docs.python.org/3/library/functions
x = input("Please choose one of either 'rock', 'paper', or scissors': ")
print(x)
# At this point in time, we have tested and confirmed this section, let's commit it.

# Validate the user input
if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()


# Generate a computer choice
# some python capabilites are nested inside libraries called modules
# got inspiration for this code from stackoverflow.com/questions/306400
l = ['rock', 'paper', 'scissors']
r = random.choice(l)
print("The computer chooses:", r)

# Determine a winner and display results
if x == r:
    print("Tie!")
elif (x == "rock"):
   if r == "scissors":
       print("User wins!")
    else
        print("Computer wins!")
elif (x == "paper"):
   if r == "scissors": 
       print("Computer wins!")
    else
        print("User wins!")
elif (x == "scissors"):
   if r == "paper": 
       print("User wins!")
    else
        print("Computer wins!")

