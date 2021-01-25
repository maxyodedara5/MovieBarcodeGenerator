
framecount = 30867
skipcount = 2 

count = 1 
for i in range (1,30):
    print( framecount / i)
    print(i)
    print("iteration now is : " + str(i))
    
skipcount = 1 
framecount = 30867
while (True):
    framecount = 30867
    framecount = framecount / skipcount
    if (framecount < 1200):
        break
    skipcount += 1 
    print ("Frames skipped : " + str(skipcount) )
    print ("Current frames : " + str(framecount) )

print("-------------------------")
print(framecount)
print(skipcount)