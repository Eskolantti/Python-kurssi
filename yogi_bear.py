"""
Antti Eskola: 151210040
COMP.CS.100 Programming 1
Code template for the hottest hit song Yogi Bear
"""

def repeat_name(name: str, repeats: int) -> None:
    """Toistaa nimiä mitä syötetäää"""
    
    for i in range(repeats):
        print(f"{name}, {name} Bear")
        print(f"{name}, {name} Bear")

def verse(line: str, name: str) -> None:
    """Toistaaa verseä riveittöi"""
    print(line)
    repeat_name(name, 1)
    print(line)
    repeat_name(name, 3)

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")

if __name__ == "__main__":
    main()
