
days=["Sunday","Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday"]


day_index = int(input("Enter the day index of the week: "))

# dayinteger = int(day_index)


for i in range(len(days)): # for i in [0,1,2,3,.....,6]:

    if day_index == i : # if i == day_index:
        print(days[i])
        break
