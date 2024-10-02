import cv2
import numpy as np
import math

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Lab2-2'
cv2.namedWindow(windowName)

POINT_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 100)

control_points = []

def draw(u):
    global control_points

    def draw_verts():

        for u in control_points:
            cv2.circle(img, u, 3, POINT_COLOR, -1)
    
    def draw_bresenham(u, v):
        
        print('line:', 'u', u, 'v', v)
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
    
    
    def draw_rectangle(u, v):
        
        line = lambda u, v: draw_bresenham(u, v)

        u, v =  np.array( [ min(u[0], v[0]), min(u[1], v[1])] ) ,  np.array([max(u[0], v[0]), max(u[1], v[1])])
        d = v - u
        
        line(u, u + [d[0], 0])      # top
        line(u + [0, d[1]], u + d)  # bottom
        line(u, u + [0, d[1]])      # left
        line(u + [d[0], 0], u + d)  # right
       
    
    control_points.append(u)

    if len(control_points) >= 2:
        draw_rectangle(control_points[0], control_points[1])
        draw_verts()
        control_points = []
        return
            
    draw_verts()
    
    
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

