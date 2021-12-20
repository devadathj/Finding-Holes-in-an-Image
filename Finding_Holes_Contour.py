import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

impath = glob.glob('1fps\*png')
for i in impath:
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    cannyimg = cv2.Canny(gray,50,250)

    contours, _ = cv2.findContours(cannyimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    count = 0
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True), True)
        
        if len(approx) >= 6: 
            cv2.drawContours(img,[approx],0,(255,0,255),4)
            count += 1
            
    plt.imshow(img)
    plt.axis('off')
    plt.show()