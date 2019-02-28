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
        dicc['num'] = len(tags)
        photos[i] = dicc

    file.close()

    return photos


def writeOutput(result, problemTitle):
    file = open(problemTitle+'_result.out', 'w')

    file.write(str(len(result))+'\n')
    # TODO write result

    file.close()


# +
#data = readData('b_lovely_landscapes.txt')
#print(data)
# -

def join_verticals(all_photos):
    verticals_o = [x for x in all_photos if x['orientation']=='V']
    verticals_r = []
    while(len(verticals_o)!=0):
        v = verticals_o.pop()
        for t in verticals_o[::-1]:
            if len(np.intersect1d(v['tags'],t['tags']))==0:
                #print(len(verticals_o))
                verticals_o.remove(t)
                verticals_r.append({
                    'id':[t['id'], v['id']],
                    'tags':np.union1d(v['tags'],t['tags']),
                    'orientation':'V'             
                })
    return [x for x in all_photos if x['orientation']!='V']+verticals_r
