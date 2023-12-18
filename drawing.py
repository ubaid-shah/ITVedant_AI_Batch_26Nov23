import cv2
img=cv2.imread('zebra.jpg')

cv2.line(img,(0,0),(640,427),(59,156,48),3)
cv2.line(img,(0,427),(427,427),(0,0,255),3)
cv2.rectangle(img,(50,50),(100,100),(0,255,0),2)
cv2.circle(img,(600,600),70,(159,248,150),2)

cv2.rectangle(img,(150,150),(500,500),(255,0,0),-1)
cv2.putText(img,"Rectangle",(150,140),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()