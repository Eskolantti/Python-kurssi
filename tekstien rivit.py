"""
AnttiEskola 151210040
COMP.CS.100 Programming 1
rivinro tiedostoo
"""

def main():
    filenames = input("Enter the name of the file: ")
    try:
        with open(filenames, "r") as f:
            for i, line in enumerate(f):
                print(f"{i+1} {line.rstrip()}")
        f.close()
    except:
        print("There was an error in reading the file.")



if __name__ == "__main__":
    
    main()