arrival = [0, 0, 1, 4]
street = [0, 1, 1, 0]
time_taken = [0]*len(arrival)

index = 0
time = 0
previous_pass = 1

while index < len(arrival):
    if street[index] == 1 and previous_pass == 1:
        time_taken[index] = time + arrival[index]
        time += 1


print(time_taken)
