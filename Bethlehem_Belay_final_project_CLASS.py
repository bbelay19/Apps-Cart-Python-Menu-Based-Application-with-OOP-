#-------------------------------------------------------------------------------
# Final Project
# Student Name: Bethlehem Belay
# Submission Date: 12/05/2024
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# Your source code below
#-------------------------------------------------------------------------------
import csv

class Cart(list):
    """Cart class inherits from list to store app items purchased by the user."""
    
    def subtotal(self):
        '''Returns the subtotal from a Cart list object'''
        return sum(item.get_price() for item in self)
    
class App:
    '''App class defines an app item available in store. 
       App objects are saved in cat_dict per category, 
       rating_dict per rating, and price_dict per price range.'''
    
    cat_dict = {}  # Apps categorized by category
    rating_dict = {1: [], 2: [], 3: [], 4: [], 5: []}  # Ratings as keys
    price_dict = {}  # Apps categorized by price ranges

    def __init__(self, ID, name, developer, description, price, rating, review_count, category):
        '''Initialization method'''
        self.__id = ID
        self.__name = name
        self.__developer = developer
        self.__description = description
        self.__price = float(price)
        self.__rating = float(rating)
        self.__review_count = review_count
        self.__category = category
        
        # Add to category dictionary
        if self.__category in App.cat_dict:
            App.cat_dict[self.__category].append(self)
        else:
            App.cat_dict[self.__category] = [self]
        
        # Add to rating dictionary
        App.rating_dict[int(self.__rating)].append(self)

        # Add to price dictionary (grouped by dollar ranges)
        price_key = f"${int(self.__price)}.00"
        if price_key in App.price_dict:
            App.price_dict[price_key].append(self)
        else:
            App.price_dict[price_key] = [self]

    # Getter methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_developer(self):
        return self.__developer

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_rating(self):
        return self.__rating

    def get_category(self):
        return self.__category


# Process the file and populate dictionaries
with open('Top50ShopifyApps.csv') as fin:
    apps = csv.reader(fin, delimiter=',')
    next(apps)  # Skip the header row
    for row in apps:
        ID, name, developer, description, price, rating, review_count, category = row
        # Handle 'Free' in the price column
        price = 0.0 if price.strip().lower() == 'free' else float(price)
        App(ID, name, developer, description, price, float(rating), int(review_count), category)


'''Testing code to check object creation
Uncomment to test and then comment out when done'''
'''print("Testing Category Dictionary:")
for k, v in App.cat_dict.items():  # v is a list of all objects
    print(k, [(obj.get_name(), obj.get_rating()) for obj in v])
print('++++++++++')

print("Testing Rating Dictionary:")
for k, v in App.rating_dict.items():  # v is a list of all objects
    print(k, [obj.get_rating() for obj in v])
print('++++++++++')

print("Testing Price Dictionary:")
for k, v in App.price_dict.items():  # v is a list of all objects
    print(k, [obj.get_price() for obj in v])
print('++++++++++')'''

