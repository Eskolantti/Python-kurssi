"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 15210040
Name: Antti Eskola
pricelist assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    while True:
        input_string = input("Enter product name: ")
        input_list = list(input_string)
        filtered_list = [x for x in input_list if x != ' ']
        output_string = ''.join(filtered_list)
        if output_string != "":
            if output_string in PRICES:
                print(f"The price of {output_string} is {PRICES[output_string]:.2f} e")
                
            else:
                print(f"Error: {output_string} is unknown.")
                
        
        else:
            print("Bye!")
            break
        
    


        
    

   

if __name__ == "__main__":
    main()
