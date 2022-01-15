import cv2
import numpy as np


Path =r'C:\Users\ds-01\Documents\Opencv'
cap = cv2.VideoCapture(0)
cap.set(10, 128)
cap.set(11,32)

while(True):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite(Path + 'test.png', frame)
        break



print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))

cap.release()
cv2.destroyAllWindows()

#Entferunung 33 cm

"""DUNKELBILD
frame width: 640.0
frame height: 480.0
--------------------------------
brightness: 128.0
contrast: 255
saturation: 32.0
--------------------------------
gain: 0.0
exposure: -7.0
--------------------------------
white balance: -1.0

GRAUWERTKEIL

frame width: 640.0
frame height: 480.0
--------------------------------
brightness: 128.0
contrast: 32.0
saturation: 32.0
--------------------------------
gain: 0.0
exposure: -7.0
--------------------------------
white balance: -1.0

Weißbild

frame width: 640.0
frame height: 480.0
--------------------------------
brightness: 77
contrast: 32.0
saturation: 32.0
--------------------------------
gain: 0.0
exposure: -7.0
--------------------------------
white balance: -1.0


"""
