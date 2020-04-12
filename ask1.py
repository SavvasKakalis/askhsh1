from PIL import Image
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import sys


img = np.array(Image.open(sys.argv[1]))        
rows = img.shape[0]
columns = img.shape[1]

img.astype(float)
copy= np.zeros([rows,columns])
print(img.shape)
if(len(img.shape)==3):  # an einai eghromi th metatrepw se grayscale
    for i in range (0, rows):
        for j in range (0, columns):
            copy[i][j]=(img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3 #mesos oros rgb
else:
    copy = img

katwfli=int(sys.argv[3]) # trito orisma grammis entolon


result = np.zeros([rows,columns])
for i in range (0,rows):
    for j in range (0,columns):
        if(copy[i][j] > katwfli):
            result[i][j] = 255  
        else:
            result[i][j] = 0 

plt.imshow(result,"gray")
plt.show()
Image.fromarray(result.astype(np.uint8)).save(sys.argv[2])



