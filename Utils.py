import pandas as pd
import numpy as np

def readData(filePath):
    file = open(filePath, 'r')
    line = file.readline().split(" ")
    rows = int(line[0])
    
    photos = np.empty((rows), dtype=dict)
    for i in range(rows):
        line = file.readline()
        values = line.split()
        dicc = { 'id' : [i], 'orientation' : values[0] }
        tags = np.array([values[i] for i in range(2, 2+int(values[1]))], dtype=str)
        dicc['tags'] = tags
        photos[i] = dicc

    file.close()

    return photos


def writeOutput(result, problemTitle):
    file = open(problemTitle+'_result.out', 'w')

    file.write(str(len(result))+'\n')
    # TODO write result

    file.close()


data = readData('a_example.txt')
print(data)


