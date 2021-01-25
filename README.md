# Movie Barcode Generator

Creates a barcode of the movie by taking the average color of the frames and stacking them left to right

By stacking the frames, we get a timeline of the use of color throughout the movie

## Dependencies

Following libraries need to be installed  
* numpy
* cv2

## Working

Total number of frames are calculated from the video file usually the number of frames is very large as per the video size, we normalize that amount by skipping certain number of frames and try to keep the output image with around 1000 pixels of width and 300 pixels of height

Then average color of the frames are calculated and the output barcode image is filled with these colors respectively 

### Example 

The image below is created after calculating the average from the video of the Dota 2 game trailer for one of the in game events 

![Aghanim's Labyrinth Trailer ](AghanimsFrames.bmp)

Video link [Aghanim's Labyrinth Trailer](https://www.youtube.com/watch?v=4QxqctzXQqc&ab_channel=dota2)

If we have a look at the video the color scheme gradually changes to blue so does our movie barcode, the same principle will be applied to larger videos

