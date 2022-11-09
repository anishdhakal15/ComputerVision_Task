import numpy as numpy
import cv2
import imutils


imgs = []
img = cv2.imread('rectangle.png')
imgGry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , _ = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.015*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),1)
    x= approx.ravel()[0]
    y = approx.ravel()[1]-5

    if len(approx)==4:
        x,y,w,h = cv2.boundingRect(approx)
        newIMG = imgGry[y:y+h,x:x+w]
        a=cv2.minAreaRect(contour)
        box = cv2.boxPoints(a)
        box = numpy.int0(box)
        center,size,angle=a[0],a[1],a[2]
        center,size = tuple(map(int,center)),tuple(map(int,size))
        print(w,h)


        if angle>50:

            M = cv2.getRotationMatrix2D((w//2,h//2),angle+270,1)
            rotated = cv2.warpAffine(newIMG,M,(w,h))
            img_final = cv2.getRectSubPix(rotated,tuple(size[::-1]),(w//2,h//2))
        else:
            M = cv2.getRotationMatrix2D((w//2,h//2),angle,1)
            rotated = cv2.warpAffine(newIMG,M,(w,h))
            img_final = cv2.getRectSubPix(rotated,size,(w//2,h//2))

        
        # img_padded = cv2.copyMakeBorder(img_final,10,10,10,10,cv2.BORDER_CONSTANT,value = (255,0,0))
        imgs.append(cv2.resize(img_final,(w,100), interpolation = cv2.INTER_NEAREST))



final = numpy.concatenate(tuple(imgs),axis=1)
cv2.imshow("final",final)
cv2.waitKey(0)
cv2.destroyAllWindows()