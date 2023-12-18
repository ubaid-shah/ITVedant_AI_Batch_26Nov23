import cv2
img=cv2.imread('handwritten.png')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh_img=cv2.threshold(img_gray,128,255,cv2.THRESH_BINARY)

ada_thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY,21,30)

cv2.imshow('img',img_gray)
cv2.imshow('thresh_img',thresh_img)
cv2.imshow('ada_thresh',ada_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()