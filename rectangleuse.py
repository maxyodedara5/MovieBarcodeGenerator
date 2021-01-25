import numpy
import os
import sys
from cv2 import cv2
import json
from PIL import Image as im

barcode_width = 10
barcode_height = 250

avgs = json.loads(open("outputfile").read())
avgs = numpy.array(avgs, dtype="int")


for i, (x, y,z) in enumerate(avgs): 
    avgs[i] = (int(x), int(y) , int(z))

for i in avgs:
    print(i)

sampleimage = cv2.imread("red.jpg",1)
cv2.imshow("SampleImage", sampleimage)
cv2.waitKey(0)


#MAIN PROBLEM IS CONVERTING THE ARRAY LIST TO TUPLES 
#CONVERT THE ARRAY LIST TO TUPLE AND LOOP FOR RECTANGLE DIMENSIONS 

avg = cv2.mean (sampleimage) [:3]
cv2.rectangle(sampleimage, (50,50), (150,150), avg , -1 )
cv2.imshow("SampleImage", sampleimage)
cv2.waitKey(0)


barcode = numpy.zeros((barcode_height , len(avgs) * barcode_width , 3), dtype="uint8")
cv2.imshow("Barcode" , barcode)
cv2.waitKey(0)
