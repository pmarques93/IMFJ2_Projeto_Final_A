# program_loop_run_floatation ##################################################
def run_floatation():

    obj_density = 0
    obj_length  = 0
    obj_center  = 0
    obj_volume  = 0
    obj_mass    = 0
    gravity     = 0
    flu_density = 0

    gravity_force   = 0
    submerse_volume  = 0

    bottom_distance  = 0
    center_of_mass_distance = 0

    # Simulation parameters
    # Asks for user input and saves the answers
    gravity     = float(input(" Insert gravity: "))
    flu_density = float(input(" Insert fluid density: "))
    obj_density = float(input(" Insert cube density: "))
    obj_volume  = float(input(" Insert cube volume: "))
    
    # Sets cube mass
    obj_mass = obj_density * obj_volume

    # program loop
    running = True
    while (running):

        # Refresh results
        # Object length
        obj_length = obj_volume ** (1/3)
        obj_center = obj_length / 2

        # Gravity force
        gravity_force = obj_mass * gravity

        # Submerse Volume
        submerse_volume = gravity_force / (flu_density * gravity)

        # Buoyance Height
        bottom_distance = -submerse_volume / (obj_length * obj_length)

        # Center of mass distance
        center_of_mass_distance = obj_center + bottom_distance

        # Prints commands
        print("\n_______________________________________________________________")
        print("\n List of commands: 'set gravity x', 'set fluid_density x', ")
        print("                   'set cube_density x', 'set cube_volume x'")
        print("                   'set cube_mass x ', 'exit'")

        # Prints results
        print(f"\n Object properties: Mass = " + "%.2f" % obj_mass + " kg, Density = " + "%.2f" % obj_density + " kg/m3, Volume = " + "%.2f" % obj_volume + " m3.")
        print(f" Fluid has a density of " + "%.2f" % flu_density + " kg/m3, Gravity is " + "%.2f" % gravity + " m/s2.\n")
        print(f" Center of mass distance: " + "%.2f" % center_of_mass_distance + " m from the surface.\n")

        # Prints the cube
        if(center_of_mass_distance > 0):
            buoying()

        elif(center_of_mass_distance < - obj_length):
            submerse()

        elif(center_of_mass_distance < 0):
            underwater()

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

            elif (user_variable.lower() == "fluid_density"):
                flu_density = float(user_value)

            elif (user_variable.lower() == "cube_density"):
                obj_density = float(user_value)

                # Object mass
                obj_mass = obj_density * obj_volume

            elif (user_variable.lower() == "cube_volume"):
                obj_volume = float(user_value)

                # Object mass
                obj_mass = obj_density * obj_volume

            elif (user_variable.lower() == "cube_mass"):
                obj_mass = float(user_value)    

                # Object volume
                obj_volume = obj_mass / obj_density

        # Breaks the gameloop
        elif user_split_input.lower() == "exit":
            running = False
            
        else:
            print("\n Invalid command")


def buoying():

    print("     _____    ")
    print("    |     |   ")
    print("  vv|vvvvv|vv ")
    print("    |_____|   \n")

def underwater():

    print("     _____     ")
    print("  vv|vvvvv|vv  ")
    print("    |     |    ")
    print("    |_____|    \n")

def submerse():

    print("  vvvvvvvvvvv  ")
    print("    |     |    ")
    print("    |     |    ")
    print("    |_____|    \n")

