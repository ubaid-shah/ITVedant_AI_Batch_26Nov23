import cv2
import numpy as np
img=cv2.imread('d.jpg')

ed_img=cv2.Canny(img,100,200)
ed_img1=cv2.Canny(img,150,200)

img_dialte=cv2.dilate(ed_img1,np.ones((3,3),dtype=np.uint8))

img_erode=cv2.erode(img_dialte,np.ones((3,3),dtype=np.uint8))


cv2.imshow('ed_img',ed_img)
cv2.imshow('ed_img1',ed_img1)
cv2.imshow('img_dialte',img_dialte)
cv2.imshow('img_erode',img_erode)
cv2.waitKey(0)
cv2.destroyAllWindows()