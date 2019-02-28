import Utils
import numpy as np

data = Utils.readData("b_lovely_landscapes.txt")
data = np.array(sorted(data, key=lambda x: -x['num']))


# +
def selectFirstImage(data):
    toret = data[0]
    data = np.delete(data,0)
    return toret

def selectBestPartner(image,data):
    toret = data[0]
    data = np.delete(data,0)
    return toret


# +
print(data[:2])

current_slide = selectFirstImage(data)

print(data[:2])

slide_show = np.array([current_slide['id']])

print(slide_show)

print(data.shape[0])

while(data.shape[0]!=0):
    print(data.shape[0])
    next_slide = selectBestPartner(current_slide,data)
        
    np.append(slide_show,next_slide['id'])
    current_slide = next_slide




# -

import numpy as np
def output(filepath):
    out = open(filepath, 'w')
    out.write(str(slide_show.size)+"\n")
    for indexs in slide_show:
        string = ""
        for i in indexs:
            string += str(i)+" "
        out.write(string+"\n")
    out.close()


output("b-out.txt")


