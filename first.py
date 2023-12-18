import cv2
img=cv2.imread('zebra.jpg',0)

cv2.imshow('zebra image',img)

cv2.waitKey(1000)

cv2.destroyAllWindows()
