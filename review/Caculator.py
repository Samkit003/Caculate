#creat the program by thar htoo san
#Caculator
#Caculate the Area of Circle, the Hypotenuse, the adsobulate, the radius of circle
#17.1.2023

import math
def new_game():
    
    print("This is a Caculator and it can caculate the Area of Circle, the Hypotenuse, the adsobulate, the radius of circle ")

    print("Hypotenuse for H:",
                 "Area of circle for A:",
                 "radius of a circle for R:",
                 "absobulate value of V:")
    question = input("You can put a word as you wish to caculate:")

    if question == "h" or question == "H":
        a = float(input("Enter side A:"))
        b = float(input("Enter side B:"))
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        print(f"Side C = {round(c, 2)}")

    if question == "a" or question == "A":
        r = int(input(" Enter the Radius: "))
        m = 3.14 * pow(r,2)
        print(f"Your Area is = {round(m,5)}")

    if question == "r" or question == "R":
        radius = float(input("Enter the radius of a circle:"))
        w = radius // 2
        print (f"Your radius is = {(w)}")

    if question == "v" or question == "V":
        d = int(input("First value:"))
        e = int(input("Second value:"))
        f = abs(d+e)
        print(f"Your value is = {(f)}")

def play_again():
    response = input("Do you wanna caculate ? (yes or no):")
    response = response.upper()

    if response == "YES" or response == "y" or response == "Y":
        return True
    else:
        return False
#----------------------

while play_again():
    new_game()

print("BYE")
    




    
    
                 
