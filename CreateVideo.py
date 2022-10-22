import os
import cv2


path = "IMAGES"

IMAGES = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
       IMAGES.append(file_name)
        
#print(len(images))
count = len(IMAGES)

frame = cv2.imread(IMAGES[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(count-1,0,-1):
    frame = cv2.imread(IMAGES[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")