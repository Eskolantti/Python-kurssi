"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Print a box with input error checking
"""
def print_box(w,h,m):
    "Luo main ruudun annetuilla arvoilla, jossa ensimmäinenm kirjain on sama muutujan kanssa"
    for i in range(h):
        print(w*m)
def read_input(x):
    """ Tarkistaaa onko annettu syöte suurempi kuin 0"""
    while True:
        try:
            syöte = int(input(x))
            if syöte > 0:
                return syöte
        except:
            ValueError


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)


if __name__ == "__main__":
    main()
