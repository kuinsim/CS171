#Suin Kim CS-171 Section 070

import sys

#Main Program
#Initialize global variables, "Placeholder" is at index 0 for each list since level starts at 1
planet = ["Placeholder", "Moon", "Earth", "Pluto", "Neptune", "Uranus", "Saturn", "Jupiter", "Mars", "Venus", "Mercury", "Sun"]
G = ["Placeholder", -1.622, -9.81, -0.42, -14.07, -10.67, -11.08, -25.95, -3.77, -8.87, -3.59, -274.13]
F = ["Placeholder", 150, 5000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 50000]
level = 1

#Define function that asks user for amount of fuel to use for that second
def ask_fuel(current_fuel):
    #Repeatedly asks user for input and tests it until it meets the requirements
    while (True):
        f = input("Enter units of fuel to use:")
        #try and except statement that checks if user input is an integer, non-negative, and is less than the max amount of current fuel
        try:
            f = int(f)
            if (f < 0):
                print("Cannot use negative fuel.")
                continue
            elif (f > current_fuel):
                print("Not enough fuel. Max Fuel:", current_fuel)
                continue
            return f
        except ValueError:
            print("Please Enter Integer Value.")

#Define function that calculates and prints results of one second of a level
def play_level(name, G, fuel):
    #global needed in order to change values of global variables
    global V
    global A
    global s
    global F
    global current_fuel
    #Calling ask_fuel(current_fuel) function in order to get value for f
    f = ask_fuel(current_fuel)
    #Calculations
    current_fuel = current_fuel - f
    V = V + G + (T * f)
    A = A + V
    s = s + 1
    #Print results after calculations
    #Making sure negative altitude is never printed
    if (A < 0):
        print("After", s, "second(s): Altitude is 0.00 meters, velocity is", round(V, 2), "m/s.")
    else:
        print("After", s, "second(s): Altitude is", round(A, 2), "meters, velocity is", round(V, 2), "m/s.")
    print("Remaining Fuel:", current_fuel, "units.")

#Main program
print("Welcome to Lunar Lander Game.")
#User keeps playing until they beat every level
while (level <= 11):
    #A, V, T, s, and current_fuel are reset to respective values at the beginning of every level attempt
    A = 50
    V = 0.00
    T = 0.10
    s = 0
    current_fuel = F[level]
    #User decides if he or she wants to play or not
    play = input("Do you want to play level " + str(level) + "? (yes/no)")
    #Plays level if user says "yes"
    if (play.lower() == "yes"):
        #Displays initial values for level user is on
        print("Entering Level", level)
        print("Landing on", planet[level])
        print("Gravity is", G[level], "m/s^2")
        print("Initial Altitude:", A, "meters")
        print("Initial Velocity:", V, "m/s")
        print("Burning a unit of fuel causes", T, "m/s slowdown.")
        print("Initial Fuel Level:", (F[level]),"\n")
        print("GO")
        #User plays level until he or she lands successfully or crashes
        while (A > 0):
            #Calling play_level(name, G, fuel) function
            play_level(planet[level], G[level], F[level])
        #Determines if user lands successfully and passes level or crashes based on V
        if ((V <= 2) and (V >= -2)):
            print("Landed Successfully.")
            level+=1
        else:
            print("Crashed!")
    #Exits game and prints how many levels user beat if he or she says "no"
    elif (play.lower() == "no"):
        print("You made it past", (level - 1), "level(s).\nThank you for playing.")
        sys.exit()






