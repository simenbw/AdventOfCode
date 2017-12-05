oldValues = [1, 2, 4, 5, 10, 11, 23, 25]
newValues = []

count = 0
while count < 4:
    for i in range(len(oldValues) + 8):
        newValues.append(0)

        # Start of new round
        if i == 0:
            newValues[i] = oldValues[len(oldValues) - 1] + oldValues[0]  # Start
            continue

        # First after start
        if i == 1:
            newValues[i] = newValues[i-1] + oldValues[len(oldValues) - 1] + oldValues[0] + oldValues[1]
            continue

        # Between start and first corner
        if i > 1 and i < (count * 2) + 2:
            newValues[i] = newValues[i-1] + oldValues[i-2] + oldValues[i-1] + oldValues[i]
            continue

        # Before first corner
        if i == (count * 2) + 2:
            newValues[i] = newValues[i-1] + oldValues[i-2] + oldValues[i-1]
            continue

        # First Corner
        if i == (count * 2) + 3:
            newValues[i] = newValues[i-1] + oldValues[i-2]
            continue

        # After first corner
        if i == (count * 2) + 4:
            newValues[i] = newValues[i-1] + newValues[i-2] + oldValues[i-3] + oldValues[i-2]
            continue

        # Between first and second corner
        if i < ((count + 1) * 4) + 2 and i > count + 4:
            newValues[i] = newValues[i-1] + oldValues[i-4] + oldValues[i-3] + oldValues[i-2]
            continue

        # Before second corner
        if i == ((count + 1) * 4) + 2:
            newValues[i] = newValues[i-1] + oldValues[i-4] + oldValues[i-3]
            continue

        # Second corner
        if i == ((count + 1) * 4) + 3:
            newValues[i] = newValues[i-1] + oldValues[i-4]
            continue

        # After second corner
        if i == ((count + 1) * 4) + 4:
            newValues[i] = newValues[i-1] + newValues[i-2] + oldValues[i-4] + oldValues[i-5]
            continue

        # Between second and third corner
        if i > ((count + 1) * 4) + 4 and i < ((count + 1) * 6) + 4:
            newValues[i] = newValues[i - 1] + oldValues[i - 6] + oldValues[i - 5] + oldValues[i - 4]
            continue

        # Before third corner
        if i == ((count+1) * 6) + 4:
            newValues[i] = newValues[i-1] + oldValues[i-6] + oldValues[i-5]
            continue

        # Third corner
        if i == ((count + 1) * 6) + 5:
            newValues[i] = newValues[i - 1] + oldValues[i - 6]
            continue

        # After third corner
        if i == ((count + 1) * 6) + 6:
            newValues[i] = newValues[i-1] + newValues[i-2] + oldValues[i-7] + oldValues[i-6]
            continue

        # Between third and fourth corner
        if i > ((count + 1) * 6) + 6 and i < len(oldValues) + 6 :
            newValues[i] = newValues[i - 1] + oldValues[i - 8] + oldValues[i - 7] + oldValues[i - 6]
            continue

        # Before fourth corner
        if i == len(oldValues) + 6:
            newValues[i] = newValues[i-1] + oldValues[i-8] + oldValues[i-7] + newValues[0]
            continue

        # fourth corner
        if i == len(oldValues) + 7:
            newValues[i] = newValues[i - 1] + newValues[0] + oldValues[len(oldValues) - 1]
            continue

    print(newValues)
    oldValues = newValues
    newValues = []
    count = count + 1
