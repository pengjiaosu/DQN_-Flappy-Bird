import cv2
import numpy as np

def pre_processing(image, width, height):
    #图片变灰
    image = cv2.cvtColor(cv2.resize(image, (width, height)), cv2.COLOR_BGR2GRAY)
    #进行阈值二值化操作，大于阈值1的，使用255表示， 小于阈值1的，使用0表示
    _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
    print(image)
    return image[None, :, :].astype(np.float32)

