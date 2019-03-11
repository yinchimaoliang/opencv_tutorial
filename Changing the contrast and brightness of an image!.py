import cv2 as cv

img = cv.imread("lena.png")

dst = cv.convertScaleAbs(img,alpha = 1,beta = 100)

cv.imshow("dst",dst)
cv.waitKey()
cv.destroyAllWindows()