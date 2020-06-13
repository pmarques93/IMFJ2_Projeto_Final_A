# program_loop_run_floatation ##################################################
def run_floatation():

    obj_mass    = 0
    obj_density = 0
    obj_length  = 0
    obj_volume  = 0
    gravity     = 0
    flu_density = 0

    grav_force  = 0
    impulse     = 0

    height      = 0

    # Simulation parameters
    # Asks for user input and saves the answers
    gravity     = float(input(" Insert gravity: "))
    flu_density = float(input(" Insert fluid density: "))
    obj_density = float(input(" Insert cube density: "))
    obj_volume  = float(input(" Insert cube volume: "))
    
    # program loop
    running = True
    while (running):

        # Object volume
        obj_length = obj_volume ** (1/3)

        # Object mass
        obj_mass = obj_density * obj_volume

        # Gravity force
        grav_force = obj_mass * gravity

        # Impulse
        impulse = flu_density * gravity * obj_volume

        # Height
        height = (grav_force / (flu_density * gravity)) / (obj_length * obj_length)

        # Prints commands
        print("\n_______________________________________________________________")
        print("\n List of commands: 'set gravity x', 'set fluid_density x', ")
        print("                   'set object_density x', 'set object_volume x'")
        print("                   'exit'")

        # Prints results
        print(f"\n Object properties: Mass = {obj_mass} kg, Density = {obj_density} kg/m3, Volume = {obj_volume} m3.")
        print(f" Fluid has a density of {flu_density} kg/m3, Gravity is {gravity} m/s2.")
        print(f"\n The object would float at {height} m.\n")

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

            elif (user_variable.lower() == "object_density"):
                obj_density = float(user_value)

            elif (user_variable.lower() == "object_volume"):
                obj_volume = float(user_value)

        # Breaks the gameloop
        elif user_split_input.lower() == "exit":
            running = False
            
        else:
            print("\n Invalid command")
