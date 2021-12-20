import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 1 
color = (0, 0, 255) 
thickness = 4

impath = glob.glob('1fps\*png')
for i in impath:
    img = cv2.imread(i)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    cirloc = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, param1 = 45, param2 = 25, minRadius = 50, maxRadius = 100)
    circles = np.uint16(np.around(cirloc))
    cirs = circles[0]
    cirs = sorted(cirs, key = lambda x: x[2])
    
    k = len(cirs) - 1
    while k > 0:
        x1, y1, r1 = cirs[k]
        x1, y1, r1 = int(x1), int(y1), int(r1)
        j = k - 1
        while j >= 0:
                x2, y2, r2 = cirs[j]
                x2, y2, r2 = int(x2), int(y2), int(r2)
                if (((x1 - x2)**2) + ((y1 - y2)**2))**0.5 < (r1 + r2):
                    break
                j -= 1
        if j == -1:
            cv2.circle(img, (x1, y1), r1, (255, 0, 255), 3)
            cv2.putText(img, str(r1), (x1 - 20, y1 - 20), font, fontScale, color, thickness, cv2.LINE_AA) 
        k -= 1
    cv2.circle(img, (int(cirs[0][0]), int(cirs[0][1])), int(cirs[0][2]), (255, 0, 255), 3)
    cv2.putText(img, str(int(cirs[0][2])), (int(cirs[0][0]) - 20, int(cirs[0][1]) - 20), font, fontScale, color, thickness, cv2.LINE_AA) 
        
    plt.imshow(img)
    plt.axis('off')
    plt.show()
