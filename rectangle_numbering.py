import numpy as numpy
import cv2
import imutils

        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        # close = cv2.morphologyEx(t2,cv2.MORPH_CLOSE,kernel,iterations=2)
        # horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (35,2))
        # detect_horizontal = cv2.morphologyEx(close,cv2.MORPH_OPEN,horizontal_kernel,iterations=2)
        # c2 , _ = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rectangleMap = {}
valuesMap = {}

# function to take individual rectangle and store mean of lines
def lineMeanUpdate():
    if len(rectangleMap.keys())!=0:
        for rect in rectangleMap:
            location,image = rectangleMap[rect][0],rectangleMap[rect][1]
            _, t2 = cv2.threshold(image, 240 , 255, cv2.THRESH_BINARY)

            # subtracting two contours images to generate remaining line 
            c2 , hir = cv2.findContours(t2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            c1 , hir = cv2.findContours(t2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
            img2 = image.copy()
            img1 = image.copy()
            for c in c2:
                    apx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,False),False)
                    cv2.drawContours(image=img2, contours=c, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

            for c in c1:
                    apx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,False),False)
                    cv2.drawContours(image=img1, contours=c, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
            imgf = cv2.subtract(img2,img1)
            mask1 = cv2.morphologyEx(imgf,cv2.MORPH_OPEN,numpy.ones((2,2),dtype=numpy.uint8))
        #     imgf = abs(255-imgf)
            coords = cv2.findNonZero(mask1)
        #     x,y,w,h = cv2.boundingRect(coords)
            valuesMap[int(coords[0].mean())] = location
        #     _, t2 = cv2.threshold(imgf, 100 , 255, cv2.THRESH_BINARY)
        #     c2 , hir = cv2.findContours(t2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #     a=cv2.minAreaRect(c2[0])
        #     box = cv2.boxPoints(a)
        #     box = numpy.int0(box)
        #     print(numpy.int0(imgf).mean())
        #     for c in c2:
        #         appro = cv2.approxPolyDP(c2[0], 0.015*cv2.arcLength(contour,True),True)
        #         cv2.drawContours(image=imgf, contours=appro, contourIdx=-1, color=(233, 255, 0), thickness=1, lineType=cv2.LINE_AA)
        #         x,y,w,h = cv2.boundingRect(appro)
        #         print(w,h)
        #     cv2.imshow("img1",imgf)
            # cv2.imshow("img2",img2)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()


# reading image and converting to greyscale
img = cv2.imread('rectangle.png')
imgGry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# function to set text on the basis of thir crosponding line mean
def setText():
        if len(valuesMap.keys())!=0:
                values = [i for i in valuesMap.keys()]
                values.sort(reverse=True)
                c=1
                for i,j in enumerate(values):
                        cv2.putText(img,str(i+1),valuesMap[j],cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

                






# edged = cv2.Canny(imgGry,30,200)
count = 1
_, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
# contours , _ = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours , _ = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.015*cv2.arcLength(contour,True),True)
    cv2.drawContours(image=img, contours=approx, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # cv2.drawContours(img,[approx],0,(0,0,0),1)
    x= approx.ravel()[0]
    y = approx.ravel()[1]-5

    if len(approx)==4:
        x,y,w,h = cv2.boundingRect(approx)
        newIMG = imgGry[y:y+h,x:x+w]
        rectangleMap[count]=[(x+60,y+w),newIMG]
        

        # cv2.putText(img,str(count),(x,y+w),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        count +=1



lineMeanUpdate()
setText()

cv2.imshow("grey",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Hough line detection failed
# edges = cv2.Canny(newIMG,100,200,apertureSize=3)
#         lines = cv2.HoughLines(edges,1,numpy.pi/180,100,30,10)
#         for line in lines:
#             rho,theta = line[0]
#             a=numpy.cos(theta)
#             b=numpy.sin(theta)
#             x0 = a*rho
#             y0 = b*rho
#             x1 = int(x0+100*(-b))
#             y1 = int(y0+100*(a))
#             x2 = int(x0-100*(-b))
#             y2 = int(y0-100*(a))
#             cv2.line(newIMG,(x1,y1),(x2,y2),(0,0,255),2)
#             cv2.imshow("grey",newIMG)
#             cv2.waitKey(0)
#             cv2.destroyAllWindows()