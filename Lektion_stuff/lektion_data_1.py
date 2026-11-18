import random

def get_Temperature(temp_fromuser):
    list_Of_Temperature = [12, 34, 2, -24, 4]
    list_Of_Temperature.append(temp_fromuser)
    list_Of_Temperature.append(random.uniform(0.0, 10.0))
    return list_Of_Temperature

def meanValue():
    mylist = get_Temperature(0)
    sum = 0
    for number in mylist:
        sum = sum + number
    mean = sum / len(mylist)
    return mean
