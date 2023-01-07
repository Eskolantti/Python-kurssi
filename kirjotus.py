"""
AnttiEskola 151210040
COMP.CS.100 Programming 1
kirjoitus
"""

def main():
    # pyytää käyttäjältä tiedoston nimeä
    filename = input("Enter the name of the file: ")
    

    # lukee käyttäjältä rivit
    lines = []
    print("Enter rows of text. Quit by entering an empty row.")
    while True:
        line = input()
        if line:  # jos rivi ei ole tyhjä
            lines.append(line)
        else:  # jos rivi on tyhjä
            break

    # yritetään kirjoittaa rivit tiedostoon
    try:
        with open(filename, "w") as f:
            for i, line in enumerate(lines):
                f.write(f"{i+1} {line}\n")
        print(f"File {filename} has been written.")
    except:
        print(f"Writing the file {filename} was not successful.")

if __name__ == "__main__":
    main()
