"""
Antti Eskola 151210040
COMP.CS.100 Programming 1
Lottery
"""




def testaus(m):
    """ Tarkistaaa onko annettu syöte suurempi kuin 0"""
    while True:
        try:
            syöte = int(input(m))
            if syöte > 0 :
                return syöte
        except:
            ValueError


def testinostoista(eka,toka):
    """Testaa onks annettu syöte suurempi kuin 0 ja toteaa, että palloja ei saaa nostaa enempää ku niitä o"""
    while True:
        try:
            
            syöte = int(input(toka))
            if syöte > 0 and eka > syöte:
                
                return syöte
        except:
            ValueError



def factorical(x):
    """ Määrittää funktion kertoman syötetyllä arvolla"""
    factoric = 1 
    for i in range(1,x+1):
        
        factoric = int(factoric * i)
    return factoric

    
def main():
    n = testaus("Enter the total number of lottery balls: ")
    p = testinostoista(n,"Enter the number of the drawn balls: ")
    
   
    kertoman=factorical(int(n))
    kertomap=factorical(int(p))
    
    kertomanp= factorical((int(n)-int(p)))
    
    print(f"1/{int(kertoman/(kertomanp*kertomap))}")




    


if __name__ == "__main__":
    main()
