def stalinSort(line):
    # inspect the first comrade
    comrade = line[0]
    # go through the line
    for i in range(1, len(line)):
        comrade = max(comrade, line[i])
        # decide which consecutive is out of order
        if (comrade>line[i]):
            # eliminate comrade which is out of order
            line[i] = None
