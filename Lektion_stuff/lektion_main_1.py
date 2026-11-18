import lektion_data_1

redo_Value_Times = 0
redo_Value = "Y"

while redo_Value == "Y":
    redo_Value = input("More?") == "Y"
    redo_Value_Times = redo_Value_Times + 1
    for number in range(redo_Value_Times):
        print(lektion_data_1.meanValue())
