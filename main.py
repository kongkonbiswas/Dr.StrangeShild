import cv2
import mediapy
video=cv2.VideoCapture(0)

while True:
    ret,img=video.read()
    cv2.imshow("Image",img)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.relase()
cv2.destroyAllWiindows()