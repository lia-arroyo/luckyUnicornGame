# Lucky Unicorn Game Version 3 - fully working program
# Created 29/07/18
# AFTER USABILITY TESTING

''' v2 changes:
    - added instructions and introduction at the beginning
    - add 'rounds played' and 'balance' counter
    ~
    v3 changes:
    - added more whitespace ( more print() )
    - text decoration / format
    - include dollar signs and ensure all money input/output are 2 decimal places

'''

''' modules '''

# random module
import random

''' functions '''

# integer checking function below
def intcheck(question,low,high):
    valid = False
    while not valid:
        error = "Yikes!!! Please enter a valid integer between {} and {}".format(low,high)
        try:
            response = int(input(question))
            if low <= response <= high:
               return response
            else:
                print()
                print(error)
                print()
                
        except ValueError:
            print()
            print(error)
            print()

# token statements / decorations
def token_statement(statement,char):
    print()
    print(char*len(statement))
    print()
    print(statement)
    print()
    print(char*len(statement))
    print

''' main routine '''

# instructions / introduction

print("------------------ THE LUCKY UNICORN GAME ------------------")
print("To play, enter an amount of money between $1 and $10 that you'd like to begin with.")
print()
print("Each round costs $1. The game will randomly generate a token which will either be a donkey, a horse, a zebra or a unicorn.")
print()
print("Payouts:")
print("- Donkey: $0")
print("- Horse / Zebra: $0.50")
print("- Unicorn: $5")
print()
print("Lets Play!")
print()
# Ask user for how much money they'd like to begin with. (min $1, max $10)
total_count = intcheck("How much money do you want to begin with? $",1,10)

# Rounds played counter
rounds = 0

# Loop until game ends

keep_going = ""
while keep_going == "":

    # tokens - consists of 10 items to decrease odds of generating a unicorn

    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # to randomly generate a token from the list above
    token = random.choice(tokens)
    print("")
    print()
    
    # Adding totals correcty depending on token generated
    if token == "unicorn":
        token_statement("$$$ Congratulations! You got a {} and won $5.00 $$$".format(token),"$")
        total_count += 5 # wins $5

    elif token == "donkey":
        token_statement("*** Sorry! You got a {} and did not win anything this round. ***".format(token),"*")
        total_count -= 1 # wins $0, paid $1

    else:
        token_statement("~~~ Congratulations! You got a {} and won 50c. ~~~".format(token),"~")
        total_count -= 0.5 # wins 50c, paid $1 to play so loses 50
    print()
    print("You have ${:.2f} left to play with.".format(total_count))
    
    # Balance and Rounds played counter
    print()
    rounds += 1
    print("Rounds Played: {} | Balance: ${:.2f}".format(rounds,total_count))

    # End game mechanics
    if total_count < 1:
        print()
        print("Sorry, you don't have enough money to continue. Game over.")
        keep_going = "end"

    else:
        print()
        keep_going = input("Press <enter> to continue or enter any key to quit: ")

# Farewell message. Game over
print("------------------------------------")
print()
print("Thanks for playing Lucky Unicorns!")
print()
print("Rounds Played: {} | Balance: ${:.2f}".format(rounds,total_count))
print()

