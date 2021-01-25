import numpy
import os
import sys
from cv2 import cv2
import json

#Get video
cap = cv2.VideoCapture('Dota 2 Aghanim’s Labyrinth Trailer.mp4')

#calculate frames to get average of 
framecountvideo = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print ("Total number of frames in video file : " + str (framecountvideo))

#calulate frames to skip 
#initalizing the vars
skipcount = 1
framecount = framecountvideo

while (True):
    framecount = framecountvideo
    framecount = framecount / skipcount
    if (framecount < 1200):
        break
    skipcount += 1 

print("Frame count now is " + str(framecount))
print("Skiprate is " + str(skipcount))

#initalizing array for frame indexes 
#these frames will be considered for creating the barcode
print("=======")
print(framecount)
framecount = int(framecount)
print(framecount)
skiprate = skipcount 
frameindexs = []
for x in range(1, framecountvideo, skiprate):
  frameindexs.append(x) 


print("Frame index array now has " + str(len(frameindexs)))

#get the average color of each frame 
#avgs array contains all the averages for each frame
avgs = []
indexpos = 0
i = 0
for i in frameindexs:
    cap.set(1,i)
    ret, frame = cap.read()
    avg = cv2.mean (frame) [:3]
    print("current frame index : " + str(i))
    avgs.append(avg)


#confirming the dimensions for barcode image 

barcode_image = "colorcandy.png"
#output image

barcode_width = 1
#should be usally 1, for sample making this as 10 

barcode_height = 300
#height of image 250px

barcode = numpy.zeros((barcode_height , len(avgs) * barcode_width , 3), dtype="uint8")
#allocate memory for the barcode visualization

#filling the barcodes with colors from averages
for (i, avg) in enumerate(avgs):
    cv2.rectangle(barcode, ( i * barcode_width , 0), ((i+1) * barcode_width , barcode_height) , avg , -1)

cv2.imwrite(barcode_image , barcode)
createdimage = cv2.imread("colorcandy.png" , 1)
cv2.imshow("Barcode" , createdimage)
cv2.waitKey(0)


#Video by Kelly Lacy from Pexels