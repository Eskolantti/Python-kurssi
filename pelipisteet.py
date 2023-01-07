
"""
AnttiEskola 151210040
COMP.CS.100 Programming 1
pelin pisteet
"""


def main():
    scores = {}  # luo tyhjän tietorakenteen

    # pyytää käyttäjältä tiedoston nimeä
    filenames = input("Enter the name of the score file: ")
    with open(filenames, "r") as f:
        # käy läpi jokainen rivi tiedostossa
        for line in f:
            # pilkko rivi osiin nimen ja pistemäärän kohdalta
            name, score = line.strip().split()
            score = int(score)  # muuta pistemäärän tekstistä kokonaisluvuksi

            # lisää pistemäärä pelaajan nimelle tietorakenteessa
            if name in scores:
                scores[name] += score
            else:
                scores[name] = score

    # tulosta pelaajien pisteet aakkostettuna nimen mukaan
    print("Contestant score:")
    for name in sorted(scores):
        print(f"{name} {scores[name]}")

if __name__ == "__main__":
    main()
