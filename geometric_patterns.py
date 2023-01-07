"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Code template for geometric patterns.
"""
from math import pi


def printtaus(x):
    """Printtaa käytety kuvion nimen ja arvot"""
    print(f"The circumference is {x*4:.2f}")
    print(f"The surface area is {x*x:.2f}")
def printtaus2(x,y):
    """Printtaa käytety kuvion nimen ja arvot"""
    print(f"The circumference is {x*2+y*2:.2f}")
    print(f"The surface area is {x*y:.2f}")
    
def testaus(t):
    """FUnktio testaaa syötetyn luvun oleva isompi ku 0"""
    while True:
        x = float(input(t))
        if x > 0:
            
            return x
    
        
def square():
    """ Määrittää neliön pita-alan ja piirin"""
    sivu = testaus("Enter the length of the square's side: ")
    printtaus(sivu)

    

def rectangle(): 
    """Määrittää suorakulmion A ja piiri"""
    sivu1 = testaus("Enter the length of the rectangle's side 1: ")
    sivu2 = testaus("Enter the length of the rectangle's side 2: ")
    printtaus2(sivu1,sivu2)
   
    

def circle():
    """Määrittää ympyrän piirin ja pinta-alan"""
    sade = testaus("Enter the circle's radius: ")
    
    print(f"The circumference is {sade*2*pi:.2f}")
    print(f"The surface area is {pi*(sade*sade):.2f}")
    
    
def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()

        elif answer == "r":
           rectangle()
        elif answer == "c":
            circle()
        elif answer == "q":
            return
            
        
        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()
def main():
    menu()
    print("Goodbye!")
    

if __name__ == "__main__":
    main()
