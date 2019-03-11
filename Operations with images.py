import cv2 as cv


if __name__ == "__main__":
    img = cv.imread("lena.png")
    img_gray = cv.imread("lena.png",cv.IMREAD_GRAYSCALE)
    #深度不同取不同值
    sobelx = cv.Sobel(img, cv.CV_32F, 1, 0)
    # cv.namedWindow("Input", cv.WINDOW_AUTOSIZE)
    # cv.namedWindow("Output", cv.WINDOW_AUTOSIZE)
    # cv.imshow("Input",img)
    # cv.imshow("Output",img_gray)
    # cv.waitKey()
    cv.imshow("as",sobelx)
    cv.waitKey()
    cv.destroyAllWindows()