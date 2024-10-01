import cv2
import numpy as np
import math

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Lab2-1'
cv2.namedWindow(windowName)

POINT_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 100)

verts = []

def draw(u):
    global verts
    
    def draw_bresenham(u, v):
        
        print('u', u, 'v', v)
        x0, y0 = u
        x1, y1 = v
        
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
    
    verts.append(u)
    if len(verts)  >= 2:
        if len(verts) > 2:
            verts = verts[1:]
            
        draw_bresenham(verts[0], verts[1])
    
    cv2.circle(img, verts[0], 3, POINT_COLOR, -1)
    cv2.circle(img, verts[1], 3, POINT_COLOR, -1)
    

    

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        draw((x, y))
        

cv2.setMouseCallback(windowName, mouse_callback)

while True:
    cv2.imshow(windowName, img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
