import cv2
import numpy as np
import math

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Lab2-3'
cv2.namedWindow(windowName)

POINT_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 100)

line = lambda u, v: cv2.line(img, u, v, LINE_COLOR, 1)
point = lambda u: cv2.circle(img, u, 3, POINT_COLOR, -1)

RADIUS_X = 100
RADIUS_Y = 50
SAMPLES = 100

def draw(u):
    def draw_oval(o):
        
        theta = np.linspace(0, np.pi * 2, SAMPLES)
        xs = np.cos(theta) * RADIUS_X + o[0]
        ys = np.sin(theta) * RADIUS_Y + o[1]

        us = np.column_stack((xs[:-1], ys[:-1])).astype(int)
        vs = np.column_stack((xs[1:], ys[1:])).astype(int)

        [line(u, v) for u, v in zip(us, vs)]
    point(u)
    draw_oval(u)
    

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        draw(np.array([x, y]))
        
def window_should_close():
    keyCode = cv2.waitKey(10)
    flag = False
    flag |= (keyCode & 0xFF) == 27
    flag |= cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1
    return flag
    
# Main
cv2.setMouseCallback(windowName, mouse_callback)

while True:
    cv2.imshow(windowName, img)
    
    if window_should_close():
        break
    
cv2.destroyAllWindows()
