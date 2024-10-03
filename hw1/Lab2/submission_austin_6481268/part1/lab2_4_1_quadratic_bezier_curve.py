import cv2
import numpy as np
import math

img = np.zeros((512, 512, 3), np.uint8)
windowName = 'Lab2-4-1'
cv2.namedWindow(windowName)

# Store points for the Bezier curve
control_points = []

POINT_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 100)
ARC_SAMPLES = 100


line = lambda u, v: cv2.line(img, u, v, LINE_COLOR, 1)
point = lambda u: cv2.circle(img, u, 3, POINT_COLOR, -1)


def draw(u):
    
    global control_points
    
    def draw_all_points():
        for u in control_points:
            point(u)
    
    def calc_qudratic_curve(ps):
        n = len(ps)
        ps0, ps1, ps2 = ps[0:n-2], ps[1:n-1], ps[2:n]
        bs = []
        
        for i in np.arange(0, n-2, 2):
            for t in np.linspace(0, 1, ARC_SAMPLES):
                a0 = (ps1[i] - ps0[i]) * t + ps0[i]
                a1 = (ps2[i] - ps1[i]) * t + ps1[i]
                bs += [(a1 - a0) * t + a0]
        
        return bs
    
    def draw_bezier_curve(control_points):

        ps = calc_qudratic_curve(control_points)
        ps0, ps1 = ps[0:len(ps)-1], ps[1:]
        [line(p0.astype(int), p1.astype(int)) for p0, p1 in zip(ps0, ps1)]


    control_points += [u]
    if len(control_points) >= 3:
        draw_bezier_curve(control_points)
        
    draw_all_points()


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        img = np.zeros((512, 512, 3), np.uint8)
        draw(np.array([x, y]))

def window_should_close():
    keyCode = cv2.waitKey(10)
    flag = False
    flag |= (keyCode & 0xFF) == 27
    flag |= cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1
    return flag

cv2.setMouseCallback(windowName, mouse_callback)

while True:
    cv2.imshow(windowName, img)
    
    if window_should_close():
        break
    
cv2.destroyAllWindows()

