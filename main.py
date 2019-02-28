import Utils
import numpy as np

# +
data = Utils.readData("b_lovely_landscapes.txt")
#data = Utils.readData("a_example.txt")
data = Utils.join_verticals(data)
data = np.array(sorted(data, key=lambda x: -x['num']))
#print(data)

initAlpha = alpha = 0.1
alphaIncrement = 2


# +
def findPhoto(p):
    global data
    for i in range(data.shape[0]):
        if data[i]['id'] == p['id']: return i
    return -1

def getScore(p1, p2):
    t1, t2 = p1['tags'], p2['tags']
    inter = np.intersect1d(t1, t2)
    s1 = np.setdiff1d(t1, inter)
    s2 = np.setdiff1d(t2, inter)
    return min(inter.shape[0], s1.shape[0], s2.shape[0])

def nextPhoto(p):
    global alpha, data
    if data.shape[0] <= 0: return 0
    
    while True:
        absolutePercentile = int(alpha*data.shape[0])
        #print(alpha)
        if absolutePercentile >= 2: break
        else: alpha = min(alphaIncrement*alpha, 1.0)
    alpha = initAlpha
    
    i = findPhoto(p)
    if i == -1: return 1
    
    minV = max(0, i-int(absolutePercentile/2))
    maxV = min(data.shape[0], i+int(absolutePercentile/2)+1)
    
    candidates = list(data[minV : maxV])
    #print(candidates, p, str(minV), str(maxV))
    
    if len(candidates) <= 0: return 2
    
    candidates.sort(key=lambda x: getScore(p,x), reverse = True)
    #print(candidates)
    bestCandidate = candidates[0] if candidates[0] != p else (candidates[1] if len(candidates)>1 else None)
    
    data = np.delete(data, i)
    #print(candidates)
    return bestCandidate#, getScore(p, bestCandidate)


# +
def selectFirstImage():
    global data
    toret = data[0]
    #data = np.delete(data,0)
    return toret

def selectBestPartner(image):
    global data
    toret = data[0]
    data = np.delete(data,0)
    return toret


# +
# %%time
global data
#print(data[:2])

current_slide = selectFirstImage()

#print(data[:2])

slide_show = [current_slide['id']]

#print(slide_show)

#print(data.shape[0])

while(data.shape[0]!=1):
    if data.shape[0] % 1000 == 0: print(data.shape[0])
    #print(data.shape[0])
    next_slide = nextPhoto(current_slide)
    #print(next_slide)
    if next_slide == None: break
    slide_show.append(next_slide['id'])
    current_slide = next_slide

#slide_show.append(data[0]['id'])

#print(slide_show)
# -

import numpy as np
def output(filepath):
    out = open(filepath, 'w')
    out.write(str(len(slide_show))+"\n")
    for indexs in slide_show:
        string = ""
        for i in indexs:
            string += str(i)+" "
        out.write(string+"\n")
    out.close()


output("a-out.txt")


