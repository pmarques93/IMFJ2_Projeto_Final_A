# program_loop_run_springs #####################################################
def run_springs():

    gravity         = 0
    obj_mass        = 0
    base_length     = 0
    constant        = 0
    stretch         = 0

    grav_force      = 0

    # Simulation parameters
    # Asks for user input and saves the answers
    gravity     = float(input(" Insert gravity: "))
    obj_mass    = float(input(" Insert object mass: "))
    base_length = float(input(" Insert spring length: "))
    constant    = float(input(" Insert spring constant: "))
    
    # program loop
    running = True
    while (running):

        # Gravitic force
        grav_force = -gravity * obj_mass

        # Stretch
        stretch = (grav_force - constant * base_length) / -constant

        # Prints commands
        print("\n_______________________________________________________________\n")
        print(" List of commands: 'set gravity x', 'set mass x', ")
        print("                   'set constant x', 'set length x'")
        print("                   'exit'")

        # Prints results
        print(f"\n Object properties: Mass = " + "%.2f" % obj_mass + " kg, Gravity is " + "%.2f" % gravity + " m/s2.")
        print(f" Base spring length " + "%.2f" % base_length + " m, Constant is " + "%.2f" % constant + " N/m.")
        print(f"\n The spring would stretch to {stretch} m.\n")

        # New inputs
        # Gets user input and splits the string
        user_input  = input(">")
        user_split_input = user_input.split(' ')[0]

        if user_split_input.lower() == "set":
            # Gets user second and third variables
            user_variable = user_input.split(' ')[1]
            user_value    = user_input.split(' ')[2]

            if (user_variable.lower() == "gravity"):
                gravity = float(user_value)

            elif (user_variable.lower() == "mass"):
                obj_mass = float(user_value)

            elif (user_variable.lower() == "length"):
                base_length = float(user_value)

            elif (user_variable.lower() == "constant"):
                constant = float(user_value)

        # Breaks the gameloop
        elif user_split_input.lower() == "exit":
            running = False
            
        else:
            print("\n Invalid command")
