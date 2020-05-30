# -*- coding: utf-8 -*-
import numpy as np
import cv2
import platform

print(platform.python_version())

print('ok')
img = cv2.imread('a.jpg')

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

