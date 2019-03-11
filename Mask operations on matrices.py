from __future__ import print_function
import sys
import time
import numpy as np
import cv2 as cv


if __name__ == "__main__":
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    kernel_sobel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]],np.float32)
    img = cv.imread("lena.png")
    dst = cv.filter2D(img,-1,kernel)
    # ddepth = -1, means destination image has depth same as input image
    cv.namedWindow("Input", cv.WINDOW_AUTOSIZE)
    cv.namedWindow("Output", cv.WINDOW_AUTOSIZE)
    cv.imshow("Input",img)
    # cv.waitKey()
    cv.imshow("Output",dst)
    cv.waitKey()
    cv.destroyAllWindows()