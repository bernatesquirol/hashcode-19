# +
import numpy as np
# photos: list of all available photos (unified into slides)
# p: current photo
photos = np.array([{'id': [0], 'orientation': 'H', 'tags': np.array(['cat', 'beach', 'sun'], dtype='<U5'), 'num': 3},
 {'id': [1,2], 'orientation': 'V', 'tags': np.array(['selfie', 'smile','garden'], dtype='<U6'), 'num': 3},
 {'id': [3], 'orientation': 'H', 'tags': np.array(['garden', 'cat'], dtype='<U6'), 'num': 2}])

p = {'id': [3], 'orientation': 'H', 'tags': np.array(['garden', 'cat'], dtype='<U6'), 'num': 2}
q = {'id': [0], 'orientation': 'H', 'tags': np.array(['cat', 'beach', 'sun'], dtype='<U5'), 'num': 3}
alpha = 0.1
alphaIncrement = 2


# -

def nextPhoto(p):
    global alpha, photos
    if photos.shape[0] <= 0: return "Photos array is empty!"
    
    while True:
        absolutePercentile = int(alpha*photos.shape[0])
        if absolutePercentile >= 2: break
        else: alpha = min(alphaIncrement*alpha, 1.0)
    
    i = findPhoto(p)
    if i == -1: return "Original photo not found in photos!"
    
    candidates = list(photos[i-int(absolutePercentile/2) : i+int(absolutePercentile/2)])
    
    if len(candidates) <= 0: return "Empty candidates!"
    
    candidates.sort(key=lambda x: getScore(p,x), reverse = True)
    bestCandidate = candidates[0] if candidates[0] != p else candidates[1]
    
    photos = np.delete(photos, i)
    #print(candidates)
    return bestCandidate#, getScore(p, bestCandidate)


nextPhoto(p)


def getScore(p1, p2):
    t1, t2 = p1['tags'], p2['tags']
    inter = np.intersect1d(t1, t2)
    s1 = np.setdiff1d(t1, inter)
    s2 = np.setdiff1d(t2, inter)
    return min(inter.shape[0], s1.shape[0], s2.shape[0])


getScore(p, q)


def findPhoto(p):
    global photos
    for i in range(photos.shape[0]):
        if photos[i]['id'] == p['id']: return i
    return -1


