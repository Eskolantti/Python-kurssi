"""
Antti Eskola 151210040
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""
def calculate_dose(p,t,k):
  """Määrittää syötettävän lääkeannoksen potilaalle ja huomioi edelliset annokset 24 tunnin aikana ja viimisen 6h annosmäärän"""
  täysi =p*15 + k
  if t < 6 :
    return 0
  elif täysi > 4000:
    return 4000-k
  return p*15

  
  

def main():
    paino=input("Patient's weight (kg): ")
    paino = int(paino)
    tunnit=input("How much time has passed from the previous dose (full hours): ")
    tunnit = int(tunnit)
    kokoannos=input("The total dose for the last 24 hours (mg): ")
    kokoannos = int(kokoannos)
    annos=calculate_dose(paino,tunnit,kokoannos)
    print(f"The amount of Parasetamol to give to the patient: {annos}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
  