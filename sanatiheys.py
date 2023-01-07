"""
Student Id: 15210040
Name: Antti Eskola
COMP.CS.100 Programming 1
tourist dictionary.
"""


def word_frequency(text):
    """
    Laskee tekstin sanojen esiintymistiheydet ja palauttaa ne dictinä, jossa avaimena on sana ja arvona esiintymiskertojen lukumäärä.
    """
    
    frequencies = {}
    
    words = text.split()
    
    for word in words:
        word = word.lower()
        
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
        
    sorted(frequencies)
    
    return frequencies

def main():
    text = ""
    
    
    # Kysytään käyttäjältä syötettä rivi kerrallaan
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        
        line = input()
        
        # Jos rivi on tyhjä, lopetetaan syötteen otto
        if not line:
            break
        
        # Muussa tapauksessa lisätään rivi tekstiin ja lisätään välilyönti ennen seuraavaa riviä
        text += " " + line
        
    frequencies = word_frequency(text)
    
    
    for word, count in frequencies.items():
        print(f"{word} : {count} times")
  
if __name__ == "__main__":
    main()

