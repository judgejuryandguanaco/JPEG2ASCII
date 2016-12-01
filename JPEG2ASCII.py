# JPEG2ASCII4

import cv2
import numpy as np
import os

def main():
    asciiToNum = {}
    transformedAscii = [])
    img = cv2.imread("img.jpg") # make this user-settable
    if img is None: # is null?
        print "Image doesn't exist\n\n"
        os.system("pause")
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    setupAsciiMapping(asciiToNum)
    print asciiToNum
    print img.shape
    for i in img:
        temp = []
        for j in i:
            temp.append(asciiToNum[j])
        transformedAscii.append(temp)
    ascii = ''
    for i in transformedAscii:
        ascii += ' '.join(i
        ascii += '\n'
    print ascii
    return

def setupAsciiMapping(asciiToNum):
    characterSet = list(('#'*8)+('-'*8)+('.'*10))
    for i in range(26):
        for j in range(10):
            asciiToNum[i*10+j] = characterSet[i]

if __name__ == "__main__":
    main()