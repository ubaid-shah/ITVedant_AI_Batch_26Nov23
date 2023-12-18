import cv2

cap=cv2.VideoCapture('dog.mp4')

while True:
    ret,img=cap.read()

    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(img_gray,128,255,cv2.THRESH_BINARY)

    cnt,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for c in cnt:
        x1,y1,w,h=cv2.boundingRect(c)


    cv2.rectangle(img,(x1,y1),(x1+240,y1+240),(0,255,0),2)
    cv2.putText(img,"Sea Lion",(x1+240,y1+220),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


    cv2.imshow('dog',img)

    if cv2.waitKey(100) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




