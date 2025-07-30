from tkinter import *
from tkinter import messagebox
from functools import partial
import random, string
from Bethlehem_Belay_final_project_CLASS import App, Cart

class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root) #Frame class initialization
        self.init_container() #initialize all widget containers
        self.cart = Cart() #initialize Cart list object 
        self.welcome() #start the application
        self.data = StringVar(self, 'Subtotal: 0.0') #Associated with subtotal label


    def init_container(self):
        '''Initialize widget containers'''
        self.states = []

    def clear_frame(self):
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

    def welcome(self):
        '''Welcome window'''
        self.clear_frame()
        Label(self, text='**** Welcome to AppsCart! ****', background="gray70", font=('Arial', 16)).pack(pady=10)

        Button(self, text="Select by Category", command=self.shop_by_apps_category).pack(pady=5)
        Button(self, text="Select by Rating", command=self.shop_by_apps_ratings).pack(pady=5)
        Button(self, text="Select by Price", command=self.shop_by_apps_price).pack(pady=5)
        Button(self, text="Exit Application", command=self.exit_application).pack(pady=10)

    def shop_by_apps_category(self):
        '''Widget to display different categories of apps'''
        self.clear_frame()
        categories = list(App.cat_dict.keys())

        Label(self, text="Choose Apps Category:", font=('Arial', 14)).pack(pady=10)
        for category in categories:
            Button(self, text=category, command=partial(self.display_apps, App.cat_dict[category])).pack(pady=5)
        Button(self, text="Go Back", command=self.welcome).pack(pady=10)

    def shop_by_apps_ratings(self):
        '''Widget to display apps by rating'''
        self.clear_frame()
        ratings = sorted(App.rating_dict.keys())

        Label(self, text="Choose Apps by Rating:", font=('Arial', 14)).pack(pady=10)
        for rating in ratings:
            Button(self, text=f"Rating {rating} and above", command=partial(self.display_apps, App.rating_dict[rating])).pack(pady=5)
        Button(self, text="Go Back", command=self.welcome).pack(pady=10)

    def shop_by_apps_price(self):
        '''Widget to display apps by price'''
        self.clear_frame()
        prices = sorted(App.price_dict.keys())

        Label(self, text="Choose Apps by Price Range:", font=('Arial', 14)).pack(pady=10)
        for price in prices:
            Button(self, text=f"${price:.2f}", command=partial(self.display_apps, App.price_dict[price])).pack(pady=5)
        Button(self, text="Go Back", command=self.welcome).pack(pady=10)

    def display_apps(self, current_items):
        '''Display selected apps'''
        self.clear_frame()
        self.states = []

        Label(self, text="Available Apps", font=('Arial', 16)).grid(row=0, column=0, columnspan=6, pady=10)
        headers = ["App Name", "Price", "ID", "Rating", "Category"]
        for col, header in enumerate(headers):
            Label(self, text=header, font=('Arial', 12)).grid(row=1, column=col, padx=10)

        for row, item in enumerate(current_items, start=2):
            self.states.append(IntVar())
            Checkbutton(self, text=item.get_name(), variable=self.states[row-2]).grid(row=row, column=0, sticky=W)
            Label(self, text=f"${item.get_price():.2f}").grid(row=row, column=1)
            Label(self, text=item.get_id()).grid(row=row, column=2)
            Label(self, text=f"{item.get_rating()}").grid(row=row, column=3)
            Label(self, text=item.get_category()).grid(row=row, column=4)

        Button(self, text="Add to Cart", command=partial(self.add_to_cart, current_items)).grid(row=row+1, column=1, pady=10)
        Button(self, text="Checkout", command=self.checkout).grid(row=row+1, column=3, pady=10)
        Button(self, text="Back to Menu", command=self.welcome).grid(row=row+2, column=2, pady=10)

        Label(self, textvariable=self.data).grid(row=row+3, column=0, columnspan=6, pady=10)

    def add_to_cart(self, current_items):
        '''Add selected items to the cart'''
        for i, item in enumerate(current_items):
            if self.states[i].get():
                self.cart.append(item)

        self.data.set(f"Subtotal: ${self.cart.subtotal():.2f}")
        messagebox.showinfo("Cart Update", "Selected items have been added to the cart.")

    def get_receipt_number(self):
        '''Generate random receipt number'''
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def checkout(self):
        '''Display checkout window'''
        self.clear_frame()

        Label(self, text="Your e-Receipt", font=('Arial', 16)).pack(pady=10)
        Label(self, text=f"Receipt Number: {self.get_receipt_number()}", font=('Arial', 12)).pack(pady=5)

        headers = "{:<20} {:<10} {:<10} {:<15}".format("Name", "Price", "Rating", "Category")
        Label(self, text=headers, font=('Arial', 12, 'bold')).pack(pady=5)

        for item in self.cart:
            details = "{:<20} ${:<9.2f} {:<10.1f} {:<15}".format(
                item.get_name(), item.get_price(), item.get_rating(), item.get_category())
            Label(self, text=details).pack()

        subtotal = self.cart.subtotal()
        tax = subtotal * 0.043
        total = subtotal + tax

        Label(self, text=f"Subtotal: ${subtotal:.2f}", font=('Arial', 12)).pack(pady=5)
        Label(self, text=f"Tax (4.3%): ${tax:.2f}", font=('Arial', 12)).pack()
        Label(self, text=f"Total: ${total:.2f}", font=('Arial', 14, 'bold')).pack(pady=10)
        Label(self, text="Thank you for shopping with AppsCart!", font=('Arial', 14, 'bold'), fg="green").pack(pady=10)

        Button(self, text="Exit Application", command=self.exit_application).pack(pady=10)


if __name__ == "__main__":
    root = Tk()
    root.title("AppsCart")
    frame = MyFrame(root)
    frame.pack(fill=BOTH, expand=True)
    root.mainloop()

