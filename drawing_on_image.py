import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline 


#variables

#while mouse button down then done = false else otherwise
done = False
ix,iy = -1,-1

#function

def draw_rectangle(event,x,y,flags,params):
    #pass
    global ix,iy,done
    
    if event == cv.EVENT_LBUTTONDOWN:
        done = True
        ix,iy = x,y
        
    elif event == cv.EVENT_LBUTTONUP:
        done=False
        
        cv.rectangle(img,(ix,iy),(x,y),color = (0,255,0), thickness = -1)
        
    elif event == cv.EVENT_MOUSEMOVE:
        if done == True:
            cv.rectangle(img,(ix,iy),(x,y),color = (0,255,0), thickness = -1)
            


img = np.zeros((512,512,3))

cv.namedWindow(winname="win_name")

cv.setMouseCallback("win_name",draw_rectangle)


while True:
    cv.imshow("win_name",img)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        
cv.destroyAllWindows()
