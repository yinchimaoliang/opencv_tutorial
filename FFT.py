import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



class Main():
    def __init__(self):
        self.img = cv.imread("lena.png",0)

    def main(self):
        f = np.fft.fft2(self.img)
        fshift = np.fft.fftshift(f)
        s1 = np.log(np.abs(fshift))
        plt.subplot(131)
        plt.imshow(self.img,"gray")
        plt.subplot(132)
        plt.imshow(s1)
        # plt.show()
        inv = np.fft.ifftshift(fshift)
        inv = np.fft.ifft2(inv)
        inv = np.abs(inv)
        plt.subplot(133)
        plt.imshow(inv,"gray")
        plt.show()


if __name__ == "__main__":
    t = Main()
    t.main()
