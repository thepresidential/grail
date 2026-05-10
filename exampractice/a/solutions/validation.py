numbers = []
count = 0

num = 0
while num != -1:
    num = int(input("Enter a number between 1 and 100 (or -1 to stop): ")) # CASTING!!!

    if num != -1:
        if 1 <= num <= 100:
            numbers.append(num)
            count += 1
        else:
            print("Invalid number")

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

if count > 0:
    average = total / count

    print("Average: ", average)
else:
    print("No valid numbers entered")