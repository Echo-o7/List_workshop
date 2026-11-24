import numpy
import random
import data

temperatures = data.get_temperatures()
cities = data.get_cities()
games = data.get_games()
shopping = data.get_shopping_list()
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

elif Path == "10":
    None

elif Path == "11":
    None

elif Path == "12":
    None

elif Path == "13":
    None

elif Path == "14":
    None

elif Path == "15":
    None
