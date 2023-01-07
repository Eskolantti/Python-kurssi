"""
Antti Eskola 151210040
Ohjelmointi 1 / Programming 1
Trangle's Area when the Sides Are Known
"""

from math import sqrt

def area(a,b,c):
    """TÄä laskee mainissa määritetyn pinta-alan ja palauttaa sen"""
    s = float((a+b+c)/2)
    
    tulos = sqrt(s*(s-a)*(s-b)*(s-c))
  
    return tulos


def main():
    eka = float(input("Enter the length of the first side: "))
    toka = float(input("Enter the length of the second side: "))
    kolmas= float(input("Enter the length of the third side: "))
    pinta=area(eka,toka,kolmas)

    print(f"The triangle's area is {pinta:.1f}")


if __name__ == "__main__":
    main()
