names = []
times = []

for i in range(5): # 1 -> 5 simplifies to range(5)
    name = input("Enter runner name: ")
    names.append(name)

    time = float(input("Enter time: ")) # CASTING!!!
    times.append(time)

fastestTime = times[0]
fastestName = names[0]

for i in range(1, len(names)): # pay attention to the code and think about how it would have to run
    if times[i] > fastestTime:
        fastestTime = times[i]
        fastestName = names[i]

print("Winner: ", fastestName)
print("Time: ", fastestTime)