import numpy
import os
import sys
from cv2 import cv2
import json


#Get video
cap = cv2.VideoCapture('ColorCandies.mp4')

#calculate frames to get average of 
framecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print ("Total number of frames in video file : " + str (framecount))

#calulate frames to skip 
skipcount = 1 
framecount = 30867
while (True):
    framecount = 30867
    framecount = framecount / skipcount
    if (framecount < 1200):
        break
    skipcount += 1 




skiprate = 28 
nums = []
for x in range(1, framecount, skiprate):
  nums.append(x) 

#print frames position
print(nums)

avgs = []

indexpos = 0
i = 0
while i < 1000:
    cap.set(1,nums[indexpos])
    ret, frame = cap.read()
    avg = cv2.mean (frame) [:3]
    avgs.append(avg)
    indexpos += 1
    i += 1




#for i in nums:
    #cap.set(1,i)
    #ret, frame = cap.read()
    #cv2.imshow('frame',frame)
    #cv2.waitKey(0) & 0xFF == ord('q')
    #avg = cv2.mean (frame) [:3]
    #avgs.append(avg)

cv2.destroyAllWindows()
print("Writing the average to JSON file")

f = open("outputfile" , "w")
f.write(json.dumps(avgs))
f.close()




print("[INFO] {:,} total frame averages saved".format(len(avgs)))

#avgs = numpy.array(avgs , dtype="uint")

barcode_image = "B99S7E1.png"
#output image

barcode_width = 1
#should be usally 1, for sample making this as 10 

barcode_height = 768
#height of image 250px

barcode = numpy.zeros((barcode_height , len(avgs) * barcode_width , 3), dtype="uint8")
#allocate memory for the barcode visualization

for (i, avg) in enumerate(avgs):
    cv2.rectangle(barcode, ( i * barcode_width , 0), ((i+1) * barcode_width , barcode_height) , avg , -1)







cv2.imwrite(barcode_image , barcode)
createdimage = cv2.imread("B99S7E1.png" , 1)
cv2.imshow("Barcode" , createdimage)
cv2.waitKey(0)





while (False):
    ret, frame = cap.read()

    #gry = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame' , frame)
   
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
