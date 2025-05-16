#Almost all code by troy, only the class and function names are taken from Sethbling

import wscreenshot 
import numpy as np
import pygetwindow as gw
import mss
from skimage import transform

# CapLeft = 512
# CapRight = 640
# CapTop = 334
# CapBottom = 366

# ColorDepth = 3

frameshape = [32, 28, 4]

def get_bizhawk_bbox():
    windows = gw.getWindowsWithTitle("SNES") #bizhawk window name changes after the loaded game
    for win in windows:
        
		#Return bounding box (left, top, width, height)
    	return {
                "left": win.left,
                "top": win.top,
                "width": win.width,
                "height": win.height
            	}


class screen_cap:
    def __init__(self):
        # self.cap = wscreenshot.Screenshot()
        # self.frame = None
        # wscreenshot.list_window_names() #troytest, gets open window memory and names
        self.cap = get_bizhawk_bbox()
        if self.cap == None:
              print("Game window not found! Big sad")
		
    def get(self):
        screenshot = mss.mss()
        frame = screenshot.grab(self.cap)
        frame = np.array(frame)
        frame = transform.resize(frame, (32, 28), anti_aliasing= True)
        # print(frame.shape) #test, gives the array size of the frame
        shape = frame.shape
        frame = frame.reshape(shape[0]*shape[1]*shape[2]) #turns the frame into a 2D array (necessary for Tensorflow later)
        # print(frame.shape) #test, gives the new array size 
        
        
        # Crop safely
        # cropped = frame[CapTop:CapBottom, CapLeft:CapRight]
        return frame
    
    def size(self):
        return  [frameshape[0]*frameshape[1]*frameshape[2]]  #[CapBottom - CapTop, CapRight - CapLeft, ColorDepth]
    
