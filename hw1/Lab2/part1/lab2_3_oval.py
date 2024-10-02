import cv2
import numpy as np
import math

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Lab2-3'
cv2.namedWindow(windowName)

POINT_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 100)

RADIUS_X = 100
RADIUS_Y = 50
SAMPLES = 100

def draw(u):

    def draw_bresenham(u, v):
        
        x0, y0 = u[0], u[1]
        x1, y1 = v[0], v[1]
        
        # integer arithmetic, all cases
        # https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm#All_cases
        dx = np.abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -np.abs(y1 - y0)
        sy =  1 if y0 < y1 else -1
        
        error = dx + dy

        while True:
            cv2.circle(img, (x0, y0), 1, LINE_COLOR, -1)
            
            if x0 ==x1 and y0 == y1:
                break
            
            e2 = 2 * error
            
            if e2 >= dy:
                error = error + dy
                x0 = x0 + sx
                
            if e2 <= dx:
                error = error + dx
                y0 = y0 + sy
    
    def draw_oval(o):
        
        line = lambda u, v: draw_bresenham(u, v)

        theta = np.linspace(0, np.pi * 2, SAMPLES)
        xs = np.cos(theta) * RADIUS_X + o[0]
        ys = np.sin(theta) * RADIUS_Y + o[1]

        us = np.column_stack((xs[:-1], ys[:-1])).astype(int)
        vs = np.column_stack((xs[1:], ys[1:])).astype(int)

        [line(u, v) for u, v in zip(us, vs)]
       
    cv2.circle(img, u, 3, POINT_COLOR, -1)
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
