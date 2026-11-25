import random
import numpy
shopping_list = ["Fruit", "Milk", "Bread", "Eggs", "Cheese"]
random_item_list = ["Meat", "Fish", "Pork", "Chicken", "Vegetables"]

def get_temperatures(): #3.
    temperatures = [12, 15, 18, 14, 11]
    return temperatures
def get_cities(): #3.
    return ["Göteborg", "Malmö", "Stockholm", "Majorna"]
def get_games(): #3)
    return ["Deadlock", "Portal", "Left For Dead", "Titanfall", "Half Life"]
def get_shopping_list(): #4)
    shopping_list = ["Fruit", "Milk", "Bread", "Eggs", "Cheese"]
    random_item_list = ["Meat", "Fish", "Pork", "Chicken", "Vegetables"]
    shopping_list.insert(random.randrange(len(shopping_list) + 1), random.choice(random_item_list))
    shopping_list.append(random.choice(random_item_list))
    return shopping_list
def remove_shopping_list(): #5)
    shopping_list.insert(random.randrange(len(shopping_list) + 1), random.choice(random_item_list))
    shopping_list.remove(random.choice(shopping_list))
    shopping_list.append(random.choice(random_item_list))
    shopping_list.pop(random.randrange(len(shopping_list)))
    return shopping_list
def get_scores(): #6)
    scores = [1, 71, 36, 83, 26, 53, 97, 14, 53, 40]
    return scores