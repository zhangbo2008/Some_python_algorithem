"""
Created on Fri Sep 28 15:22:29 2018


直方图均衡化是使用图像直方图对对比度进行调整的图像处理方法。目的在于提高图像的全局对比度，使亮的地方更亮，暗的地方更暗。常被用于背景和前景都太亮或者太暗的图像，尤其是 X 光中骨骼的显示以及曝光过度或者曝光不足的图片的调整。

作者：caoqi95
链接：https://www.jianshu.com/p/726b7b284ef3
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


@author: Binish125
"""
import copy
import os

import numpy as np

import cv2
import matplotlib.pyplot as plt


class contrastStretch:
    def __init__(self):
        self.img = ""
        self.original_image = ""
        self.last_list = []
        self.rem = 0
        self.L = 256
        self.sk = 0
        self.k = 0
        self.number_of_rows = 0
        self.number_of_cols = 0

    def stretch(self, input_image):
        self.img = cv2.imread(input_image, 0)  # 0表示按照灰度图读取.
        self.original_image = copy.deepcopy(self.img)
        x, _, _ = plt.hist(self.img.ravel(), 256, [0, 256], label="x")
        self.k = np.sum(x)
        for i in range(len(x)):
            prk = x[i] / self.k  # 当前颜色锁站比例.
            self.sk += prk
            last = (self.L - 1) * self.sk
            if self.rem != 0:
                self.rem = int(last % last)
            last = int(last + 1 if self.rem >= 0.5 else last)
            self.last_list.append(last)
            self.number_of_rows = int(np.ma.count(self.img) / self.img[1].size)
            self.number_of_cols = self.img[1].size
        for i in range(self.number_of_cols):
            for j in range(self.number_of_rows):
                num = self.img[j][i]
                if num != self.last_list[num]:
                    self.img[j][i] = self.last_list[num]
        cv2.imwrite("output_data/output.jpg", self.img)

    def plotHistogram(self):
        plt.hist(self.img.ravel(), 256, [0, 256])

    def showImage(self):
        cv2.imshow("Output-Image", self.img)
        cv2.imshow("Input-Image", self.original_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    file_path =  "image_data/input.jpg"
    print(file_path)
    stretcher = contrastStretch()
    stretcher.stretch(file_path)
    stretcher.plotHistogram()
    stretcher.showImage()
