import cv2 as cv




if __name__ == "__main__":
    src1 = cv.imread("lena.png")
    src2 = cv.imread("Lily.jpg")
    src2 = cv.resize(src2,(512,512),cv.INTER_CUBIC)
    dst = cv.addWeighted(src1,0.5,src2,0.5,0.0)
    cv.imshow("dst",dst)
    cv.waitKey()
    cv.destroyAllWindows()