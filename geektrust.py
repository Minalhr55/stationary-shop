# command line arguments
import sys

class Purchase:
    def __init__(self):
        self.purchases = []
        self.total = 0 
        self.sale_rules = {"min_purchase_amount_for_discount": 1000,
        "min_purchase_amount_for_extra_discount": 3000,
        "extra_discount_percentage": 5,
        "sales_tax_percentage": 10}
        self.products = [
            {
                "name": "TSHIRT",
                "category": "Clothing",
                "price": 1000,
                "discount": 10,
                "max_quantity": 2
            },
            {
                "name": "JACKET",
                "category": "Clothing",
                "price": 2000,
                "discount": 5,
                "max_quantity": 2
            },
            {
                "name": "CAP",
                "category": "Clothing",
                "price": 500,
                "discount": 20,
                "max_quantity": 2
            },
            {
                "name": "NOTEBOOK",
                "category": "Stationery",
                "price": 200,
                "discount": 20,
                "max_quantity": 3
            },
            {
                "name": "PENS",
                "category": "Stationery",
                "price": 300,
                "discount": 10,
                "max_quantity": 3
            },
            {
                "name": "MARKERS",
                "category": "Stationery",
                "price": 500,
                "discount": 5,
                "max_quantity": 3
            },
        ]
        self.total_discount = 0
        self.total_amount_to_pay = 0
    def add_item(self,name, quantity):
        product = next((p for p in self.products if p["name"] == name), None)
        if product is not None and quantity <= product["max_quantity"]:
            cur_total = quantity*product["price"]
            self.total += cur_total
            self.purchases.append([cur_total,product["discount"]])
            print("ITEM_ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED") 

    def print_bill(self):
        if(self.total >= self.sale_rules["min_purchase_amount_for_discount"]):
            disc = 0  
            price = 0 
            for purchase in self.purchases :
                disc += (purchase[1] / 100)*purchase[0]
            price = self.total - disc
            if(self.total >= self.sale_rules["min_purchase_amount_for_extra_discount"]):
                disc += (self.sale_rules["extra_discount_percentage"]/100)*price 
                price -= disc 
            price += (self.sale_rules["sales_tax_percentage"]/100)*price 
            self.total_discount = disc
            self.total_amount_to_pay = price 
            print("TOTAL_DISCOUNT",round(self.total_discount,2))
            print("TOTAL_AMOUNT_TO_PAY",round(self.total_amount_to_pay,2))

        else :
            self.total_discount = 0
            self.total_amount_to_pay = self.total + (self.sale_rules["sales_tax_percentage"]/100)*self.total
            print("TOTAL_DISCOUNT",round(self.total_discount,2))
            print("TOTAL_AMOUNT_TO_PAY",round(self.total_amount_to_pay,2))


def execute(file_path):
    # Open the input file in read mode
    with open(file_path, "r") as input_file:
        # Read all the lines from the file
        lines = input_file.readlines()
    # Iterate over the lines and process each line as an input command
    purchase = Purchase()
    for line in lines:
        # Split the line into parts
        parts = line.split(" ")

        # Extract the command and the arguments
        command = parts[0]

        # Process the command
        if command == "ADD_ITEM":
            # Extract the product name and quantity from the arguments
            name = parts[1]
            quantity = int(parts[2])

            # Call the add_item function to process the ADD_ITEM command
            purchase.add_item(name, quantity)
        elif command == "PRINT_BILL":
            # Call the print_bill function to process the PRINT_BILL command
            purchase.print_bill()
        else:
            # Print an error message if the command is not recognized
            print("ERROR_INVALID_COMMAND")


if __name__ == '__main__':
    execute(sys.argv[1])
