import cv2
import numpy as np
from PIL import Image
from PIL import ImageEnhance
import random


def oil_style(img):
    height, width, n = img.shape
    output = np.zeros((height-2, width,n), dtype='uint8')

    for i in range(1,height-2):

        for j in range(width-2):

            if random.randint(1,10) % 3==0:
                output[i, j] = img[i+1,j]
            elif random.randint(1,10) % 2==0:
                output[i, j] = img[i + 2, j]
            else:
                output[i, j] = img[i - 1, j]

    cv2.imshow("oil_img", output)
    cv2.imwrite("oil_img.jpg", output)

def color_add():
    image = Image.open('oil_img.jpg')
    enh_col = ImageEnhance.Color(image)
    color = 2.0
    image_colored = enh_col.enhance(color)
    image_colored.show()


def main():
    global img
    img = cv2.imread('1.jpg')
    oil_style(img)
    color_add()
    # cv2.imshow("img", img)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
