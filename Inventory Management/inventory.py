from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
 


#=============Shoe list===========
shoes_list = [
    Shoe("USA", "SKU001", "Nike Air Max", 1200, 100),
    Shoe("Italy", "SKU002", "Prada Loafers", 3000, 50),
    Shoe("Japan", "SKU003", "Adidas Ultraboost", 1500, 80),
]
#==========Functions outside the class==============
def read_shoes_data():
    try:
        # Open the "inventory.txt" file in read mode and read all lines except the first one
        with open("inventory.txt", "r") as file:
            lines = file.readlines()[1:]
        
        # Loop through each line in the file
        for line in lines:
            # Split the line by commas to extract the shoe data
            data = line.strip().split(",")
            # Extract the shoe details from the data
            country = data[0]
            code = data[1]
            product = data[2]
            cost = float(data[3])
            quantity = int(data[4])
            # Create a Shoe object using the extracted data
            shoe = Shoe(country, code, product, cost, quantity)
            # Append the Shoe object to the shoes_list
            shoes_list.append(shoe)
            # Print a success message
            print("Data read from file successfully!")
    
    # If the "inventory.txt" file is not found, print an error message
    except FileNotFoundError:
        print("File not found.")

            
def capture_shoes(shoe_data):
    # Extract shoe details from the dictionary
    country = shoe_data["country"]
    code = shoe_data["code"]
    product = shoe_data["product"]
    cost = float(shoe_data["cost"])
    quantity = int(shoe_data["quantity"])
    
    # Create a Shoe object
    shoe = Shoe(country, code, product, cost, quantity)
    
    # Append the Shoe object to the shoes_list
    shoes_list.append(shoe)
    
    # Print a message indicating success
    print("Shoe added successfully.")
    

def view_all():
    if len(shoes_list) == 0:
        return "No shoes to display."
    else:
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        data = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoes_list]
        return tabulate(data, headers=headers)
    

def re_stock():
    # Find the shoe with the lowest quantity in the inventory
    lowest_qty_shoe = min(shoes_list, key=lambda x: x.quantity)
    print(f"The shoe with code {lowest_qty_shoe.code} needs to be restocked.")
    
    # Prompt the user to add more shoes to the inventory
    add_qty = input("Do you want to add more shoes to the inventory? (y/n): ")
    if add_qty.lower() == "y":
        # Ask the user to enter the quantity of shoes to add
        new_qty = int(input("Enter the quantity to add: "))
        # Add the new quantity to the shoe's quantity
        lowest_qty_shoe.quantity += new_qty
        
        # Update the inventory file with the new shoe quantity
        with open("inventory.txt", "r+") as file:
            # Read all the lines from the file
            lines = file.readlines()
            # Move the file pointer to the beginning of the file
            file.seek(0)
            # Loop through each line in the file
            for line in lines:
                # Split the line by commas to extract the shoe data
                data = line.strip().split(",")
                # Check if the shoe code in the line matches the code of the shoe being restocked
                if data[1] == lowest_qty_shoe.code:
                    # Update the quantity of the shoe in the line
                    data[-1] = str(lowest_qty_shoe.quantity)
                    # Join the shoe data back into a string and add a newline character
                    line = ",".join(data) + "\n"
                # Write the updated line back to the file
                file.write(line)
            # Truncate any remaining lines in the file
            file.truncate()
        # Print a success message
        print("Inventory updated successfully!")



def search_shoe():
    # Prompt the user to enter the shoe code to search for
    code = input("Enter shoe code: ")
    
    # Loop through each shoe in the shoes_list
    for shoe in shoes_list:
        # Check if the shoe code matches the search code
        if shoe.code == code:
            # If there is a match, print the shoe details and return
            print(shoe)
            return
    
    # If no match is found, print a "not found" message
    print("Shoe not found.")

def value_per_item():
    # Check if the shoes_list is empty
    if len(shoes_list) == 0:
        print("No shoes to calculate value for.")
    else:
        index = int(input ("Enter the index of the shoe u want the value for: "))
        print(shoes_list[index])
        # Loop through the shoes_list and calculate the value for each shoe
        value = shoes_list[index].cost * shoes_list[index].quantity
        print(f"Code:{shoes_list[index].code}\tName:{shoes_list[index].product}\tValue:{value}")


def highest_qty(shoes_list):
    # Initialize a variable to hold the maximum quantity
    max_qty = 0
    
    # Loop through each shoe in the shoes_list
    for shoe in shoes_list:
        # Check if the shoe's quantity is greater than the current maximum
        if shoe.quantity > max_qty:
            # If so, update the maximum quantity and the shoe with the highest quantity
            max_qty = shoe.quantity
            max_shoe = shoe
    
    # Print the shoe with the highest quantity
    print(f"The shoe with the highest quantity ({max_qty}) is {max_shoe.product} and is for sale!")