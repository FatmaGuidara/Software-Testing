import cv2 as cv
import numpy as np
import imutils
import matplotlib.pyplot as plt
import easyocr

import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def img2string(img_path):
    img = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    bfilter = cv.bilateralFilter(gray, 11, 17, 17)
    edged = cv.Canny(bfilter, 30, 200)
        
    # f = plt.figure()
    # f.add_subplot(1,2, 1)
    # plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    # f.add_subplot(1,2, 2)
    # plt.imshow(cv.cvtColor(edged, cv.COLOR_BGR2RGB))
    # plt.show(block=True)
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(edged)
    coordinates, text, acuracy = result[0]
    text = text.replace(" ", "")
    # print(text)
    return text


def string2op(op_string):
    return(eval(op_string))

def calculus(img):
      img_string = img2string(img)
      return(string2op(img_string))
      
# image_1 = "images/1+1.png"
# print(calculus(image_1))
# image_2 = "images/10x6.png"
# print(calculus(image_2))
# image_3 = "images/72%2.png"
# print(calculus(image_3))
# image_4 = "images/2000-1999.png"
# print(calculus(image_4))
