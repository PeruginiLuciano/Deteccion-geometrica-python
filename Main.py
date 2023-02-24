import cv2
import numpy as np
imagen = cv2.imread('Figuras.png')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny= cv2.Canny(gray,10,150)
Binalizada=np.uint8((gray<220)*255)

cv2.imshow('gray',gray)
cv2.imshow('canny',canny)
cv2.imshow('BINARIO',Binalizada)
contorno,_= cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(imagen,contorno,-1,(255,0,0),2)

for C in contorno:
    epsilon = 0.01*cv2.arcLength(C, True)
    approx=cv2.approxPolyDP(C,epsilon,True)
    print(len(approx))
    cv2.drawContours(imagen,[approx],0,(255,0,0),2)
    cv2.imshow('image',imagen)
    cv2.waitKey(0)

cv2.imshow('imagen',imagen)
cv2.waitKey(0)

cv2.destroyAllWindows()