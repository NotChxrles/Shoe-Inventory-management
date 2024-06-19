from tkinter import *
from tkinter import messagebox
from inventory import read_shoes_data, capture_shoes, view_all, re_stock, search_shoe, value_per_item, highest_qty

class ShoeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shoevest")
        
        self.labels = ["Country", "Code", "Product", "Cost", "Quantity"]
        self.entries = {}
        
        for i, label in enumerate(self.labels):
            Label(root, text=label).grid(row=i, column=0, sticky=E, padx=10, pady=5)
            entry = Entry(root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label.lower()] = entry
            
        # Configure grid weights for better layout control
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        # Buttons to create Shoe instance and perform other operations
        self.create_button = Button(root, text="Add Shoe", command=self.add_shoe)
        self.create_button.grid(row=len(self.labels), column=0, columnspan=2, pady=5)

        self.view_button = Button(root, text="View All Shoes", command=self.view_all_shoes)
        self.view_button.grid(row=len(self.labels) + 1, column=0, columnspan=2, pady=5)

        self.search_button = Button(root, text="Search Shoe", command=self.search_shoe)
        self.search_button.grid(row=len(self.labels) + 2, column=0, columnspan=2, pady=5)

        self.restock_button = Button(root, text="Restock Shoe", command=self.re_stock_shoe)
        self.restock_button.grid(row=len(self.labels) + 3, column=0, columnspan=2, pady=5)

        self.value_button = Button(root, text="Value Per Item", command=self.value_per_item)
        self.value_button.grid(row=len(self.labels) + 4, column=0, columnspan=2, pady=5)

        self.highest_qty_button = Button(root, text="Highest Quantity", command=self.highest_qty)
        self.highest_qty_button.grid(row=len(self.labels) + 5, column=0, columnspan=2, pady=5)

        self.read_button = Button(root, text="Read Shoes Data", command=self.read_shoes_data)
        self.read_button.grid(row=len(self.labels) + 6, column=0, columnspan=2, pady=5)

    def add_shoe(self):
        shoe_data = {label: self.entries[label].get() for label in self.entries}
        print("Shoe data to be added:", shoe_data)  # Debugging print statement
        if all(shoe_data.values()):  # Ensure all fields are filled
            try:
                capture_shoes(shoe_data)
                messagebox.showinfo("Success", "Shoe added successfully!")
                self.clear_fields() # Clear all fields after successful addition
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add shoe: {e}")
        else:
            messagebox.showwarning("Warning", "All fields must be filled out.")
            
    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, END)
            
    def search_shoe(self):
        code = self.entries['code'].get()
        if code:
            try:
                result = search_shoe(code)
                messagebox.showinfo("Search Result", f"Result: {result}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to search shoe: {e}")
        else:
            messagebox.showwarning("Warning", "Code field must be filled out.")

    def re_stock_shoe(self):
        code = self.entries['code'].get()
        if code:
            try:
                re_stock(code)
                messagebox.showinfo("Success", "Shoe restocked successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to restock shoe: {e}")
        else:
            messagebox.showwarning("Warning", "Code field must be filled out.")

    def view_all_shoes(self):
        try:
            shoes_data = view_all()
            messagebox.showinfo("All Shoes", f"All Shoes:\n{shoes_data}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to view shoes: {e}")

    def value_per_item(self):
        try:
            values = value_per_item()
            messagebox.showinfo("Value Per Item", f"Values: {values}")
        except Exception as e:
            messagebox.showerror("Error", "Failed to calculate value per item")

    def highest_qty(self):
        try:
            result = highest_qty()
            messagebox.showinfo("Highest Quantity", f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", "Failed to find highest quantity shoe")

    def read_shoes_data(self):
        try:
            read_shoes_data()
            messagebox.showinfo("Success", "Shoe data read successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read shoe data: {e}")

if __name__ == "__main__":
    root = Tk()
    app = ShoeApp(root)
    root.mainloop()
