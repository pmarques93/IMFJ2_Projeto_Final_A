from floatation import *
from springs import *

# main #########################################################################
def main():

    user_input = ''

    while (str(user_input) != '1' or '2' or '3'):
        
        
        # Print Options
        print(" What problem do you want to solve?")
        print(" 1. Floatation")
        print(" 2. Springs")
        print(" 3. Exit program")

        # Asks user for input
        user_input = input('>')

        # Options
        if (str(user_input) == '1'):
            run_floatation()
            print(" Bye bye!")
            break
        elif (str(user_input) == '2'):
            run_springs()
            print(" Bye bye!")
            break
        elif (str(user_input) == '3'):
            print(" Bye bye!")
            break
        else:
            print("\n Please choose one of the following options\n")


# Run main
main()