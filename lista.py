"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Lista
"""


def input_to_list(x):
    """Funktio syöttäää listaan annetut arvot"""
    numerot=[]
    print(f"Enter {x} numbers: ")
    for i in range(x):
        arvo=input()
        numerot.append(int(arvo))



    return numerot
    
def main():
    len=input("How many numbers do you want to process: ")
    len=int(len)
    amount=0
    j=0
    etsi= input_to_list(len)
    hakuehto= input("Enter the number to be searched: ")
    hakuehto= int(hakuehto)
    for määrä in etsi:
        
        if määrä == hakuehto:
            amount= amount + 1 
        
    if amount > 0:
        print(f"{hakuehto} shows up {amount} times among the numbers you have entered.")
    else:
        print(f"{hakuehto} is not among the numbers you have entered.")


   

    return
if __name__ == "__main__":
    main()