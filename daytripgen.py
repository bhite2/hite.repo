destinations = ['Miami,FL', 'New York City, NY', 'Los Angeles, CA', 'Atlanta, GA', 'Dallas,TX']

restaurants = ["Ruth's Chris Steakhouse", 'Ocean Prime', "Shula's", 'Seasons 52', 'Flemings']

entertainments = ['Broadway Show', 'Museum', 'Theme Park', 'Sporting Event', 'Night Club']

transportations = ['Car', 'Bus', 'Train', 'Plane', 'Boat']

import random

destination = random.choice(destinations)

restaurant = random.choice(restaurants)

entertainment = random.choice(entertainments)

transportation = random.choice(transportations)

def des_gen ():
    destination = random.choice(destinations)
    print(destination)

def res_gen ():
    restaurant = random.choice(restaurants)
    print(restaurant)

def ent_gen ():
    entertainment = random.choice(entertainments)
    print(entertainment)

def tran_gen ():
    transportation = random.choice(transportations)
    print(transportation)

def user_satisfaction ():
    print("Are you satisfied with your selection? Y or N ")
    result = input("")
    if result == "Yes":
        print("Congratulations!!! Your trip has been scheduled.")
        print(f"Destination: {destination}")
        print(f"Restaurant: {restaurant}")
        print(f"Entertainment: {entertainment}")
        print(f"Transportation: {transportation}")
    else:
        run ()

def run ():
    des_gen ()
    res_gen ()
    ent_gen ()
    tran_gen ()
    user_satisfaction ()

run ()