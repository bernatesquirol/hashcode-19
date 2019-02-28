import numpy as np
# photos: list of all available photos (unified into slides)
# p: current photo
alpha = 0.1
alphaIncrement = 2


# +
def findPhoto(p):
    global photos
    for i in range(photos.shape[0]):
        if photos[i]['id'] == p['id']: return i
    return -1

def getScore(p1, p2):
    t1, t2 = p1['tags'], p2['tags']
    inter = np.intersect1d(t1, t2)
    s1 = np.setdiff1d(t1, inter)
    s2 = np.setdiff1d(t2, inter)
    return min(inter.shape[0], s1.shape[0], s2.shape[0])


# -

nextPhoto(p)



getScore(p, q)




