"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Liukulukujen vertailu
"""
from pickle import TRUE
from tkinter import FALSE


def compare_floats(eka,toka,Epsi):
    if abs(eka-toka) < Epsi:
        return True
    else:
        return False
def main():
    epsilon=compare_floats("EPSILON:")
    compare_floats()



    


if __name__ == "__main__":
    main()
