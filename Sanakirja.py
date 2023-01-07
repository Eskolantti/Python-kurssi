"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Puhelinluettelo
"""
def read_file(filename: str) -> dict:
    """Lukee tiedoston ja palauttaa infoluetttelon"""
    contacts = {}
    with open(filename) as f:
        # Luetaan otsikkorivi ja jaetaan se puolipisteiden kohdalta listaan
        headers = f.readline().strip().split(";")
        for line in f:
            # Jaetaan rivi puolipisteiden kohdalta listaan ja muutetaan listan alkiot str -> int
            values = line.strip().split(";")
            # Luodaan sanakirja, jossa avaimina ovat otsikkorivin literaalit ja arvoina rivin arvot
            contact = {header: value for header, value in zip(headers, values)}
            # Lisätään sanakirja contacts-sanakirjaan key:n perusteella
            contacts[contact["key"]] = contact
    return contacts



def main():
    read_file("contacts.csv")


if __name__ == "__main__":
    main()
