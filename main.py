import numpy
import random
import data

temperatures = data.get_temperatures()
cities = data.get_cities()
games = data.get_games()
shopping = data.get_shopping_list()
Shopping = data.remove_shopping_list()
scores = data.get_scores()
print("Look at the code to see the different paths")
Path = input("Path ")

if Path == "1": #1)
    print(["Minecraft", "Peak", "Rounds", "Risk of Rain Returns", "Risk of Rain 2"])
    print(len(["Minecraft", "Peak", "Rounds", "Risk of Rain Returns", "Risk of Rain 2"]))
elif Path == "2": #2.
    animals = ["hund", "katt", "häst", "kanin"]
    print(animals[0])
    print(animals[2])
    print(animals[-1])
elif Path == "3": #2.
    colors = ["röd", "blå", "grön"]
    colors[1] = "gul"
    print(colors)
elif Path == "4": #2)   
    Games = ["Minecraft", "Peak", "Rounds", "Risk of Rain Returns", "Risk of Rain 2"]
    print(Games[0])
    print(Games[2])
    print(Games[4])
    Games[1] = "TABS"
    print(Games)
elif Path == "5": #3.
    print(temperatures)
elif Path == "6": #3.
    print(cities)
elif Path == "7": #3)
    print(games)
    print(len(games))
elif Path == "8": #4.
    score = [1, 5, 3, 19, 13, 23, 26, 7]
    score.append(6)
    score.insert(4,10)
    print(score)
elif Path == "9": #4)
    print(shopping)
elif Path == "10": #5.
    names = ["Anna", "Erik", "Sara", "Johan"]
    names.pop(1)
    print(names)
elif Path == "11": #5.
    names = ["Anna", "Erik", "Sara", "Johan"]
    removed_name = names.pop(1)
    print("Borttaget namn:", removed_name)
    print("Kvar i listan:", names)
elif Path == "12": #5)
    print(Shopping)
elif Path == "13": #6.
    fruits = ["äpple", "banan", "päron", "banan", "apelsin", "vindruvor", "äpple"]
    for fruit in fruits:
        print(fruit)
elif Path == "14": #6.
    prices = [10, 25, 15, 30]
    for price in prices:
        print(price*2)
elif Path == "15": #6.
    prices = [5, 10, 25, 15, 30, 45, 20]
    for price in prices:
        if price < 20:
            print(price+10)
elif Path == "16": #6)
    for score in scores:
        if score > 50:
            print(score*2)
        print("original scores")
    for score in scores:
        if score > 50:
            print(score)
    print("other way")
    for score in scores:
        if score*2 > 50:
            print(score*2)
    print("original number the other way")
    for score in scores:
        if score*2 > 50:
            print(score)
elif Path == "17":
    None
elif Path == "18":
    None
elif Path == "19":
    None
elif Path == "20":
    None
elif Path == "21":
    None
elif Path == "22":
    None
elif Path == "23":
    None
elif Path == "24":
    None
elif Path == "25":
    None