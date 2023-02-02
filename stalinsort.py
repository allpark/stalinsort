def stalinSort(line):
    # inspect the first comrade
    comrade = line[0]
    # go through the line
    for i in range(1, len(line)):
        comrade = max(comrade, line[i])
        # decide if next in line is out of order
        if (comrade>line[i]):
            # eliminate 
            line[i] = None
