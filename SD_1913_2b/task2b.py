import cv2
import numpy as np

img = cv2.imread('yellow_detect.jpeg', -1)
clean = cv2.GaussianBlur(img, (5, 5), 0)
hsv = cv2.cvtColor(clean, cv2.COLOR_BGR2HSV)
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(clean, (x, y), (x+w, y+h), (0, 0, 255), 3)
        print(int(x+(w/2)), int(y+(h/2)))

