"""
Student Id: 15210040
Name: Antti Eskola
COMP.CS.100 Programming 1
tourist dictionary.
"""

def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    print("Dictionary contents:")
    print(", ".join(sorted(english_spanish)))
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[english_word] = spanish_word
            print("Dictionary contents:")
            print(", ".join(sorted(english_spanish)))
        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "P":
            
            print("\nEnglish-Spanish")
            for word in sorted(english_spanish.keys()):
                print(f"{word} {english_spanish[word]}")

            print("\nSpanish-English")
            for word in sorted(english_spanish.values()):
                print(f"{word} {[key for key, value in english_spanish.items() if value == word][0]}")
            print()

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            words = text.split()
            translated_words = []
            for word in words:
                if word in english_spanish:
                    translated_words.append(english_spanish[word])
                else:
                    translated_words.append(word)
            print("The text, translated by the dictionary:")
            print(' '.join(translated_words))

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
